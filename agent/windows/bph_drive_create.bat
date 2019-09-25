ECHO create vdisk file=%appdata%\test.vhd maximum=1000 > %appdata%\vhd.script
ECHO select vdisk file=%appdata%\test.vhd >> %appdata%\vhd.script
ECHO attach vdisk >> %appdata%\vhd.script
ECHO create partition primary >> %appdata%\vhd.script
ECHO format fs=ntfs label="install" quick >> %appdata%\vhd.script
ECHO assign letter=h >> %appdata%\vhd.script

diskpart /s %appdata%\vhd.script
