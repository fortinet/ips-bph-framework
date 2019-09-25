import socket
import sys
import re
import subprocess
import time

BPH_NAME = "[BLACKPHENIX]"

def show_banner():
    banner = \
    """
         -=[B L A C K P H E N I X]=-
    by Chris Navarrete @ FortiGuard Labs
    
      [VirtualMachine Server Manager]

    """
    print(banner)
        
class VBoxManager:
    
    def __init__(self):
        self.vm_manager = "C:\\Progra~1\\Oracle\\VirtualBox\\VBoxManage.exe"
        
    def run(self, vm_data, check_output=False):

        try:        
            if check_output:
                print("{} | Checking Output".format(BPH_NAME))
                return subprocess.check_output(vm_data)
            else:
                print("{} | Not-Checking Output".format(BPH_NAME))
                subprocess.check_call(vm_data)
                            
        except subprocess.CalledProcessError:
            return False
        else:
            return True


class VBoxControl(VBoxManager):
    def __init__(self):
        super().__init__()
        self.nic_numbers = []
        self.vm_running = False 
    
    def __vm_cmd_output(self, cmd):
        try:
            output_data = self.run(cmd, check_output=True).decode('ascii').split('\n') 
            
            if "not find a registered machine" in output_data:
                print("{} | Wrong machine name".format(BPH_NAME))
            
        except AttributeError:
            print("{} | Error in the user input".format(BPH_NAME))
        else:
            return output_data

    def __nic_counter(self, vm_id):
        cmd = [self.vm_manager, "showvminfo", vm_id]

        for data in self.__vm_cmd_output(cmd):
            if re.match(r'NIC\s\d+:\s+MAC', data):
                
                nic_found = re.search(r'(\d+)', data).group()
                print("{} | >> NIC Found: {}".format(BPH_NAME, nic_found))
                
                if nic_found not in self.nic_numbers:
                    self.nic_numbers.append(nic_found)
    
        print(self.nic_numbers)
               
    def __is_vm_running(self, vm_id):
        print("{} | Searching for running VMs".format(BPH_NAME))
        status = None
        cmd = [self.vm_manager, "showvminfo", vm_id]
        
        for data in self.__vm_cmd_output(cmd):
            
            if "State: " in data:
                status = list([ status for status in data.split(' ') if len(status) != 0 ])[1]
                print("{} | Status Detected: {}".format(BPH_NAME, status))
                
            if status is not None:
                
                if status == "restoring":
                    print("{} | Restoring state detected. Waiting for a status change to avoid VM start-up problems...".format(BPH_NAME))
                    time.sleep(5)
                    self.__is_vm_running(vm_id)
                    
                # State: saved (since 2019-07-20T19:40:32.000000000)
                # State: restoring snapshot (since 2019-07-20T19:40:32.613000000)
                if status == "saved" or status == "running":
                    print("{} | VM-ID:({}) Found".format(BPH_NAME, vm_id))
                    self.vm_running = True
                    return True
                
        print("{} | VM-ID:({}) Not Found".format(BPH_NAME, vm_id))
        self.vm_running = False
        return False
            
    def set_network(self, vm_data):
        print("{} | Setting up Network connection for the VM".format(BPH_NAME))        
        # Here, the network connection selected by the user will be activated.
        if self.__is_vm_running(vm_data['vm_id']):      
            
            self.__nic_counter(vm_data['vm_id'])
            
            if len(self.nic_numbers) != 0:
                for nic_found in self.nic_numbers:
                    
                    # If nic is not the user's selected, then disable the rest.
                    if vm_data['network_id'] != nic_found:
                        cmd = [ self.vm_manager, "controlvm", vm_data['vm_id'], 
                            "setlinkstate{}".format(nic_found), "off" ]
                        print(cmd)
                        
                        if self.run(cmd):
                            print("{} | Deactivation of unused network interface was OK".format(BPH_NAME))
                        else:
                            print("{} | Error when deactivating unused network interfaces".format(BPH_NAME))

            # At this point all the network interfaces not-selected by the user
            # were turning off. Here the right one will be enabled.
            cmd = [ self.vm_manager, "controlvm", vm_data['vm_id'], 
                            "setlinkstate{}".format(vm_data['network_id']), "on" ]
            print(cmd)
            
            if self.run(cmd):
                print("{} | Network was set correctly".format(BPH_NAME))
            else:
                print("{} | Network was not set".format(BPH_NAME))
           
           
    def start(self, vm_data):
        print("{} | Starting VM".format(BPH_NAME))
        cmd = [self.vm_manager, "startvm", vm_data['vm_id'], "--type", "gui"]
        print(cmd)
        
        if self.__is_vm_running(vm_data['vm_id']):
            
            # If VM is running, stop and restore.
            self.stop(vm_data)
            
        # Then restore and run.
        self.restore(vm_data)
            
        if self.run(cmd):
            print("{} | VM started correctly".format(BPH_NAME))
            
            self.set_network(vm_data)
                        
            return True
        return False
                
    def stop(self, vm_data):
        print("{} | Stopping VM".format(BPH_NAME))
        cmd = [self.vm_manager, "controlvm", vm_data['vm_id'], "poweroff"]
        print(cmd)
        
        if self.__is_vm_running(vm_data['vm_id']):
            # If VM is running, stop it.            
            if self.run(cmd):
                print("{} | VM stopped correctly".format(BPH_NAME))
                return True
        return False
 	        
    def restore(self, vm_data):
        print("{} | Restoring VM".format(BPH_NAME))
        
        cmd = [self.vm_manager, "snapshot", vm_data['vm_id'], "restore", vm_data['snapshot_id']] 
        print(cmd)
        
        if self.__is_vm_running(vm_data['vm_id']):
            # If VM is running, stop and restore.
            self.stop(vm_data)
        
        if not self.vm_running:
            time.sleep(5)
            if self.run(cmd):
                print("{} | VM restoration OK".format(BPH_NAME))
                return True
        return False
                     
                                  
