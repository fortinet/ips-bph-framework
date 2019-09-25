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

import shutil
import os
import sys
import urllib.parse
import time
import logging
from termcolor import colored


LOGGING_LEVELS = { 'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40, 'CRITICAL': 50 }

class BphLogger:
    
    def __init__(self, level='INFO', module=None):
        self.module = module
        self.level = LOGGING_LEVELS[level]
        logging.basicConfig(level=self.level, format='%(asctime)s|%(levelname)s|%(message)s') 

    def log(self, data, level='INFO'):
        #print(level)
        data = "{}| {}".format(colored(self.module, 'cyan'), colored(data, 'magenta'))
        
        if level == "DEBUG":
            colored(logging.debug(data), 'red')
            
        elif level == "INFO":         
            colored(logging.info(data), 'blue')

        elif level == "WARNING":         
            colored(logging.warning(data), 'red')

        elif level == "ERROR":         
            colored(logging.error(data), 'red')

        elif level == "CRITICAL":         
            colored(logging.critical(data), 'red')
