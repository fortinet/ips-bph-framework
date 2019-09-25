# Tool Modules
from bph.tools.windows.dumppe import BphDumpPE as DumpPE

# Core Modules
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

dumppe = DumpPE(LabFile(session.launcher_abs_path))
dumppe.default()
dumppe.execute()
dumppe.output()
dumppe.files()

