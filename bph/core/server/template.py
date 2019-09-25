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

import socket
import sys
import time
import pickle
import tempfile
import json
import box
import threading

# Core imports
from bph.core.logger import BphLogger as Logger
from bph.core.template import BphToolTemplateExecutor
from bph.core.configuration import BphTemplateServerConfiguration
from bph.core.constants import *


class BphTemplateServer(BphToolTemplateExecutor):

    BphToolTemplateExecutor.server_status = False
    BphToolTemplateExecutor.template_delivered = False
   
    def __init__(self):
        self.logger = Logger(level='INFO', module=self.__module__)
        self.thread_flag = False
        self._scan_bph_tmp_file(clean=True)
        
    def start(self):
        
        self.logger.log('Initializing BLACKPHENIX C&C Template Server...')
        
        try:
            serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        except socket.error as e:
            self.logger.log('Initialization Socket Error: {e}'.format(e.errno), level='DEBUG')
        else:

            self._socket_handle = serversocket
            self.logger.log('Socket Ready')
            self._socket_handle.bind((BPH_TEMPLATE_SERVER_IP, BPH_TEMPLATE_SERVER_PORT))
            self.logger.log('Starting server listener..')
            self._socket_handle.listen(0)
            self.logger.log('Accepting new connections now....')
            
            self.thread = threading.Thread(target=self.accept_connections, daemon=True)
            self.thread.start()          
              
    def __cleanup(self, template_file):
        if os.path.isfile(template_file):
            self.logger.log('Removing template file: {}'.format(template_file), level='DEBUG')
            try:
                os.remove(template_file)
            except OSError:
                self.logger.log('Error while deleting the file: {}'.format(template_file), level='DEBUG')
            else:
                self.logger.log('File deleted: {}'.format(template_file), level='DEBUG')

    def accept_connections(self):
        while True:

            try:
                # Accepting connections from Agent
                clientsocket, addr = self._socket_handle.accept()
                
                if clientsocket:
                    BphToolTemplateExecutor.server_status = True

                    self.logger.log(f"Agent connected: {addr}")
                        
                    # Continuous scan for temporary template files
                    while True:
                        self.logger.log('Agent Loop...', level='DEBUG')
                        time.sleep(1)
    
                        template_file = self._scan_bph_tmp_file()
                        self.logger.log('Template File: {}'.format(template_file), level='DEBUG')

                        if template_file is not None: 
                            if os.path.isfile(template_file):
                                self.logger.log('Template: {}'.format(template_file), level='DEBUG')
                                
                                self.send_template(template_file, clientsocket)
                                template_file = None               
                    
            except (BrokenPipeError):
                self.logger.log('Agent down? Running server once again...')
                BphToolTemplateExecutor.server_status = False
                self.accept_connections()
                
    def send_template(self, template_file, clientsocket):
        self.logger.log('Delivering Template', level='DEBUG')
        BphToolTemplateExecutor.template_delivered = False
        
        # If temp template is found, send it to agent
        if os.path.isfile(template_file) and os.path.getsize(template_file) != 0:
            self.logger.log('Sending template...')

            self.logger.log(template_file, level='DEBUG')

            # Temp file is a Boxed & Pickled data
            tmp_file = open(template_file, 'rb')
            dat = tmp_file.read()
        
            clientsocket.send(dat)
            tmp_file.close()
    
            self.logger.log('Waiting response from client...')
            if clientsocket.recv(128) == b"ok":
                self.logger.log('Template was delivered correctly')
                self.__cleanup(template_file)
                BphToolTemplateExecutor.template_delivered = True
                
            else:
                self.logger.log('Template was not delivered correctly.')
                time.sleep(5)
                
    def stop(self):
        self.logger.log('Stopping Template server...')
        self._socket_handle.close()

    def restart(self):
        self.logger.log('Restarting Template Server')
        self.stop()
        self.start()