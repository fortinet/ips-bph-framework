# Tool Imports
from bph.tools.windows.depends import BphDepends as Depends

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

depends = Depends(LabFile(session.launcher_abs_path))
depends.default()
depends.execute(delay=5)
depends.files()
