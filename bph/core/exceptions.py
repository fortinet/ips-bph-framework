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

import sys

## BlackPhenix Exception Base Class ##

class BphException(Exception):
    def __init__(self):
        pass


## BlackPhenix Session Exceptions ##

class BphSessionException(BphException):
    pass


class BphSessionNameException(BphSessionException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return(str(f"{self.__class__.__name__}: {self.data}"))


## BlackPhenix FileSystem Exceptions ##

class BphFileSystemException(BphException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return(str(f"{self.__class__.__name__}: {self.data}"))

class BphDirectoryNotFound(BphFileSystemException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return(str(f"{self.__class__.__name__}: {self.data}"))

## BlackPhenix VirtualMachine Exceptions ##

class BphVirtualMachineException(BphException):
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
        return(str(f"{self.__class__.__name__}: {self.data}"))

class BphVirtualMachineSnapshotException(BphVirtualMachineException):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return(str(f"{self.__class__.__name__}: {self.data}"))