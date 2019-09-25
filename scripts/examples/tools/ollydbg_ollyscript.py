# Tool Imports
from bph.tools.windows.ollydbg import BphOllyDbg as OllyDbg

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

ollydbg = OllyDbg(LabFile(session.launcher_abs_path))
ollydbg.configuration.execution.background_run = True
ollydbg.ollyscript(ollyscript_file_name='msg.osc')
ollydbg.execute()