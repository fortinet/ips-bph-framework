# Tool imports
from bph.tools.windows.peid import BphPeid as Peid

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

sample_file = LabFile(session.launcher_abs_path)

peid = Peid(sample_file)
peid.kanal_scan()
peid.execute()
peid.output()
peid.files()
