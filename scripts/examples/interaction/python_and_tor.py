# Tool Imports
from bph.tools.windows.nircmd import BphNirCmd as NirCmd

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.sample import BphSample as Sample
from bph.core.sample import BphLabFile as LabFile
from bph.core.session import BphSession as Session
from bph.core.vm import BphVmControl as VmControl

import time

session = Session(project_name='blackhat_arsenal_2019')
session.start()

vm = VmControl()
vm.set_vm('basic_static', network_id=1)
vm.start()

templateserver = TemplateServer()
templateserver.start()

time.sleep(10)

nircmd = NirCmd()
nircmd.configuration.reporting.report_files = True
nircmd.start_process(program=r'python -c "import urllib2 ; print(urllib2.urlopen(\"http://icanhazip.com\").read().strip())" > @report_folder@\\nircmd.log')
nircmd.execute(delay=5)
nircmd.output()

templateserver.stop()
vm.stop()

vm = VmControl()
vm.set_vm('basic_static', network_id=2)
vm.start()

templateserver = TemplateServer()
templateserver.start()

time.sleep(20)

nircmd = NirCmd()
nircmd.configuration.reporting.report_files = True
nircmd.start_process(program=r'python -c "import urllib2 ; print(urllib2.urlopen(\"http://icanhazip.com\").read().strip())" > @report_folder@\\nircmd.log')
nircmd.execute(delay=3)
nircmd.output()

templateserver.stop()
vm.stop()