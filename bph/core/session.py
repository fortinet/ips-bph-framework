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

import uuid
import time
import os
import shutil 
from termcolor import colored, cprint

# Core imports
from bph.core.exceptions import *
from bph.core.constants import *
from bph.core.os.filesystem import BphDirectory as Directory
from bph.core.sample import BphLabFile as LabFile
from bph.core.logger import BphLogger as Logger

class BphSession:
 
    # Class variables are being used when a template is generated
    project_name = ""
    sample_md5 = ""  
    sid = ""
    sid_folder = ""      
    sample_folder = ""
    launcher_abs_path = ""
    
    def __init__(self, project_name=None):
        self.show_banner()
        self.logger = Logger(level='DEBUG', module=self.__module__)

        if project_name is not None:
            BphSession.project_name = project_name
        else:
            raise BphSessionNameException('Session Name was not provided')

        try:
            sample_abs_path = sys.argv[1]
        except IndexError:
            self.logger.log('Starting session without setting up a sample file...')
        else:
            self.tmp_sample_abs_path = sample_abs_path
            self.logger.log('Setting sample: {}'.format(self.tmp_sample_abs_path))
            BphSession.sample_md5 = LabFile.md5hash(self.tmp_sample_abs_path)
            
        # Session files, folders and identifiers here.
        self.project_folder = os.path.join(BPH_USER_DATA, BphSession.project_name)
        self.session_log_file = os.path.join(self.project_folder, 'session.log')
        self.launcher_folder = os.path.join(self.project_folder, 'launcher')
        
        self.project_folder_check()
        
        if BphSession.sample_md5 == '':
            self.sid_folder = os.path.join(BPH_USER_DATA, BphSession.project_name, '', BphSession.sid)
        else:
            self.sid_folder = os.path.join(BPH_USER_DATA, BphSession.project_name, BphSession.sample_md5, BphSession.sid)
            
        BphSession.sample_folder = os.path.join(BPH_USER_DATA, BphSession.project_name, BphSession.sample_md5)
        
        BphSession.sid_folder = self.sid_folder

        # Create session directory if doesn't exist.
        Directory(self.sid_folder).check_and_create()
        
        #self.collect_session_files()
            
    def show_banner(self):
        logo = r"""
            ____  __    ___   ________ __ ____  __  _________   _______  __
           / __ )/ /   /   | / ____/ //_// __ \/ / / / ____/ | / /  _/ |/ /
          / __  / /   / /| |/ /   / ,<  / /_/ / /_/ / __/ /  |/ // / |   / 
         / /_/ / /___/ ___ / /___/ /| |/ ____/ __  / /___/ /|  // / /   |  
        /_____/_____/_/  |_\____/_/ |_/_/   /_/ /_/_____/_/ |_/___//_/|_|
                                                             -=[v.1.0.0]=-
                                                              
                    MALWARE ANALYSIS + AUTOMATION FRAMEWORK
                   
                Developed by Chris Navarrete @ FortiGuard Labs
              
                       Copyright (c) 2019 Fortinet, Inc.
                       
                     Contact: bph_framework@fortinet.com               
        """  
        print(colored(logo, 'green', attrs=['bold']))
            
    def project_folder_check(self):
        if os.path.isdir(self.project_folder):
            self.logger.log('Project folder already exists', level='DEBUG')
            
            if os.path.isfile(self.session_log_file):
                self.logger.log('Session log already exists', level='DEBUG')
                
                self.session_log(action='read')
                    
        else:
            self.logger.log('Generating sid...', level='DEBUG')
            BphSession.sid = self.generate_session_id()                  
        
        self.logger.log('Session ID: {}'.format(self.sid))
    
    @staticmethod       
    def get_session_id():
        return BphSession.sid
    
    def generate_session_id(self):
        return str(uuid.uuid4())        
    
    def session_log(self, action=None):
        
        if action == 'write':
            try:
                self.logger.log('Writing Session file...', level='DEBUG')
                log_file = open(self.session_log_file, 'w+')
                log_file.write(self.sid)
            except IOError:
                self.logger.log('Error when writing session log file', level='DEBUG')
            else:
                if os.path.isfile(self.session_log_file):
                    self.logger.log('Saved SessionID: {}'.format(self.sid), level='DEBUG')
                    self.logger.log(self.session_log_file, level='DEBUG')
            
        elif action == 'read':
            try:
                log_file = open(self.session_log_file, 'r')
                BphSession.sid = log_file.readline()
                log_file.close()
            except IOError:
                self.logger.log('Error when reading the log file.', level='DEBUG')
            else:
                self.logger.log('Stored SessionID: {}'.format(self.sid), level='DEBUG')
    
 
    def set_launcher(self, move_sample=True):
        try:
            if not os.path.isdir(self.launcher_folder):
                os.mkdir(self.launcher_folder)                
                
            sample_file_set = os.path.join(self.launcher_folder, os.path.split(self.tmp_sample_abs_path)[1])
    
            if not os.path.isfile(sample_file_set):
                if move_sample:
                    self.logger.log('MOVING SAMPLE', level='INFO')
                    shutil.move(self.tmp_sample_abs_path, self.launcher_folder)
                else:
                    self.logger.log('COPYING SAMPLE', level='INFO')
                    shutil.copy(self.tmp_sample_abs_path, self.launcher_folder)                
            
        except shutil.Error as e:
            self.logger.log('Error when copying the sample file: {}'.format(e), level='DEBUG')
            raise
        else:
            
            BphSession.launcher_abs_path = os.path.join(self.launcher_folder, os.path.basename(sample_file_set))
 
    def start(self):     
        self.logger.log('Starting session: {}'.format(self.project_name)) 
        if os.path.isdir(self.project_folder):
            self.logger.log('Session folder OK', level='DEBUG')
                        
            if os.path.isfile(self.session_log_file):
                self.logger.log('Session Log file OK', level='DEBUG')
                
                # Checking if file is empty
                with open(self.session_log_file, 'r') as lf:
                    if len(lf.readline()) == 0:
                        self.session_log(action='write')                
                    else:
                        self.session_log(action='read')
            else:
                self.logger.log('No session folder. Creating one...', level='DEBUG')
                self.session_log(action='write')
       
                
    def stop(self):
        self.logger.log('Stopping session: {}'.format(self.session_log_file))
        os.remove(self.session_log_file)
        
        
    def collect_session_files(self, tool_name=None):
        session_files = []
        for root, dirs, files in os.walk(self.sid_folder):
            if len(dirs) == 0 and len(files) != 0:
                for file in files:
                    file_abs_path = os.path.join(root, file)
                    
                    if tool_name is not None:
                        if tool_name in file:
                            print('Filtered: {}'.format(file_abs_path))
                            
                            if file not in session_files:
                                session_files.append(file_abs_path)
                    else:
                        print('Unfiltered: {}'.format(file_abs_path))

                        if file_abs_path not in session_files:
                            session_files.append(file_abs_path)
                            
        return session_files
