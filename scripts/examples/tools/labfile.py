
# Core Imports
from bph.core.sample import BphLabFile as LabFile

sample = LabFile('/home/bph/bph-framework/session/blackhat_arsenal_2019/launcher/bph_upx.exe')

print(f"""
  Sample Data:
    
    Absolute Path:\t {sample.abs_path}

    Base Path:\t {sample.path}

    File Name:\t {sample.file_name}

    md5 Hash:\t {sample.md5}

    Imported Symbols:\t {sample.symbols(type='imports').keys()}

    Imported Functions w/symbols:\t {sample.symbols(type='imports').items()}
""")
