# Tool Imports
from bph.tools.windows.nircmd import BphNirCmd as NirCmd

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session

session = Session(project_name='blackhat_arsenal_2019')
session.start()

templateserver = TemplateServer()
templateserver.start()

nircmd = NirCmd()
nircmd.start_process(program=r'calc.exe')
nircmd.execute(delay=3)

nircmd = NirCmd()
nircmd.kill_process(program=r'calc.exe')
nircmd.execute(delay=3)
