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
import shutil
import time

from bph.core.logger import BphLogger as Logger

class BphFileSystem:
    pass


class BphFile(BphFileSystem):
    pass


class BphDirectory(BphFileSystem):

    def __init__(self, directory):
        self.directory = directory
        self.logger = Logger(level='INFO', module=self.__module__)

    def check_and_create(self):
        self.logger.log(f"Verifying directory existence: {self.directory}", level='DEBUG')
        try:
            if os.path.isdir(self.directory):
                self.logger.log(f"Directory ({self.directory}) exists.", level='DEBUG')
                
            else:
                self.logger.log(f"Creating directory: {self.directory}", level='DEBUG')
                os.makedirs(self.directory, 0o777, exist_ok=True)
                
        except OSError:
            raise
