# Tool imports
from bph.tools.windows.xorstrings import BphXorStrings as XorStrings

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

xorstrings = XorStrings(LabFile(session.launcher_abs_path))
xorstrings.search_xored()
xorstrings.execute()
xorstrings.output()
xorstrings.files()

