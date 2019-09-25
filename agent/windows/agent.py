import shutil
import socket
import subprocess
import threading
import json
import pickle
import tempfile
import time
import box
import threading
import os
import base64
import getpass
import urllib
import requests
import zipfile
import sys
import pprint
import platform

DEBUG = True

BPH_TEMPLATE_SERVER_IP = sys.argv[1]
BPH_TEMPLATE_SERVER_PORT = int(sys.argv[2])
BPH_CONTROLLER_WEB_PORT = int(sys.argv[3])

running_os = platform.release()

if running_os == "7":
    APP_DATA = "C:\\Users\\{current_user}\\AppData\\Roaming\\".format(
        current_user=getpass.getuser())
    TMP_FOLDER = "C:\\Users\\{current_user}\\AppData\\Local\\Temp\\".format(
        current_user=getpass.getuser())
    
elif running_os == "XP":
    # To avoid tool issues when dealing with white-spaced paths. 
    APP_DATA = "C:\\DOCUME~1\\{current_user}\\APPLIC~1\\".format(
        current_user=getpass.getuser())
    TMP_FOLDER = "C:\\DOCUME~1\\{current_user}\\LOCALS~1\\Temp\\".format(
        current_user=getpass.getuser())
else:
    print "Unsupported platform! Exiting..."
    sys.exit()

class FilterSpecialVars():
    def __init__(self, unfiltered_data, template=None, custom_user_vars=None):

        # unfiltered_data should be a list
        self.unfiltered_data = unfiltered_data
        self.filtered_data = []
        self.special_vars = {
            '@appdata@': APP_DATA,  # os.path.expandvars('%appdata%'),
            '@temp@': TMP_FOLDER,
            '@toolname@': template['tool_name'], # "peid"
            '@filename@': template.tool.filename, # "peid.exe"
            '@rid@': template['rid'],
            '@md5@': template['md5'],
            '@sample@': "\"" + ExecutionManager.sample_abs_path + "\"",
            '@sample_filename@': "\"" + os.path.basename(ExecutionManager.sample_abs_path) + "\"",
            '@tool_drive@': template['tool_drive'],
            '@tool_path@': os.path.join(template['tool_drive'], template['remote_tool_path'].replace('/','\\')),
            '@tool_abs_path@': os.path.join(template['tool_drive'], template['remote_tool_path'],
                                            template.tool.filename),
            '@report_folder@': os.path.join(APP_DATA, template['rid'], template['tool_name'])
        }
        
        if custom_user_vars != None:
            self.custom_user_vars_filter(custom_user_vars)

    def custom_user_vars_filter(self, custom_user_vars):
        if DEBUG: print "Custom User Vars Filtering: {}".format(custom_user_vars)
        for k, v in custom_user_vars.items():
            key = "@{}@".format(k)
            self.special_vars.update({key: v})
        if DEBUG: print self.special_vars

    def filter_now(self):
        def do_filter(unfiltered_string):
            for k, v in self.special_vars.items():
                if k in str(unfiltered_string):
                    unfiltered_string = unfiltered_string.replace(k, v)
                    if DEBUG: print ">> Found: {}".format(unfiltered_string)
            return unfiltered_string

        for unfiltered_string in self.unfiltered_data:
            if len(unfiltered_string) != 0:
                if DEBUG: print "### Searching Variable ###: {}".format(unfiltered_string)
                self.filtered_data.append(do_filter(unfiltered_string))

        if DEBUG: print self.special_vars

        if DEBUG:
            print"FILTERED: {}".format(self.filtered_data)
        # return " ".join(self.filtered_data)


class File(object):
    def __init__(self):
        pass

    def generate_random_file_name(self):
        import string
        import random
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(0, 10))

    def zip_file(self, file_abs_path, seconds=5):
        if not file_abs_path.endswith('.log') and not file_abs_path.endswith('.zip'):
            if DEBUG: print "Creating compressed (zip) archive: {}".format(file_abs_path)
            #time.sleep(5)

        try:
            zip_filename = "{}.zip".format(os.path.basename(file_abs_path))
            if DEBUG: print zip_filename
            original_filename = os.path.basename(file_abs_path)
            if DEBUG: print original_filename
            path_location = os.path.dirname(file_abs_path)
            if DEBUG: print path_location
            zip_file_abs_path = "{}\\{}".format(path_location, zip_filename)
            if DEBUG: print zip_file_abs_path
            zf = zipfile.ZipFile(zip_file_abs_path, 'w', zipfile.ZIP_DEFLATED)
            
            # When a file is bein created as compressed file (zip), in some cases
            # the set delay time is not enough and file-access errors appears.
            # To avoid such situation, several attempts are made until the access
            # to the source file is ready.  
            try:
                zf.write(file_abs_path, os.path.basename(file_abs_path))
            except IOError:
                if DEBUG: print "Target file is still in use... attempting in ({}) seconds".format(seconds)
                time.sleep(seconds)
                self.zip_file(file_abs_path)
                
            else:
                if DEBUG: print "Zip file creation - Done."
                
        except OSError as e:
            if DEBUG: print "Error when setting up info for target zip file: {}".format(e)
            raise
        else:

            zipfile.ZIP_DEFLATED
            if os.path.isfile(zip_file_abs_path):
                if DEBUG: print "Zip file ok: {}".format(zip_file_abs_path)

                # os.remove(file_abs_path)
                return zip_filename
            else:
                if DEBUG: print "Zip file can't be created"
                return None


