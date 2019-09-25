# Tool Modules
from bph.tools.windows.regshot import BphRegShot as RegShot

# Core Modules
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='pony8')
session.start()

templateserver = TemplateServer()
templateserver.start()

regshot = RegShot()
regshot.first_shot()
regshot.execute()

regshot.second_shot()
regshot.execute()

regshot.compare()
regshot.execute()
regshot.files()

print("Done")