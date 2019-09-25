
  ********************************************************
  *                                                      *
  *                Ext_Detector.dll                      *
  *                                                      *
  *      Non executable detector for Exeinfo Pe          *
  *                                                      *
  *    ver.1.3.0 - required min. Exeinfo v0.0.3.1        *
  *                                                      *
  *               www.exeinfo.xn.pl                      *
  *                                                      *
  *               2013.11.18 by A.S.L                    *
  *                                                      *
  *                freeware version                      *
  *                                                      *
  ********************************************************



 Usage : Copy this file to ExeinfoPe directory or System directory files


 Detection list :


001. NOT EXE - .skf GUI skin file for developers - www.SkinCrafter.com
002. NOT EXE - .vpx Avast packed setup files www.avast.com
003. NOT EXE - .ICO Windows Vista icon PNG format - > ( new icon detector )
004. NOT EXE - .CRX - Google Chrome Extension
005. NOT EXE - .Tar - Tape ARchive ***
006. NOT EXE - .lz LZIP ( UNIX archive file - LZ77/78 like Lzma )
007. NOT EXE - .ppu  Free Pascal Unit file ( F.P.Compiler ) - www.freepascal.org
008. NOT EXE - .arj - ARJ compressed archive - www.arjsoftware.com    *ACM
009. NOT EXE - .wim - Windows Imaging Format ( no compression )
010. NOT EXE - .NUP - NOD32 Antivirus Update file - www.eset.com
011. NOT EXE - .LZH/LHA -  LHARC/LZARK compressed archive
012. NOT EXE - .CPIO -  CPIO ASCII archive / new portable / CRC format
013. NOT EXE - .IMG - Qemu qcow disk image [ Ver.01/02 ]
014. NOT EXE - .DSK - Generic PC disk image (FDD-HDD/NTFS crypt on/off info) - www.Qemu.com
015. NOT EXE - .VHD - Virtual Hard Disk image - ( Fixed size )  MS Virtual PC file format
016. NOT EXE - .VHD - Virtual Hard Disk image - ( Dynamically Expanding Size ) MS Virtual PC file format
017. NOT EXE - .yz1 archive - Deep Freezer compressed archive - by Yamazaki ZIPPER
018. NOT EXE - .jbc - Jetico BestCrypt encrypted drive ( *Virtual Disk ) - www.jetico.com
019. NOT EXE - .uif Universal Image Format [ MODE: *** Compr. ] MagicISO file ( without password* )
020. NOT EXE - .icns Apple Icons Mac OS X resource file www.apple.com
021. NOT EXE - .ROM ( ROFS Symbian FirmWare file )
022. NOT EXE - .asz Skin file for Delphi AlphaControls 2010 v7.67 www.alphaskins.com
023. NOT EXE - .pak ( founded in Game files level0x.pak  *Mumbo Jumbo )
024. NOT EXE - .aswcs Avast! antivirus skin
025. NOT EXE - .MTS - AVCHD video clips - MPEG Transport Stream
026. NOT EXE - .CPI - AVCHD Clip Information
027. NOT EXE - .MPL - AVCHD Video Playlist
028. NOT EXE - .DAA - PowerISO Direct-Access-Archive image [ Mode : Normal / password : Yes ] - www.poweriso.com
029. NOT EXE - .mp4/f4v HTTP Streaming Video f4f - ( part of movie - not playable ) [ I. MetaData first * ]
030. NOT EXE - .xar eXtensible ARchiver Archive  - http://code.google.com/p/xar - Mac OS X / Unix
031. NOT EXE - .IMG  * Disk Image / Partition - Generic Detector for UNIX / GPS / other systems
032. NOT EXE - .HFS  HFS+/HFSX (Hierarchical File System) volume - MAC Os / OS X (iPod) Volume
033. NOT EXE - .DER - DER encoded X509 Certificate ( ex. from exe file - if Digital Signed )
034. NOT EXE - .BH BlackHole compressed archive - www.ziptv.com
035. NOT EXE - .GCD/GMA - Garmin GPS generic file detector - www.garmin.com
036. NOT EXE - .??? / *Garmin GPS generic file detector ( .TRF / .JCV / .TYP ) - www.garmin.com
037. NOT EXE - .GCD - data file for : Software key wrapper 2.0. GiveawayOfTheDay.com
038. NOT EXE - .GEA Archive - from ovl Gentee Installers - www.createinstall.com
039. NOT EXE - .TDB - used by Mapsource & Basecamp - www.garmin.com
040. NOT EXE - .o MinGW/FPC object files ***
041. NOT EXE - .skn VCLSkin - www.link-rank.com ( not free Delphi VCL ! ) *** 90% detector
042. NOT EXE - .dcu - Delphi 2010 compiled Unit - Borland Delphi 2010 - www.borland.com - www.embarcadero.com
043. NOT EXE - .dcu - Delphi 2011 compiled Unit - Delphi XE - www.borland.com - www.embarcadero.com
044. NOT EXE - .obj 32bit - OMF Relocatable Object Module Format
045. NOT EXE - .obj 64bit - *** Relocatable Object Module Format *
046. NOT EXE - .ice - ICE compressed archive- www.iceows.com [ :-( Free Compressor - NO GUI ]
047. NOT EXE - .ice - Freeze! Compressed Archive (Reeve Soft) by Alan Reeve - obsolete 1991 ***
048. NOT EXE - .uha UHARC Archive last ver.0.6a Beta - FREE (c) 1997-2005 by Uwe Herklotz
049. NOT EXE - .apk ( AP32 header ) aPLib compression library  www.ibsensoftware.com
050. NOT EXE - .aplib / (.apk without header AP32 ) M8Z  - I detect only Exe file packed with aPlib compression 
051. NOT EXE - (.) Mac OS X Mach-O 64bit Intel executable
052. NOT EXE - .ddd - GLBasic 3D data - www.glbasic.com ( GCC )
053. NOT EXE - .dcu - Delphi v7 compiled Unit - Borland Delphi 7 - www.borland.com - www.embarcadero.com
054. NOT EXE - .dcu - Delphi 2009 compiled Unit - Borland Delphi 2009 - www.borland.com - www.embarcadero.com
055. NOT EXE - .dcu - Delphi 2011 XE2 compiled Unit - Borland Delphi 2011 - www.borland.com - www.embarcadero.com
056. NOT EXE - .DER - DER encoded X509 Certificate ( *for small bytes sign detector -  ex. from exe file - if Digital Signed )
057. NOT EXE - .ARC - FreeArc compressed archive
058. NOT EXE - .pkg -  Sun Solaris SVR4 package data stream  *UNIX Package
059. NOT EXE - .mkv/.mka - Matroska Video/Audio stream - www.matroska.org
060. NOT EXE - .dcu 32bit - Delphi 2012 XE3 compiled Unit - Borland Delphi 2012 - www.borland.com - www.embarcadero.com
061. NOT EXE - .dcu 64bit - Delphi 2012 XE3 compiled Unit - www.borland.com - www.embarcadero.com
062. NOT EXE - .dcu [ Mac OS X 32bit ] - Delphi 2012 XE3 compiled Unit - www.borland.com - www.embarcadero.com
063. NOT EXE - .AC3 Dolby Digital audio
064. NOT EXE - .dcu - Delphi v9 compiled Unit - Borland Delphi 2005 - www.borland.com - www.embarcadero.com
065. NOT EXE - .dcu - Delphi v6 compiled Unit - www.borland.com - www.embarcadero.com
066. NOT EXE - .JDBG - Embedded JCL debug info - www.delphi-jedi.org
067. NOT EXE - .dat Game files - ex. Mumbo Jumbo / 7 Wonders
068. NOT EXE - .PSD Adobe Photoshop image  - www.adobe.com
069. NOT EXE - .3DS - ( 3D Studio Mesh ) - 3D file format - Developed by Autodesk Inc.  Autodesk 3ds Max 3D modeling
070. NOT EXE - .skp  SketchUp 3D model
071. NOT EXE - .aqt - AQtime projects - SmartBear Software (2012) - profiler file - www.SmartBear.com
072. NOT EXE - .rsm / .dsm -  Remote debug symbols / Delphi Symbol Module file
073. NOT EXE - .GE - Gentee compiled source file - Freeware open source compiler - www.gentee.com
074. NOT EXE - .vct - Installer VISE Mindvision Wizard Module v3 - project file - www.mindvision.com
075. NOT EXE - .inx - InstallShield 2012 setup compiled script file  www.installshield.com - Flexera Software
076. NOT EXE - .kdc - Kaspersky Anti-Virus signature base - www.kaspersky.com
077. NOT EXE - .avz/.pva* - AVZ Antiviral Toolkit data - www.z-oleg.com/secur/avz  ( RUS )
078. NOT EXE - .xpt - XPCOM Type Library generated by the XPIDL compiler  (ver.info)
079. NOT EXE - HIV/DAT - Windows NT Registry on-disk storage format ( ver.info / type ) 
080. NOT EXE - .otf - OpenType CFF compact font format
081. NOT EXE - .bpi - Borland Package Import - www.borland.com
082. NOT EXE - .ib - InterBase Database by Borland/Embarcadero
083. NOT EXE - .prj6 - Visual Prolog 7 project file - TXT UTF-16 (LE) encoded
084. NOT EXE - .jxr/.wdp JPEG XR picture ( TIFF container ) - Better then jpg format
085. NOT EXE - (.WOFF) Web Open Font Format - http://www.w3.org/TR/WOFF
086. NOT EXE - .dds DirectX DirectDraw Surface
087. NOT EXE - .sdb - Windows Prepackaged Database
088. NOT EXE - .LIB Library file - OMF ( .obj files inside )
089. NOT EXE - .Lzma Archive ( LZMA:24 ) by Igor Pavlov
090. NOT EXE - .pdn Paint.NET picture format (v3)
090. NOT EXE - .pdn Paint.NET picture format (v3)
091. NOT EXE - .dar Disk Archive Denis Corbin - v2.4.10 2013.03.09 (Bzip2/GZ/store) - http://dar.linux.free.fr
092. NOT EXE - .b1 Archive ( free , nice GUI ) - www.b1.org    *ACM
093. NOT EXE - .sqx Archive - www.sqx-archiver.org
094. NOT EXE - .apl - APLIBTC - aPlib Archive - inside .apk ( AP32 header ) aPLib compression library  www.ibsensoftware.com
095. NOT EXE - .msg - Inno Setup Installer Messages file - www.innosetup.com
096. NOT EXE - .DAT - Inno Setup Uninstall Log - www.innosetup.com
097. NOT EXE - .GCA - [ passworded and not ] G Compression Archiver v.0.9k ! 2001 by Shin-ichi TSURUTA- www.emit.jp/gca
098. NOT EXE - .bza - BGA Archive ( Mode : BZA )
099. NOT EXE - .Gza - BGA Archive ( Mode : GZA )
100. NOT EXE - .PYO  Python optimized code - www.python.org ( .PYC generic bytecode )
101. NOT Win exe - (.) MenuetOS 32-bit x86 application - www.menuetos.net
102. NOT Win exe - (.) MenuetOS 64-bit x86 application - www.menuetos.net
103. NOT EXE - .vdd - Visual Basic 5-6 decompiler  data base - DotFix Software - www.vb-decompiler.org
104. NOT EXE - .isz - zipped packed .iso file 
105. NOT EXE - .DWG - AutoCAD drawing file v2.20 - 2014 - www.autodesk.com ( ver.detector )
106. NOT EXE - .csf  Secure CSF (Content Sealed Format) ***AutoCAD vector picture .DWG
107. NOT EXE - .DFM - text file - Delphi Compiler Form [ objects description - size/color/font ] - text format 
108  NOT EXE - .dcu - Delphi 2013 XE4 compiled Unit - Borland Delphi 2013 - www.embarcadero.com
109. NOT EXE - .FLP / .Fst -  FL Studio v11 - Audio and sound file type by Image Line Software - www.image-line.com 
110. NOT EXE - .IFX  IcoFX Software file ( icons / cursors )
111. NOT EXE - .dcu - Delphi 2013 XE5 * compiled Unit - Borland Delphi 2013 - www.embarcadero.com
112. NOT EXE - .cab - InstallShield compressed Archive - www.installshield.com - www.flexerasoftware.com
113. NOT EXE - .FRM VisualBasic Form ( ver.5.0 ) - www.microsoft.com
114. NOT EXE - obj Visual Basic *** - OR asm generic header
115. NOT EXE - .pak - Game data file ( XORed F7 byte ) -  /Alchemy/Yumster/...
116. NOT EXE - .pak  ( PAK V11 Game Data - not packed , ex. Puzkend / Dragon Portal / ... )
117. NOT EXE - .DAT - Futuremark Corporation 2011-2013 crypted data file  ( PCMark7 / 3DMark05 )
118. NOT EXE - .txt / .asc - text file with --- PGP KEY BLOCK ---  http://en.wikipedia.org/wiki/Pretty_Good_Privacy
119. NOT EXE - .SFS/SQUASHFS/SB* - SquashSF image file (little endian) - is a compressed file system for Linux.
120. NOT EXE - .img - RKFW - ROM Image  Flash Boot Data file ( for Android - Tablet devices )
121. NOT EXE -.hgr - KA3D is a scene graph based 3D-engine with a tool-chain for 3dsmax  (7 and newer) . *www.ka3d.com  / ***Rovio
122. NOT EXE - .pvr - Texture format - compatible with TexturePacker v3
123. NOT EXE - .ccz ( packed .pvr texture format with .Zlib ) 
124. NOT EXE -.PVR - PowerVR Texture format - www.imgtec.com
125. NOT EXE - .odex - Android system - optimized Dalvik executable file, like an .exe in Windows. 
126. NOT EXE -.e4a Mahmoud Elsisy Encrypted Archive Format v1.0 - Encrypt4all Home Edition v.5.4.1.299 - www.encrypt4all.com
127. NOT EXE - .lic - EXE Shield v5 -  License file - www.exeshield.com
128. NOT EXE - .xsh - project file for EXE Shield 5 - www.exeshield.com
129. NOT EXE - .pl - Perl script  - www.perl.org
130. NOT EXE - .rce - Encrypted file - Right-Click Encrypter - www.starfortsoftware.com





			***	( c ) - A.S.L    ***





