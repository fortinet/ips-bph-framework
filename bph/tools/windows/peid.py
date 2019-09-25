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

from termcolor import colored

# Core imports
from bph.core.template import BphToolTemplateExecutor


class BphPeid(BphToolTemplateExecutor):
    def __init__(self, target_file=None, tool_name='peid', arch='x86', version='0.95'):
        super().__init__()
        self.load_tool_config_file(tool_name, arch, version, target_file=target_file)

    def normal_scan(self):
        self.logger.log(colored('EXECUTING NORMAL SCAN', 'yellow'))
        self.actions.action = "normal_scan"
       
    def deep_scan(self):
        self.logger.log(colored('EXECUTING DEEP SCAN', 'yellow'))
        self.actions.action = "deep_scan"

    def hardcore_scan(self):
        self.logger.log(colored('EXECUTING HARDCORE SCAN', 'yellow'))
        self.actions.action = "hardcore_scan"
   
    def kanal_scan(self):
        self.logger.log(colored('EXECUTING KANAL SCAN', 'yellow'))
        self.actions.action = "kanal_scan"
