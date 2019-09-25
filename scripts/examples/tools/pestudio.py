# Tool Imports
from bph.tools.windows.pestudio import BphPeStudio as PeStudio

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

pestudio = PeStudio(LabFile(session.launcher_abs_path))
pestudio.default()
pestudio.execute()
pestudio.files()
