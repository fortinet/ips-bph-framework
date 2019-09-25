#!/usr/bin/python
#
# Copyright 2019 Fortinet Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import time
import box
import os
import tempfile
import pickle
import uuid
from termcolor import colored

# Custom imports
from bph.core.logger import BphLogger as Logger
from bph.core.constants import *
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile
from bph.core.constants import *

class BphTemplate:
    def __init__(self):
        self.logger = Logger(level='INFO', module=self.__module__)
        
class BphToolTemplate(BphTemplate):
    def __init__(self):
        super().__init__()

class BphToolTemplateConfiguration(BphToolTemplate):
    def __init__(self):
        super().__init__()
        
    def __locate_tool_config_file(self, *args):
        """ Search for the Tool config file """

        self.tool_name = args[0]
        self.arch = args[1]
        self.version = args[2]
        self.tool_directory = None
        self.md5 = Session.sample_md5
        
        self.logger.log('TemplateConfig #1: {}'.format(self.__dict__), level='DEBUG')

        # Detect the tool's base folder.
        for root, dirs, files in os.walk(BPH_PLUGIN_DIR):
            for directory in dirs:
                if self.tool_name in directory:
                    self.logger.log('Tool Match: {}'.format(self.tool_name), level='DEBUG')
                    tool_dir = os.path.join(root, directory, self.arch)
                    self.logger.log(tool_dir, level='DEBUG')
                    
                    if os.path.isdir(tool_dir):
                        self.logger.log(f"Tool dir: {tool_dir}", level='DEBUG')
                        self.tool_directory = tool_dir

                        # Generating remote tool's path
                        # Peid: E:\basic\static\peid\x86\0.95\peid.exe
                        self.remote_tool_path = "{}\\{}".format(
                            "\\".join(tool_dir.split('/')[5:]), self.version)
                        self.logger.log(f"Remote Tool Path: {self.remote_tool_path}", level='DEBUG')

    def load_tool_config_file(self, tool_name, arch, version, target_file=None):
        """ Loads the tool config file: (JSON data -> BOX object) conversion"""
        try:
            # print(f"Loading Template ({tool_name}) Arch: {arch} Version: ({version})")
            self.__locate_tool_config_file(tool_name, arch, version)
            cfg_file = f"{self.tool_directory}/{self.version}/{self.tool_name}.json"
            self.logger.log('Config file path: {}'.format(cfg_file))
            j = open(cfg_file, 'r')
        except FileNotFoundError as e:
            self.logger.log('Cannot open config JSON file: {}'.format(e), level='DEBUG')

        else:
            self.logger.log('Loading JSON config file', level='DEBUG')
            try:
                json_data = json.load(j)
                
                # This will set the dictionary required to hold
                # custom user variables used in json template/config files.
                json_data['configuration']['execution']['download_sample'] = False                
                json_data['configuration']['execution']['custom_user_vars'] = {}
                json_data['configuration']['execution']['delay'] = 0                
                json_data['actions']['action'] = ""

            except json.JSONDecodeError:
                self.logger.log('Error during JSON decoding', level='DEBUG')
                return False
            else:
                j.close()
                self.logger.log('The JSON config file was loaded correctly', level='DEBUG')

                # The Config JSON data is loaded and then converted
                # into an extended python dict by using the python-box
                # module. Through this way, attributes can be accessed
                # with dot notation:
                #
                #   self.automation.normal_scan.execute = True
                #
                
                self.__dict__.update(box.Box(json_data))

                #print("JSON_AND_DICT_DATA: {}".format(self.__dict__))

            if target_file is None:
                self.logger.log('>> Target file is not set', level='DEBUG')
                self.configuration.execution.download_sample = False
               
            elif target_file is not None:
                self.logger.log('>> Target file is set', level='DEBUG')
                self.configuration.execution.download_sample = True
                self.download_url = target_file.download_url 
            else:
                self.logger.log('>> Unknown target', level='DEBUG')               
                
