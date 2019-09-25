# Tool imports
from bph.tools.windows.networktrafficview import BphNetworkTrafficView as NetworkTrafficView
from bph.tools.windows.nircmd import BphNirCmd as NirCmd

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

# Analysis Imports
from bph.analysis.network import BphNetworkAnalysisCsvReader as NetworkAnalysisCsvReader

import time

session = Session(project_name='blackhat_arsenal_2019')
session.start()

templateserver = TemplateServer()
templateserver.start()

ntv = NetworkTrafficView()
ntv.start()
ntv.execute()

nircmd = NirCmd()
nircmd.configuration.reporting.report_files = True
nircmd.start_process(program=r'python -c "import urllib2 ; print(urllib2.urlopen(\"https://icanhazip.com\").read().strip())" > @report_folder@\\nircmd.log')
nircmd.execute(delay=5)

ntv.stop()
ntv.execute()

for csv_file in ntv.files():
    ntv = NetworkAnalysisCsvReader(tool_name='networktrafficview', csv_file=csv_file)
    ntv.fetch(data_type='domains')

