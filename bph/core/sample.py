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
import urllib.parse
import pefile

# Custom imports
from bph.core.constants import *


class BphSample:

    @staticmethod
    def md5hash(file):
        import hashlib
        return hashlib.md5(open(file, 'rb').read()).hexdigest()


class BphLabFile(BphSample):

    def __init__(self, sample_abs_path):
        super().__init__()
        
        sample = pefile.PE(sample_abs_path)
        self.__dict__.update(sample.__dict__)
        
        self.path = os.path.split(sample_abs_path)[0]
        self.file_name = os.path.split(sample_abs_path)[1]
        self.abs_path = sample_abs_path
        self.md5 = BphSample.md5hash(sample_abs_path)
        
        self.download_url = r"{}/{}/session/{}/{}".format(BPH_WEB_SERVER, BPH_WEB_FOLDER, "/".join(
            self.path.split('/')[5:]), urllib.parse.quote(self.file_name))
           
    
    def symbols(self, type=None):
            if type == "imports":
                imports = {}
            
                try:
                    for entry in self.DIRECTORY_ENTRY_IMPORT:                
                        #if entry not in imports:
                        dll_name = entry.dll.decode('utf-8')
                                            
                        for function in entry.imports:
                            function_name = function.name.decode('utf-8')
                            func_data = {'function': function_name, 
                                        'address': hex(function.address)}
                            
                            if dll_name not in imports:
                                imports[dll_name] = []
                                
                            imports[dll_name].append(func_data)
                except AttributeError: 
                    print("ERROR WHEN PARSING PE FILE")
                    return False
                                            
                else:
                    print("Imports: {}".format(imports))
                    return  imports
                            
            elif type == "exports":
                exports = []

                #print(self.__dict__)
                            
                for entry in self.IMAGE_DIRECTORY_ENTRY_EXPORT.symbols:        
                    if entry not in exports:
                        exports.append(entry.name.decode('utf-8'))
                        
                return exports
            
            else:
                print("Unknown symbol type")
