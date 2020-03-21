Title: Compile on Linux
Date: 2017-06-11 10:20
slug: linuxcomp
status: hidden
lang: en


# Get Source code

The way to get source code changes given your objectives.

## I want to compile stable version

To get the source, just [download the zip archive](http://www.rolisteam.org/download.html)
Appropriate when compiling for your own computer.

## I want to take part in **Rolisteam** development

The way allows you to change **Rolisteam** and to share your changes easily.
In this case, you will need to `clone` the rolisteam repository from git.
More details on this page: [Contribute]({filename}/31_contribute_coding.md).

# Pre-requirements

## Qt

### From Distribution

The first thing is to install **Qt** (v5.12 or higher). If your linux distribution is recent, you may install Qt from your distribution package system.

On debian/ubuntu system:
```
sudo apt-get install qt5-default qtbase5-dev-tools qt5-qmake libqt5network5 zlib1g-dev build-essential git qtmultimedia5-dev libqt5core5a libqt5gui5 qttools5-dev-tools qtdeclarative5-dev
qtwebengine5-dev
```

### Qt Installer

However, if the version is too old or if you need a recent Qt version, you should install Qt from Qt Installer.
Get Community version of Qt: [https://www.qt.io/download/](https://www.qt.io/download/)
At the Qt installation, please select Qt package compatible with your compiler.


## Zlib

The version from your distribution should be fine.

# Compilation

## Rolisteam

Let say Rolisteam source code is in:  `/home/user/documents/program/rolisteam`

  :::shell
  $ cd /home/user/documents/program/rolisteam
  $ mkdir build
  $ cd build
  $ qmake -r ../
  $ make -j4
  $ sudo make install

These lines will build **Rolisteam** and **Roliserver**.


## RCSE

It is basically the same thing.

  :::shell
  $ cd /home/user/documents/program/rcse
  $ mkdir build
  $ cd build
  $ qmake -r ../
  $ make -j4
  $ sudo make install


## Compiling Roliserver Only

* This will be useful if you plan on a setting up a dedicated **roliserver**.
* The following code is compatible with the latest versions of Debian and Raspian.
* We assume you've followed the docs on getting the source code past this point.


## Install dependencies

  It required less than the whole software.

  `sudo apt-get install qt5-qmake libqt5network5 libqt5core5a`


## Create a build directory

      :::shell
      $ mkdir server/build
      $ cd server/build

## Build
      :::shell
      $ qmake -r ../server.pro
      $ make
      $ sudo make install

For information on how to run the server checkout the [documentation]({filename}02_1_server.md)

# Compilation in Debug

Sometime, it is important to know what is happening into the program. You may want to compile in the debug mode.
The qmake command must be amend a bit to enable debugging.

`$ qmake -r ../server.pro CONFIG+=debug`

# [Advanced] Disable Features

Rolisteam has many features and some of them required dependencies or special tools.
In order to make rolisteam easier to compile, you can disable some features.
These 4 features can be switched off:

<pre>
############## FEATURES ######################
CONFIG += HAVE_SOUND
CONFIG += HAVE_WEBVIEW
CONFIG += HAVE_ZLIB
CONFIG += HAVE_PDF
############## END OF FEATURES ######################
</pre>

It makes **Rolisteam** easier to compile.
If you disabled **HAVE_WEBVIEW**, you must disable **HAVE_PDF** as well.

## HAVE_ZLIB

Rolisteam needs zlib to save its notes editor as *OpenDocument (.odt)*
In an extreme case, remove the need of *Zlib* .
Edit `rolisteam/client/client.pro` and comment out:

```
CONFIG += HAVE_ZLIB
```

## HAVE_SOUND

Rolisteam comes with audio players. These player required QtMultimedia module and its backend.

Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_SOUND
```

## HAVE_WEBVIEW

Rolisteam (since 1.9) embedded a web browser. This feature requires QtWebEngine which is a very heavy module (~80Mo).
Webview is also used for viewing pdf, in order to compile rolisteam without webview, you must also disable the PDF feature.
Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_WEBVIEW
CONFIG += HAVE_PDF
```

## HAVE_PDF

Rolisteam (since 1.9) can display PDF. If you don't want this feature:
Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_PDF
```

# FAQ

## Error on Translations in resources file.

**RCC: Error in 'rolisteam.qrc': Cannot find file 'translation/rolisteam_fr.qm'**  

`rolisteam.qrc` is rolisteam resource file. In order to be built, all resources must exist at the compilation.
Translation are generated from `.ts` files to `.qm` files.
Qt provides `lrelease` tool to convert `ts` to `qm`

Run this command, to generate all qm files.
> lrelease translation/rolisteam_*.ts

Then rebuild.

[More information](https://doc.qt.io/qt-5/qtlinguist-index.html)

## Some files are not found by the compiler

Perhaps, you forgot the --recursive parameter when getting the source code.

# I want to improve the project

Please discuss with us. We can share the effort to make new features and your work will fulfill **Rolisteam** needs and goals.  
Please take a look at our [roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=900739263)