class AutoItScript(File):

    def __init__(self, automation_data):
        self.autoit_script = None
        self.__base64totmp(automation_data)

    def __base64totmp(self, automation_data):
        if DEBUG: print "Converting from base64 file data to Auto-it Script"
        
        tmp_au_script_abs_path = os.path.join(
            APP_DATA, self.generate_random_file_name())
        with open(tmp_au_script_abs_path, 'w+') as tmp_au_script:
            for _ in automation_data:
                if DEBUG: print "Writing: {}\n".format(_)
                tmp_au_script.write(_)

        self.autoit_script = tmp_au_script_abs_path


class DownloadedFile(File):
    def __init__(self, download_url):
        self.download_dir = APP_DATA
        self.fake_file_name = self.generate_random_file_name()
        self.original_file_name = os.path.basename(download_url)
        self.extension = os.path.splitext(download_url)[1].replace('.', '')
        #self.abs_path = os.path.join(self.download_dir, "{}.{}".format(
        #    self.fake_file_name, self.extension))
        self.abs_path = os.path.join(self.download_dir, self.original_file_name)

        if DEBUG:
            print self.abs_path


class ExecutionManager(object):

    report_path = ""
    sample_abs_path = ""

    #### Agent Command Control ######
    def execute_tool(self, **cmd_data):

        if DEBUG:
            print cmd_data
            
        tool_drive = cmd_data['tool_drive']
        tool_path = cmd_data['tool_path'].replace('/', '\\')
        tool_name = cmd_data['tool_name']

        tool_abs_path = "\"{tool_drive}{tool_path}\\{tool_name}\"".format(
            tool_drive=tool_drive,
            tool_path=tool_path,
            tool_name=tool_name,
        )
        if DEBUG:
            print tool_abs_path
        tool_args = cmd_data['tool_args']
        if DEBUG:
            print tool_args
        cmd = "{} {}".format(tool_abs_path, tool_args)
        if DEBUG:
            print cmd
            
        print "\nExecuting Cmd: {}\n".format(cmd)
        subprocess.call(cmd, shell=True)
                
    def exec_manager(self, **cmd_data):

        if DEBUG:
            if DEBUG: print "\nExecuting Thread with data: {}\n".format(cmd_data)
            
        thread_name = cmd_data['tool_name']
        thread = threading.Thread(target=self.execute_tool, name=thread_name, kwargs=cmd_data)
        thread.start()
        
    def write_tmp_file(self, datatowrite, sample_abs_path):
        try:
            if DEBUG: print "Writing Tmp file: {}".format(sample_abs_path)
            with open(sample_abs_path, 'wb+') as f:
                f.write(datatowrite)
        except:
            if DEBUG: print "Error while creating the tmp file."
        else:
            if DEBUG: print "Done."
            if os.path.isfile(sample_abs_path):
                if DEBUG: print "Temp file created correctly."

                # Destination folder is created this way because because
                # some tools shows weird behaviors when passing arguments
                # For instance, CFF Explorer does not work correctly when
                # the file agument resides on a directory with whitespaces.
                # The workaround is to use DOS version of the path.
                #fixed_sample_abs_path = sample_abs_path.split('\\')
                #fixed_sample_abs_path[1] = "docume~1"
                #fixed_sample_abs_path[3] = "applic~1"
                # print fixed_sample_abs_path

                # Setting up Class attribute for sample path
                return sample_abs_path 
        return False

    def download_file(self, download_url):
        if DEBUG: print "Downloading: {}".format(download_url)

        try:
            import urllib2
            filedata = urllib2.urlopen(download_url)
        except urllib2.URLError:
            if DEBUG: print "Can't download the target sample file. Make sure BPH Webserver is running on the host."
            return False

        else:
            datatowrite = filedata.read()
            sample_abs_path = DownloadedFile(download_url).abs_path

            # Used when filtering custom variables
            ExecutionManager.sample_abs_path = sample_abs_path

            if DEBUG: print "Downloaded file: {}".format(sample_abs_path)
            return self.write_tmp_file(datatowrite, sample_abs_path)

    def execute_autoit_script(self, template, auto_it_script_abs_path):
       
        # The previously generated AutoIT script will be executed.
        if DEBUG: print "Executing Auto-It script"
        self.exec_manager(
            tool_drive=template.tool_drive,
            tool_path='misc\\autoitv3\\',
            tool_name='AutoIt3.exe',
            tool_args=auto_it_script_abs_path)

    def tool_execution(self, template):
        def selected_execution(filtered_parameters, filtered_automation):
            cascade_execution = False 

            if filtered_parameters is not None and filtered_automation is not None:
                if DEBUG: print "Cascaded Execution Detected: parameters -> autoit"
                cascade_execution = True
                
            if filtered_parameters is not None:
                if DEBUG: print "Parameter Execution Detected"
                
                self.exec_manager(
                    tool_drive=template.tool_drive,
                    tool_path=template.remote_tool_path,
                    tool_name=template.tool.filename,
                    tool_args=filtered_parameters
                )
                
            if filtered_automation is not None:
                # If cascase execution is set, then a delay between tool execution
                # and automation is also set. This to allow the tool to properly
                # load and the automation be able to run properly. A default value
                # of 5 seconds was given.
                if cascade_execution:
                    if DEBUG: print "Cascade Execution Delay - Running now..."
                    time.sleep(5)
                
                if DEBUG: print "Automation-Only Execution Detected"
                custom_user_vars = template.configuration.execution.custom_user_vars
                
                auto_it_script_abs_path = AutoItScript(filtered_automation).autoit_script
                self.execute_autoit_script(template, auto_it_script_abs_path)
                

        def filter_custom_vars(template, filter_type=None):
            # Handling template parameters custom vars
            
            if filter_type is not None:
                
                custom_user_vars = template.configuration.execution.custom_user_vars

                if filter_type == "parameters":
                    parameters = template.actions[template.actions.action]['parameters']

                    if parameters is not None:
                        if DEBUG: print "Parameters: {}".format(parameters)

                        if len(custom_user_vars) != 0: 
                            if DEBUG: print "Custom Parameters Vars {} - Parameters({})".format(custom_user_vars, parameters)
                            filtered_parameters = self.filter_variables(
                                parameters, template, filter_type='parameters', custom_user_vars=custom_user_vars)

                        else:
                            
                            filtered_parameters = self.filter_variables(
                                parameters, template, filter_type='parameters', custom_user_vars=None)
                            
                        return filtered_parameters
                    
                if filter_type == "automation":
                    automation = template.actions[template.actions.action]['automation']
                    
                    if automation is not None:
                        if DEBUG: print "Automation: {}".format(automation)
                        
                        if len(custom_user_vars) != 0:
                            if DEBUG: print "Custom Automation Vars {}".format(custom_user_vars)
                            
                            filtered_automation = self.filter_variables(
                            automation, template, filter_type='automation', custom_user_vars=custom_user_vars)

                        else:
                            filtered_automation = self.filter_variables(
                            automation, template, filter_type='automation', custom_user_vars=None)

                        return filtered_automation

                            
        action_name = template.actions.action
        if DEBUG: print "Executing: {}".format(action_name)
        
        filtered_parameters = filter_custom_vars(template, filter_type='parameters')
        filtered_automation = filter_custom_vars(template, filter_type='automation')

        selected_execution(filtered_parameters, filtered_automation)


