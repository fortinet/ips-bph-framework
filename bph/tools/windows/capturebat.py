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

class BphCaptureBat(BphToolTemplateExecutor):

    def __init__(self, target_file=None, tool_name='capturebat', arch='x86', version='2.0.0-5574'):
        super().__init__()
        self.load_tool_config_file(tool_name, arch, version, target_file=target_file)

    def cleanup(self):
        self.logger.log(colored('CLEANING UP PREVIOUS ACTIVITY', 'yellow'))
        self.configuration.reporting.report_files = False
        self.configuration.execution.background_run = False
        self.actions.action = "cleanup"

    def start(self):
        self.logger.log(colored('CAPTURING ACTIVITY', 'yellow'))
        self.configuration.reporting.report_files = False
        self.configuration.execution.background_run = True
        self.actions.action = "start"

    def stop(self):
        self.logger.log(colored('STOP CAPTURE', 'yellow'))
        self.configuration.reporting.report_files = False
        self.configuration.execution.background_run = False
        self.actions.action = "stop"

    def collect(self):
        self.logger.log(colored('COLLECTING DATA AND FILES', 'yellow'))
        self.configuration.reporting.report_files = True
        self.configuration.execution.background_run = False
        self.actions.action = "collect"


 