def main():
    show_banner()
    print("{} | Starting VM Control server...".format(BPH_NAME))
    s = socket.socket()         
    host = sys.argv[1]
    port = int(sys.argv[2])
    s.bind((host, port))        
    s.listen(1) 
    
    vbox = VBoxControl()
    
    while True:
        
        print("{} | Accepting connections".format(BPH_NAME))
        
        try:
            client_socket, addr = s.accept()
        except KeyboardInterrupt:
            sys.exit() 
        else:
            print('Receiving connection from:', addr)

            while True:
                print("{} | Waiting for data...".format(BPH_NAME))
                data = client_socket.recv(512).decode('ascii')
        
                if data:
                    
                    if re.match(r'restart|restore|start|stop', data):
                        print("{} | VM Command received: {}".format(BPH_NAME, data))
                    
                        data = data.strip().split('|')    
                        vm_data = {}
                        
                        if len(data) == 4:
                            print("{} | OK".format(BPH_NAME))
                            vm_data = {}
                            vm_data['cmd'] = data[0]
                            vm_data['vm_id'] = data[1]
                            vm_data['snapshot_id'] = data[2]
                            vm_data['network_id'] = data[3]
                            print(vm_data)

                            if vm_data['cmd'] == "start":
                                if vbox.start(vm_data):
                                    client_socket.send(b'OK\n')
                                else:
                                    client_socket.send(b'ERROR\n')
                        
                            elif vm_data['cmd'] == "stop":
                                if vbox.stop(vm_data):
                                    client_socket.send(b'OK\n')
                                else:
                                    client_socket.send(b'ERROR\n')
                                                        
                    else:
                        print("{} | Unknown command: {}".format(BPH_NAME, data))
                    
                else:
                    break
                                

if __name__ == '__main__':
    main()