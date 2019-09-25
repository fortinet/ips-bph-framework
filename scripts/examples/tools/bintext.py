# Tool Imports
from bph.tools.windows.bintext import BphBinText as BinText

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

bintext = BinText(LabFile(session.launcher_abs_path))
bintext.default()
bintext.execute(delay=3)
bintext.output()
bintext.files()
