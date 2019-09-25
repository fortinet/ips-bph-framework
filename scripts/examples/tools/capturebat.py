# Tool Imports
from bph.tools.windows.capturebat import BphCaptureBat as CaptureBat

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.sample import BphSample as Sample
from bph.core.sample import BphLabFile as LabFile
from bph.core.session import BphSession as Session

session = Session(project_name='blackhat_arsenal_2019')
session.start()

templateserver = TemplateServer()
templateserver.start()

capturebat = CaptureBat()
capturebat.cleanup()
capturebat.execute()

capturebat.start()
capturebat.execute(delay=15)

capturebat.stop()
capturebat.execute()

capturebat.collect()
capturebat.execute()
capturebat.files()