class TemplateManager(ExecutionManager):

    def __init__(self, template):

        # self.report_directory_check(template.vm_report_name)

        if DEBUG: print "#"*50
        if DEBUG: print dict(template)
        if DEBUG: print "#"*50

        # Each tool request must save files. Those can be either a log file
        # or output files from its execution. This "report path" folder will
        # be created per request.
        #
        # The /files/ folder will be used to store any additional files generated
        # by the tool.
        self.report_path_files = os.path.join(
            APP_DATA, template.rid, template.tool_name, 'files')
        self.report_path = os.path.join(
            APP_DATA, template.rid, template.tool_name)

        if not os.path.isdir(self.report_path_files):
            if DEBUG: print "Creating: {}".format(self.report_path_files)
            os.makedirs(self.report_path_files)

        if template.configuration.execution['download_sample']:
            self.download_file(template.download_url)
            
        # Tool execution will eventually select which execution type will be run,
        # either automated or manual (only based in parameters)
        self.tool_execution(template)

        # Delay (seconds) between tool executions.
        exec_delay = template.configuration.execution.delay
        if DEBUG: print "Execution Delay (in seconds): {}".format(exec_delay)
        time.sleep(exec_delay)

        while True:
            if DEBUG: print threading.active_count()
            if DEBUG: print threading.enumerate()
        
            threads = str(threading.enumerate()).lower()

            if template.configuration.execution.background_run:
                if DEBUG: print "TOOL DOES RUN IN BACKGROUND..."
            
                if template.tool.filename.lower() in threads:
                    # FIXED: This allows more than one tool running in background
                    if threading.active_count() != 1:
                        if "autoit" not in threads:
                            if DEBUG: print "TOOL RUN CHECK DONE"
                            break
                           
            else:
                if DEBUG: print "TOOL DOES NOT RUN IN BACKGROUND..."
   
                if template.tool.filename.lower() not in threads:
                    if "autoit" not in threads:
                        if DEBUG: print "TOOL RUN CHECK - DONE"
                        break
            
            time.sleep(1)
    
        if DEBUG: print "\n###### Tool execution has ended #######\n"
        if DEBUG: print threading.active_count()
        if DEBUG: print threading.enumerate()
                
        
        if template.configuration.reporting.report_files:
            if DEBUG: print "########## Starting COLLECTING HTTP FILES ##############"
            self.report(template)

    def filter_variables(self, data, template, filter_type=None, custom_user_vars=None):
        if filter_type == "parameters":
            # Convert into list here.
            data = data.split(' ')

        if filter_type == "automation":
            # Decode first, then convert into a list.
            data = base64.decodestring(data).split('\n')

        if DEBUG: print "Filtering Variables: {}".format(data)
        unfiltered_data = FilterSpecialVars(data, template=template, custom_user_vars=custom_user_vars)
        unfiltered_data.filter_now()
        if DEBUG: print "Filtered Args: ({})".format(unfiltered_data.filtered_data)
        
        if filter_type == "parameters":
            return " ".join(unfiltered_data.filtered_data) 
        
        if filter_type == "automation":
            return unfiltered_data.filtered_data


    def report_back(self, report_data):
        url = "http://{}:{}/bph/report.php".format(BPH_TEMPLATE_SERVER_IP, BPH_CONTROLLER_WEB_PORT)

        files = {'file': open(report_data['file_abs_path'], 'rb')}
        response = requests.post(url, data={'project_name': report_data['project_name'],
                                            'md5': report_data['md5'],
                                            'sid': report_data['sid'],
                                            'tool': report_data['tool_name'],
                                            'rid': report_data['rid'],
                                            'file': report_data['file'],
                                            'dir': report_data['dir']}, files=files)
        if DEBUG: print "Response: {}".format(response.text)

    def report_files(self, base_folder, tool_name):
        if DEBUG: print "Searching files in: {} - tool: {}".format(base_folder, tool_name)
        
        while True:
            if len(os.listdir(base_folder)) != 0:
                if DEBUG: print "Files found.. Collecting them now..."
                files_found = []

                for root, dirs, files in os.walk(base_folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        if DEBUG: print "FullPath: {}".format(full_path)
                        file_name = os.path.basename(full_path)
                        if DEBUG: print "FileName: {}".format(file_name)
                        index = full_path.split('\\').index(tool_name)
                        if DEBUG: print "Index: {}".format(index)
                        path_found = "/".join([x for x in full_path.split('\\')[index+1:]])
                        if DEBUG: print "PathFound: {}".format(path_found)

                        if path_found.count('/') == 0:
                            
                            # Tool log file was found (e.g. bintext.log)
                            if DEBUG: print "Found log file: {}".format(path_found)
                            if path_found.endswith('.log'):
                                if DEBUG: print "FullPath: {}".format(full_path)
                                file_and_path_found = [full_path, path_found, '/']
                                files_found.append(file_and_path_found)
                        else:
                            # Any file inside of the /files/ folder.
                            if DEBUG: print "Found non-log file: {}".format(path_found)

                            # For non-log files, a file version of the file will be generated
                            # due problems of uploading big files through HTTP. This is a temporary fix.
                            zip_filename = File().zip_file(full_path)
                            file_and_path_found = zip_filename.split() + \
                                path_found.split('/')[:-1]
                            if DEBUG: print file_and_path_found
                            file_and_path_found.insert(
                                0, full_path.replace(file_name, zip_filename))

                            if file_and_path_found not in files_found:
                                if DEBUG: print "Appending file found: {}".format(file_and_path_found)
                                files_found.append(file_and_path_found)

                        if DEBUG: print "FullPathFound: {}".format(file_and_path_found)

                if DEBUG: print "Files Found: {}".format(files_found)
                return list(files_found)
            else:
                if DEBUG: print "Waiting for files to appear..."
                time.sleep(1)

    def report(self, template):
        def filter_dir(unfiltered_dir):
            if DEBUG: print "Unfiltered dir: {}".format(unfiltered_dir)

            dir_path = "/".join(unfiltered_dir)

            if dir_path.startswith('/'):
                return unfiltered_dir[0]
            return "/{}".format(dir_path)

        report_data = {}

        if os.path.isdir(self.report_path):
            if DEBUG: print "Sending back results to C&C server..."
            # Request variables. Generate data on the server.
            report_data['project_name'] = template.project_name
            report_data['md5'] = template.md5
            report_data['sid'] = template.sid
            report_data['rid'] = template.rid
            report_data['tool_name'] = template.tool_name

            for file_found in self.report_files(self.report_path,
                                                template.tool_name):
                # if DEBUG: print "FileFound: {}".format(file_found)
                report_data['file_abs_path'] = file_found[0]
                report_data['file'] = urllib.quote(file_found[1], safe='')
                report_data['dir'] = filter_dir(file_found[2:])
                if DEBUG: print report_data
                self.report_back(report_data)
            
            if DEBUG: print "Done."
        else:
            if DEBUG: print "Report Directory ({}) does not exist".format(self.report_path)

    def report_directory_check(self, vm_report_name):
        report_path = os.path.join(APP_DATA, vm_report_name)
        if DEBUG:
            print report_path

        if not os.path.isdir(report_path):
            os.mkdir(report_path)
            self.report_directory_check()
        else:
            REPORT_PATH = report_path


class Agent:
    RETRY_SECS = 1
    BUFFER_SIZE = 16384

    def __init__(self):
        self.connection_status = False

    #### Agent Control Functions ####

    def start(self):
        print "Starting Agent..."
        # Connect to Server
        self.connect()

    def stop(self):
        print "Stopping Agent..."
        self.disconnect()
        self.connection_status = False

    def restart(self):
        self.stop()
        self.start()

    #### Agent Connection Functions ####

    def check_connection(self):
        pass
        # print dir(self._clientsocket)

    def is_connected(self):
        if self.connection_status == True:
            return True
        return False

    def send(self, data):
        print "Sending Data: {}".format(data)
        try:
            self._clientsocket.send(data)
        except:
            self.reconnect()

    def listen(self):
        print "Connected to C&C Template Server. Waiting for instructions..."

        try:
            while True:
                # Keeps running receiving data. Once received
                # it its automatically un-serialized and converted
                # into an Python dictionary object.
                serialized_data = pickle.loads(self._clientsocket.recv(self.BUFFER_SIZE))
                template_data = box.Box(serialized_data)

                # TemplateManager decomposes serialized data
                # and take actions to execute the selected program
                TemplateManager(template_data)
                                
                print "Sending back to C&C => OK status"
                self.send('ok')

        except socket.error as e:
            print "Server disconnection: {}".format(e)
            self.reconnect()

        except EOFError as e:
            print "Server disconnection...".format(e)
            self.reconnect()

        else:
            # If template data was received correctly, then acknowledge.
            self.send('skip')

    def connect(self):
        # Make the connection to the server
        print "Connecting to C&C Template Server: {}:{}".format(BPH_TEMPLATE_SERVER_IP, BPH_TEMPLATE_SERVER_PORT)
        try:
            # Initialize Socket & connect back to server.
            self._clientsocket = socket.socket()
            self._clientsocket.connect((BPH_TEMPLATE_SERVER_IP, BPH_TEMPLATE_SERVER_PORT))
            self._clientsocket.setblocking(1)

        except socket.error:
            self.reconnect()

        except KeyboardInterrupt:
            print "Interrupting execution."
            sys.exit()

        else:
            print "Connection established. "
            self.connection_status = True
            self.listen()

    def disconnect(self):
        self._clientsocket.close()

    def reconnect(self):
        print "Reconnecting...."
        if DEBUG: print "Connection Error. Server down? Attempting connection in: ({}) seconds".format(self.RETRY_SECS)
        time.sleep(self.RETRY_SECS)
        if DEBUG: print "Attempting now..."
        self.connect()


if __name__ == "__main__":
    agent = Agent()
    
    try:
        agent.start()

        while True:
            # agent.check_connection()
            if not agent.is_connected():
                # If agent stops. Start it again.
                agent.start()
    except KeyboardInterrupt:
        print "Manual interruption. Bye!"
        sys.exit()
        
