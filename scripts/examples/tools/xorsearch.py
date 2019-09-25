# Tool imports
from bph.tools.windows.xorsearch import BphXorSearch as XorSearch

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

xorsearch = XorSearch(LabFile(session.launcher_abs_path))
xorsearch.search_www()
xorsearch.execute()
xorsearch.output()
xorsearch.files()
