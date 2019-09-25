# Tool imports
from bph.tools.windows.exeinfope import BphExeInfoPe as ExeInfoPe
from bph.tools.windows.upx import BphUpx as Upx

# Core Imports
from bph.core.server.template import BphTemplateServer as TemplateServer
from bph.core.session import BphSession as Session
from bph.core.sample import BphLabFile as LabFile

import re

session = Session(project_name='blackhat_arsenal_2019')
session.start()
session.set_launcher(move_sample=False)

templateserver = TemplateServer()
templateserver.start()

sample_file = LabFile(session.launcher_abs_path)

exeinfope = ExeInfoPe(sample_file)
exeinfope.default()
exeinfope.execute()

sig_match = re.search(r'(upx.*3.91.*)', "".join(exeinfope.output()), re.I)

if sig_match:
    print("SAMPLE IS UPX PACKED => VERSION 3.91. DECOMPRESSING...")

    for symbol, function_data in sample_file.symbols(type='imports').items():
        print(symbol)
        
        for data in function_data:
            print(data) 

    upx = Upx(sample_file)
    upx.decompress()
    upx.execute()
    
    unpack_result = upx.output()
    
    if "Unpacked 1 file." in unpack_result:
        print("SAMPLE WAS SUCCESSFULLY UNPACKED...!!!11")
     
        files_found = upx.files()
        
        for file_found in files_found:
            if "unpacked.exe" in file_found:
                
                unpacked_file = LabFile(file_found)
                exeinfope = ExeInfoPe(unpacked_file)
                exeinfope.default()
                exeinfope.execute()
                exeinfope.output()
                
                for symbol, function_data in unpacked_file.symbols(type='imports').items():
                    print(symbol)
                    
                    for data in function_data:
                        print(data)             