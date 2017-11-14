Title: Compile on Mac Os X
Date: 2017-06-11 10:20
slug: compmacos
status: hidden
lang: en

## Pre-requirements
Since v1.7, rolisteam is based on Qt5.

You have to install XCode. It should install cpp compiler and many required components.

Then you must install from Qt Sdk file or source code. Make sure you are using the Qt5 (Qt4 will not work).

## Get Rolisteam Source code

Depending of what you want to compile.

### The latest stable version
You can get the source code of the latest stable version: [http://www.rolisteam.org/download| here]

### Dev version

Two ways:

'''-clone it from github''' 
  git clone --recursive git@github.com:Rolisteam/rolisteam.git

'''-if you can't use git'''
you may download both archive:
[https://github.com/Rolisteam/rolisteam/archive/master.zip| Rolisteam]
and
[https://github.com/Rolisteam/DiceParser/archive/master.zip| DiceParser]

### Extract source code
This step is needed while you get the source of latest stable version.
You must extract the code source.
 tar -xzvf rolisteam-1.7.1.tar.gz
or
 unzip rolisteam-1.7.1.zip


If you get the source code from git, this step is not needed.
Otherwise, you may get the source from the github page. 
So you need to do :

  unzip master.zip (from rolisteam)
  cd rolisteam/src
  unzip master.zip (from diceparser)
  mv DiceParser diceparser


### Compile the source

Open rolisteam.pro with qtcreator. It will compile rolisteam for you. Otherwise, these commands can be helpful:

 cd rolisteam
 lrelease rolisteam.pro 
 qmake -r rolisteam.pro
 make

(make sure to use qt5 qmake)


## start rolisteam
In terminal, just run:
 rolisteam

it may be possible to find rolisteam on graphical user menu, depending of your system.

Qt creator is able to start it.

## FAQ
### Having trouble with Qt4 and Qt5
If qt4 and qt5 are both installed on your computer, that may cause troubles.
While you compile Rolisteam v1.7.X (or higher), you must use qt5. 
So you may need to run
  lrelease-qt5 rolisteam.pro
  qmake-qt5 rolisteam.pro
  make

### How to make the installer


 1: copy/paste rolisteam.app into packaging/MacOs 
 2: run installZlib.sh
 3: appdmg  nodedmg.json rolisteam_v1.7.1-MacOsX_setup.dmg


install_name_tool -change "/usr/lib/libz.1.dylib" "@executable_path/../Frameworks/libz.framework/libz.1.dylib" rolisteam

appdmg  ../../rolisteam/packaging/MacOS/nodedmg.json rolisteam_v1.7.1-MacOsX_setup.dmg

