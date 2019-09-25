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
nircmd.configuration.reporting.report_files = True
nircmd.start_process(program='ping 4.2.2.2 > @report_folder@\\nircmd.log')
nircmd.execute(delay=5)
nircmd.output()
nircmd.files()