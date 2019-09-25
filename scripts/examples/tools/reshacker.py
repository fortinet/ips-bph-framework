# Tool Imports
from bph.tools.windows.resourcehacker import BphResourceHacker as ResourceHacker

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

reshacker = ResourceHacker(LabFile(session.launcher_abs_path))
reshacker.extract_resources()
reshacker.execute()
reshacker.files()

