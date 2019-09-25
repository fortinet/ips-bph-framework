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

import time
import os
import sys
import csv

# Custom imports
from bph.core.session import BphSession
from bph.core.constants import *
      
class BphNetworkAnalysis:
    def __init__(self):
        pass
    
class BphNetworkAnalysisCsvReader(BphNetworkAnalysis):
    def __init__(self, tool_name=None, csv_file=None):
        super().__init__()
        self.tool_name = tool_name
        self.csv_file = csv_file

    def fetch(self, data_type=None):
        with open(self.csv_file) as csv_file_h:
            csv_reader = csv.reader(csv_file_h, delimiter=',')

            domains = []
    
            for row in csv_reader:
                
                if self.tool_name == "networktrafficview":
                    if "Destination" not in str(row):
                        if "[" in str(row[3]):
                            domain = row[3].split(' ')[0] 
                            if domain not in domains:
                                domains.append(domain)
                    
    
            print(domains)     
            return domains               

