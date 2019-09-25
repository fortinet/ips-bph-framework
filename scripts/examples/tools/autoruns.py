# Tool Imports
from bph.tools.windows.autoruns import BphAutoruns as Autoruns

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()

templateserver = TemplateServer()
templateserver.start()

autoruns = Autoruns()
autoruns.analysis_basic()
autoruns.execute(delay=5)
autoruns.files()