class BphToolTemplateExecutor(BphToolTemplateConfiguration):

    server_status = None
    template_delivered = False
    template_file = None

    def __init__(self):
        super().__init__()

        # Variables added into the general (not-boxed) JSON Template
        self.module_name = self.__module__
        self.sid = Session.get_session_id()
        self.md5 = Session.sample_md5
        self.project_name = Session.project_name
        self.rid = str(uuid.uuid4())
        self.tool_drive = BPH_REMOTE_TOOLS_DRIVE

    def __dump_command_file(self, tmp_file):
        """ Dump Template's JSON data into Temporary file """
        try:
            tmp = open(tmp_file, 'wb')
            self.logger.log(f"Dumping Template Data into a Tmp file: {tmp.name}", level='DEBUG')

            # At this time self.__dict__ was already boxed.
            # Making a copy of current objetc's dictionaty and removing logger
            # from it. This way the 'logger object' is not included within the
            # template data and regular 'logger; module remains. 
            
            template_data = {}
            
            for k,v in self.__dict__.items():
                if k != "logger":
                    self.logger.log('Key: {} Value: {}'.format(k, v), level='DEBUG')
                    if k not in template_data:
                        template_data.update({k: v})

            if BPH_TEMPLATE_SERVER_OUTPUT:
                self.logger.log(template_data)

            pickle.dump(template_data, tmp, protocol=2)
            
            del template_data
            
            tmp.close()
            
            self.logger.log(self.__dict__, level='DEBUG')
                        
        except IOError:
            self.logger.log("Tmp file can't be written", level='DEBUG')
            return False
        else:
            self.logger.log('Tmp file - OK', level='DEBUG')
            return True

    def __make_cmds_tmp_file(self):
        """ Created Temporary File """
        try:
            self.logger.log('Creating Temporary File', level='DEBUG')
            with tempfile.NamedTemporaryFile(mode='w+b', dir=BPH_TMP_DIR, delete=False, prefix='blackphenix_') as f:
                tmp_file = f.name
        except:
            self.logger.log('Error when creating tmp file', level='DEBUG')
        else:
            self.logger.log('Tmp file created:{}'.format(tmp_file), level='DEBUG')
            return tmp_file

    def _scan_bph_tmp_file(self, clean=False):
        """ Scans Windows Temporary Folder for bph_ files """
        self.logger.log('Scanning...', level='DEBUG')        
        for root, dirs, files in os.walk(BPH_TMP_DIR):
            for file in files:
                # All files matching "blackphenix_" prefix
                if "blackphenix_" in file:
                    bph_tmp_file = "{}{}".format(root, file)

                    if os.path.getsize(bph_tmp_file) != 0:
                        self.logger.log('Tmp file: {}'.format(bph_tmp_file), level='DEBUG')
                        #os.system("ls -lskh {}".format(bph_tmp_file))
                    else:
                        self.logger.log('Removing Empty file...')
                        os.remove(bph_tmp_file)

                    if clean is not False:
                        try:
                            self.logger.log('Cleaning: {}'.format(bph_tmp_file), level='DEBUG')
                            os.remove(bph_tmp_file)
                        except OSError:
                            self.logger.log("Tmp file can't be deleted", level='DEBUG')
                            return False
                        else:
                            self.logger.log('File was removed - cleaned.', level='DEBUG')
                        
                    self.logger.log('Found BphFile: {}'.format(bph_tmp_file), level='DEBUG')
                    return bph_tmp_file
        

    def execute(self, delay=0):
        self.logger.log("Executing Template")

        # If a user choose a delay for execute(), then this 
        # value is passed as parameter within the template
        # request. This will allow the windows agent to pause
        # the same amount of seconds chosen by the execute()
        # function.
        #  <Box: {'admin_required': False, 
        #         'delay': 20}>
        #
        self.configuration.execution.delay = delay
        
        # The 1 sec timeout allows enough time between exec() requests
        # to generate a template file and make it ready for the agent.
        time.sleep(2)

        if not BphToolTemplateExecutor.server_status:
            self.logger.log('Waiting for Agent Connection....')
            
        while True:
            if BphToolTemplateExecutor.server_status:    
                self.logger.log('Agent is Connected. Delivering Template now...')

                # Creates a Temp file to dump the current Boxed content
                # self.__dict__ was created by using box.Box()
                tmp = self.__make_cmds_tmp_file()
                
                # Dumps the self.__dict__ data into the Temporary file
                # This file will be used by the Agent Server to send
                # the file's content to the VM network Agent
                self.__dump_command_file(tmp)
        
                self.logger.log(self.__dict__, level='DEBUG')
                break

        self.logger.log('Template Delivered: {}'.format(BphToolTemplateExecutor.template_delivered), level='DEBUG')
        
        while BphToolTemplateExecutor.template_delivered != True:
            self.logger.log('Waiting to deliver template...')
            time.sleep(5)

        self.logger.log('Template has been delivered.')        
        BphToolTemplateExecutor.template_delivered = False
        self.logger.log('Next instruction will be sent in ({}) seconds'.format(delay))
        time.sleep(delay)

    def output(self, show=False):
        def output_conversor(tool_output_log):
            self.logger.log('output conversor', level='DEBUG')
            tool_output = []
            with open(tool_output_log) as tool_log:
                for line in tool_log:
                    if line not in tool_output:
                        if show: self.logger.log('Adding: {}'.format(line), level='DEBUG')
                        tool_output.append(line.strip())
            return tool_output

        tool_output_log = tool_files_folder = os.path.join(Session.sid_folder, self.tool_name, self.rid, "{}.log".format(self.tool_name)) 
        
        if show: self.logger.log(tool_output_log, level='DEBUG')
        
        while True:
            
            try:
                # Don't give any response until the file has arrived 
                if os.path.isfile(tool_output_log):
                    self.logger.log('Log file was found', level='DEBUG')
                    result_data = output_conversor(tool_output_log)
                    for line in result_data:
                        self.logger.log('Content: {}'.format(colored(line, 'green')))
                    return result_data
            except FileNotFoundError:
                self.logger.log('File has not arrived yet. Retrying in 5 seconds')
                time.sleep(5)
                self.logger.log('Retrying now...')
                self.output(show=show)
            
    def files(self):
        time.sleep(5)
        tool_files_folder = os.path.join(Session.sid_folder, self.tool_name, self.rid)
        self.logger.log('Searching for files now in: {}'.format(tool_files_folder))
        
        files_found = []
        
        while True:
            if os.path.isdir(tool_files_folder):
                self.logger.log('Directory OK', level='DEBUG')
                for root, dirs, files in os.walk(tool_files_folder):
                    for file in files:
                        if file not in files_found:
                            file = os.path.join(root, file)
                            files_found.append(file)
                            
                for file in files_found:
                    self.logger.log(colored('File: {}'.format(os.path.basename(file)), 'green'))                            
    
                return files_found
                     
