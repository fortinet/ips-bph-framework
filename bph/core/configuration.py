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

import os.path
import configparser
import time
import ast

from bph.core.constants import *
from bph.core.logger import BphLogger as Logger

class BphConfiguration:
        
    def __init__(self):
        self.logger = Logger(level='INFO', module=self.__module__)
        self.load_config()
    
    def load_config(self):
        try:
            
            self.logger.log('Initializing Configurator...', level='DEBUG')
            config_file = configparser.ConfigParser()
            
            if os.path.isfile(BPH_INI_FILE):
                config_file.read(BPH_INI_FILE)
    
        except configparser.Error as e:
            self.logger.log('Error when parsing the config file: {}'.format(e), level='DEBUG')
            
        else:
            for section in config_file.sections():
                setattr(BphConfiguration, section, config_file[section])


class BphVmConfiguration(BphConfiguration):
    def __init__(self):
        super().__init__()
        self.basic_static_analysis_vm_id = BphConfiguration.VIRTUALMACHINES['BasicStaticAnalysisMachineId']
        self.basic_static_analysis_snapshot_id = BphConfiguration.VIRTUALMACHINES['BasicStaticAnalysisSnapshotId']
        self.basic_static_analysis_network_connection = BphConfiguration.VIRTUALMACHINES['BasicStaticAnalysisNetworkConnection']
        
        self.basic_dynamic_analysis_vm_id = BphConfiguration.VIRTUALMACHINES['BasicDynamicAnalysisMachineId']
        self.basic_dynamic_analysis_snapshot_id = BphConfiguration.VIRTUALMACHINES['BasicDynamicAnalysisSnapshotId']
        self.basic_dynamic_analysis_network_connection = BphConfiguration.VIRTUALMACHINES['BasicDynamicAnalysisNetworkConnection']
        
        self.advanced_static_analysis_vm_id = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisMachineId']
        self.advanced_static_analysis_snapshot_id = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisSnapshotId']
        self.advanced_static_analysis_network_connection = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisNetworkConnection']

        self.advanced_dynamic_analysis_vm_id = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisMachineId']
        self.advanced_dynamic_analysis_snapshot_id = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisSnapshotId']
        self.advanced_dynamic_analysis_network_connection = BphConfiguration.VIRTUALMACHINES['AdvancedStaticAnalysisNetworkConnection']


class BphTemplateServerConfiguration(BphConfiguration):
    def __init__(self):
        super().__init__()
        self.template_server_ip = BphConfiguration.TEMPLATE_SERVER['TemplateServerIp']
        self.template_server_port = int(BphConfiguration.TEMPLATE_SERVER['TemplateServerPort'])
        self.template_server_buffer_size = int(BphConfiguration.TEMPLATE_SERVER['TemplateServerBufferSize'])
        self.template_server_output = ast.literal_eval(BphConfiguration.TEMPLATE_SERVER['TemplateServerOutput'])

        
class BphVirtualBoxServerConfiguration(BphConfiguration):
    def __init__(self):
        super().__init__()
        self.virtualbox_server_ip = BphConfiguration.VIRTUALBOX_SERVER['VirtualBoxServerIp']
        self.virtualbox_server_port = int(BphConfiguration.VIRTUALBOX_SERVER['VirtualBoxServerPort'])
        

class BphWindowsAgentConfiguration(BphConfiguration):
    def __init__(self):
        super().__init__()
        self.remote_tools_drive = BphConfiguration.WINDOWS_AGENT['RemoteToolsDrive']


class BphWebControllerConfiguration(BphConfiguration):
    def __init__(self):
        super().__init__()
        self.web_controller_ip = BphConfiguration.WEB_CONTROLLER['WebControllerIp']
        self.web_controller_port = BphConfiguration.WEB_CONTROLLER['WebControllerPort']
        self.web_controller_path = BphConfiguration.WEB_CONTROLLER['WebControllerPath']
                   
        