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

import os

# Main Information
BPH_DIR = os.sep + os.path.join(*[ x for x in __file__.split('/')[:-3] if len(x) != 0 ])
BPH_PLUGIN_DIR = f"{BPH_DIR}/plugins"
BPH_INI_FILE = f"{BPH_DIR}/conf/blackphenix.conf"
BPH_USER_DATA = f"{BPH_DIR}/session"
BPH_TMP_DIR = "/tmp/"
    
# Core imports
from bph.core.configuration import BphWebControllerConfiguration
from bph.core.configuration import BphWindowsAgentConfiguration
from bph.core.configuration import BphVirtualBoxServerConfiguration
from bph.core.configuration import BphTemplateServerConfiguration

web_controller = BphWebControllerConfiguration()
windows_agent = BphWindowsAgentConfiguration()
vbox_config = BphVirtualBoxServerConfiguration()
template_server = BphTemplateServerConfiguration()

# Windows Agent Information
BPH_REMOTE_TOOLS_DRIVE = windows_agent.remote_tools_drive

# Web Controller Information
BPH_WEB_SERVER = f"http://{web_controller.web_controller_ip}:{web_controller.web_controller_port}"
BPH_WEB_FOLDER = web_controller.web_controller_path

# Template Server Information
BPH_TEMPLATE_SERVER_IP =  template_server.template_server_ip
BPH_TEMPLATE_SERVER_PORT = template_server.template_server_port
BPH_TEMPLATE_SERVER_BUFFER_SIZE = template_server.template_server_buffer_size
BPH_TEMPLATE_SERVER_OUTPUT = template_server.template_server_output

# Virtual Machine Information
BPH_VIRTUALBOX_SERVER_IP = vbox_config.virtualbox_server_ip 
BPH_VIRTUALBOX_SERVER_PORT = vbox_config.virtualbox_server_port 
