# Tool Imports
from bph.tools.windows.nircmd import BphNirCmd as NirCmd
from bph.tools.windows.procmon import BphProcMon as ProcMon

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

procmon = ProcMon()
procmon.capture()
procmon.execute(delay=10)         

sample_exec = NirCmd(LabFile(session.launcher_abs_path))
sample_exec.configuration.execution.background_run = False
sample_exec.start_process(program='@sample@')
sample_exec.execute()

procmon.terminate()
procmon.execute(delay=15)

procmon.export()
procmon.execute(delay=10)

procmon.files()