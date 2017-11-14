Title: Compile on Linux
Date: 2017-06-11 10:20
slug: complinux
status: hidden
lang: en


{{En_old_version|Compilation_old|v1.6.1}}


## Pre-requirements
The first thing is to install Qt (v5.4 or higher).
You can get the community version of Qt: [https://www.qt.io/download/ https://www.qt.io/download/]

Rolisteam needs zlib for its notes editor. 
This page [http://blog.rolisteam.org/file/zlibapi.zip zlib] should do the job.


Rolisteam is managed through git. 
## Get the source code
There are two ways to get the source code. 
You can download the source code archive from stable release (go to [http://www.rolisteam.org/download http://www.rolisteam.org/download])

or you can clone the repository from github: please go to [https://github.com/Rolisteam/rolisteam https://github.com/Rolisteam/rolisteam]
  git clone --recursive git@github.com:Rolisteam/rolisteam.git

## Open Rolisteam
You can open the rolisteam.pro file with QtCreator and start compiling.

### Disable Music
You can compile rolisteam with or without the music player support.
You have to edit the rolisteam.pro file.

 #CONFIG += HAVE_SOUND
 CONFIG += HAVE_NULL



## FAQ

### I'm getting error like this: RCC: Error in 'rolisteam.qrc': Cannot find file 'translation/rolisteam_fr.qm'
rolisteam_fr.qm is a binary translation file. It's generated from rolisteam_fr.ts. 
Run this command: 
 lrelease translation/rolisteam_fr.ts
Then the compilation must be just fine.

### zlib compilation
zlib1g can be install on Windows, but there is an issue into zconf.h include:

 #if 1           /* HAVE_UNISTD_H -- this line is updated by ./configure */

replace this line by

 #if HAVE_UNISTD_H  /*-- this line is updated by ./configure */

