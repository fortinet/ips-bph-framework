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
import uuid
import socket               
import time

# Core imports
from bph.core.constants import *
from bph.core.configuration import BphVmConfiguration
from bph.core.logger import BphLogger as Logger

class BphVm:
    
    vm_config = BphVmConfiguration()

    def __init__(self):
        pass
    
class BphVmControl(BphVm):
    def __init__(self):
        self.logger = Logger(level='INFO', module=self.__module__)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        self.client_socket = client_socket
        self.vm_data = None
        self.connection_status = False    

    def __client_connector(self):
        try:
            self.client_socket.connect((BPH_VIRTUALBOX_SERVER_IP, BPH_VIRTUALBOX_SERVER_PORT))
        except socket.error:
                self.logger.log("Can't connect to VM manager. Attempting in 5 seconds")
                time.sleep(5)
                self.__client_connector()                
                
        else:
            self.logger.log('Connected...!')
            self.connection_status = True
            
    def send_data(self):
        if self.connection_status: 
            
            if self.vm_data is not None:
                
                self.logger.log('Sending: {}'.format(self.vm_data))
                self.client_socket.send(bytes(self.vm_data, 'ascii'))
            
                while True:
                    self.logger.log('Awaiting response from Agent...')
                    time.sleep(3)
                    data = self.client_socket.recv(128)
                    
                    if b"OK" in data:
                        self.logger.log('Data received from Agent => OK')
                        self.logger.log(data, level='DEBUG')
                        break
            
    
    def __update_cmd(self, action):
        self.logger.log('Updating cmd action to: {}'.format(action), level='DEBUG')

        self._vm_data['action'] = action
        self.vm_data = "|".join([self._vm_data['action'], 
                                    self._vm_data['vm_id'],
                                    self._vm_data['snapshot_id'], 
                                    self._vm_data['network_id']])
            
        self.logger.log('New VM Data: {}'.format(self.vm_data))
            
    def set_vm(self, exec_type, network_id=None):
        _exec_type = "".join(exec_type.split('_'))
        self.logger.log(f'[{exec_type}] VM Analysis was selected')

        data = {}
        
        for vm_data in BphVm.vm_config.VIRTUALMACHINES:
            if _exec_type in vm_data:
                if exec_type not in BphVm.vm_config.VIRTUALMACHINES[vm_data]:
                    _vm_data = BphVm.vm_config.VIRTUALMACHINES[vm_data]

                    if "machineid" in vm_data:
                        vm_id = _vm_data
                        self.logger.log(f"VmId: {vm_id}", level='INFO')
                        data['vm_id'] = vm_id

                    if "snapshotid" in vm_data:
                        snapshot_id = _vm_data
                        self.logger.log(f"SnapshotId: {snapshot_id}", level='INFO')
                        data['snapshot_id'] = snapshot_id

                    if "networkconnection" in vm_data:
                        net_id = _vm_data
                        self.logger.log(f"NetworkConnectionId: {net_id}", level='INFO')
                        
                        if network_id is not None:
                            data['network_id'] = str(network_id)
                        else:
                            data['network_id'] = net_id
                
        self._vm_data = data 
        self.logger.log('VM Data: {}'.format(self._vm_data))
        self.__client_connector()

    def start(self):
        self.logger.log('Starting VM')
        self.__update_cmd('start')
        self.send_data()

        if self.connection_status:
            self.logger.log('VM Started OK.')
            time.sleep(5)

              
    def stop(self):
        self.logger.log('Stopping VM')
        self.__update_cmd('stop')
        self.send_data()

        if not self.connection_status:
            self.logger.log('VM Shutdown OK')
            time.sleep(2)
            