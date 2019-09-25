# Tool imports
from bph.tools.windows.floss import BphFloss as Floss

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

floss = Floss(LabFile(session.launcher_abs_path))
floss.search()
floss.execute()
floss.output()
