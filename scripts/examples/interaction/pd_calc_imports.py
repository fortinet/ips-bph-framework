# Tool Imports
from bph.tools.windows.pd import BphPd as Pd
from bph.tools.windows.nircmd import BphNirCmd as NirCmd

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.sample import BphSample as Sample
from bph.core.sample import BphLabFile as LabFile
from bph.core.session import BphSession as Session

session = Session(project_name='blackhat_arsenal_2019')
session.start()

templateserver = TemplateServer()
templateserver.start()

nircmd = NirCmd()
nircmd.start_process(program=r'calc.exe')
nircmd.execute(delay=3)

pd = Pd()
pd.dump_process(process_name='calc.exe')
pd.execute(delay=5)

files_found = pd.files()
    
for file_found in files_found:
    if file_found.endswith('.exe'):

        dumped_file = LabFile(file_found)
        
        for symbol, function_data in dumped_file.symbols(type='imports').items():
            print(symbol)

            for data in function_data:
                print(data) 

