Title: Compile on Linux
Date: 2017-06-11 10:20
slug: linuxcomp
status: hidden
lang: en


# Before working on Rolisteam

Please discuss with us. We can share the effort to make new features and your work will fulfill **Rolisteam** needs and goals.
Please take a look at our [roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=900739263)

# Get Source code

The way to get source code changes given your objectives.

## I want to compile stable version

To get the source, just [download the zip archive](http://www.rolisteam.org/download.html)

Appropriate when compiling for your own computer.

## I want to take part in **Rolisteam** development

The way allows you to change **Rolisteam** and to share your changes easily.

### Git

**Rolisteam** manages its source code with **Git**.
So, first learn how to use it and install it.
[Git](https://git-scm.com/)
[Learn Git](https://try.github.io/levels/1/challenges/1)

The rest of the documentation git commands are given as command line but there are many GUI application to manage git repository.

### Github

Github is a platform which stores rolisteam's git repository.

Those following steps are not mandatory but it definitely speeds up integration.
To explain it a bit, those steps create a copy of **Rolisteam** and its dependencies into your github account.
Then, it allows you to do whatever you want.
To share your work, just make a *pull request* (github is a good friend for that).

* Create your [github account](https://github.com)
* Go to [Rolisteam organisation page](https://github.com/Rolisteam)
* Fork ![rolisteam]({static}/images/pictos/fork.png) the wanted project and its dependencies.
    * **Rolisteam** project is the source code of **Rolisteam** and **Roliserver**. It needs **DiceParser**, **RCharacterSheet**, **RPlugins** and **common**
    * **RCSE** project is the charactersheet editor. Its needs **RCharacterSheet**.
    * **Dice** brings together all tools to roll dice.
* Then those git repositories should appear in your github account: https://github.com/Your\_Login
* For **Rolisteam** and **rcse**, it is better to change the file `.gitmodules` before clone the repository:  
<pre>
[submodule "client/diceparser"]
    path = client/diceparser
    url = https://github.com/Rolisteam/DiceParser.git
    pushURL = git@github.com:Rolisteam/DiceParser.git
[submodule "client/widgets/gmtoolbox"]
    path = client/widgets/gmtoolbox
    url = https://github.com/Rolisteam/RPlugins.git
    pushURL = git@github.com:Rolisteam/RPlugins.git
[submodule "client/charactersheet"]
    path = client/charactersheet
    url = https://github.com/Rolisteam/RCharacterSheet.git
    pushURL = git@github.com:Rolisteam/RCharacterSheet.git
[submodule "client/common"]
    path = client/common
    url = https://github.com/Rolisteam/common.git
    pushURL = git@github.com:Rolisteam/common.git
</pre>

Change every **Rolisteam** by **your github username**.  
This file describes where git should retrieve dependencies (submodules). We make sure it retrieves them from your github account.
Make this only if you plan to work on dependencies too.

* For **Rcse** makes the same operation. The `.gitmodules` file is shorter than **Rolisteam** one.
* Install git on windows or [github desktop](https://desktop.github.com/)
* Clone **rolisteam**:
    > git clone --recursive git@github.com:Your_login/rolisteam.git

Congrats, the **Rolisteam** source code is on your computer.

## I have a github account but I don't want to fork so many repositories

Then, just clone the project from the main repository
    > git clone --recursive https://github.com/Rolisteam/rolisteam.git

The source code comes on your computer.
You won't be able to integrate your work in **Rolisteam**, until we give you permission to do so.
To do it, we have to accept you in **Rolisteam** organization. [Give us]({filename}26_contactUs.md) your github username.

Of course, you can send us patch. But it's less pratical this way.

## I don't want to create github account

Then, just clone the project from the main repository
    > git clone --recursive https://github.com/Rolisteam/rolisteam.git


# Pre-requirements

## Installation

The first thing is to install **Qt** (v5.10 or higher).  
Get Community version of Qt: [https://www.qt.io/download/](https://www.qt.io/download/)

At the Qt installation, please select Qt package compatible with your compiler. If you don't have any. Select mingw version.
**Qt** will install mingw on your computer.

On windows, please use visual studio 2015 to compile.
As it is painful to install it, **Rolisteam** may still be compiled with other compiler but some features will not be working.

On debian/ubuntu system:
```
sudo apt-get install qt5-default qtbase5-dev-tools qt5-qmake libqt5network5 zlib1g-dev build-essential git qtmultimedia5-dev libqt5core5a libqt5gui5 qttools5-dev-tools qtdeclarative5-dev
qtwebengine5-dev
```


# Disable Features

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

## Zlib

Rolisteam needs zlib to save its notes editor as *OpenDocument (.odt)*
In an extreme case, remove the need of *Zlib* .
Edit `rolisteam/client/client.pro` and comment out:

```
CONFIG += HAVE_ZLIB
```

## Webengine

**Webengine** is a Qt component. It is dedicated to display web page. **Rolisteam** may uses it inside some charactersheets.
Qt on windows provides it only in the visual studio 2015.


In an extreme case, remove the need of *webengine* .
Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_WEBVIEW
```

## Sound

Rolisteam comes with audio players. These player required QtMultimedia module and its backend.

Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_SOUND
```

## Webview

Rolisteam (since 1.9) embedded a web browser. This feature requires QtWebEngine which is a very heavy module (~80Mo).
Webview is also used for viewing pdf, in order to compile rolisteam without webview, you must also disable the PDF feature.
Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_WEBVIEW
CONFIG += HAVE_PDF
```

## PDF

Rolisteam (since 1.9) can display PDF. If you don't want this feature:
Edit `rolisteam/client/client.pro` and comment out:
```
CONFIG += HAVE_PDF
```

# Compiling Roliserver Only

* This will be usefull if you plan on a seting up a dedicated roliserver.
* The following code is compatible with the latest versions of Debian and Raspian.
* We assume you've followed the docs on getting the source code past this point.


## Install dependencies

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

If you're a dev and want to compile with the debug enabled, change the first line from the commands listed above:

`$ qmake -r ../server.pro CONFIG+=debug`

For information on how to run the server checkout the [documentation]({filename}02_1_server.md)

# FAQ

## I'm getting error like this: RCC: Error in 'rolisteam.qrc': Cannot find file 'translation/rolisteam_fr.qm'

rolisteam_fr.qm is a binary translation file. It's generated from rolisteam_fr.ts.
Run this command:
 lrelease translation/rolisteam_fr.ts

or run linguist (Qt translator tool) and release translations.
Then the compilation must be just fine.

## Some files are not found by the compiler

Perhaps, you forgot the --recursive parameter when getting the source code.
