Title: Compile on Windows
Date: 2017-06-11 10:20
slug: windowscomp
status: hidden
lang: en


# Before working on Rolisteam

Please discuss with us, so we can share the effort to make new features and your work will fulfill **Rolisteam** needs and goals.
Please take a look at our [roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=900739263)

# Get Source code

The way to get source code changes given your objectives.

## I want to compile stable version

To get the source, just [download it](http://www.rolisteam.org/)

## I want to take part in **Rolisteam** development


### Git

**Rolisteam** manages its source code with **Git**. 
So, first learn how to use it a bit.
[Git](https://git-scm.com/)
[Learn Git](https://try.github.io/levels/1/challenges/1)

### Github 

Those steps are not mandatory but it definitely speeds up integration. 
To explain it a bit, those steps create a copy of **Rolisteam** and its dependencies into your github account.
Then, it allows you to do whatever you want. 
To share your work, just make a pull request (github does it very well).

1. Create your [github account](https://github.com)
2. Go to [Rolisteam organisation page](https://github.com/Rolisteam)
3. Fork ![Fork logo]({filename}fork.png) the wanted project and its dependencies.
    * **Rolisteam** project is the source code of **Rolisteam** and **Roliserver**. It needs **DiceParser**, **RCharacterSheet**, **RPlugins**
    * **RCSE** project is the charactersheet editor. Its needs **RCharacterSheet**.
    * **Dice** brings together all tools to roll dice.
4. Then those git repositories shoud appears in your github account: https://github.com/Your\_Login
5. For **Rolisteam** it is better to change the file `.gitmodules` before clone the repository
        ```
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
        ```
        Change every **Rolisteam** by **your github username**. This file describs where git should retrive dependencies (submodules). We make sure it retrieves them from your github account.
        Make this only if you plan to work on dependencies too.

6. For **Rcse** makes the same previous operation. The `.gitmodules` file is shorter than **Rolisteam** one.
7. Install git on windows or [github desktop](https://desktop.github.com/)
8. Clone **rolisteam**:
    > git clone --recursive git@github.com:Your_login/rolisteam.git

Congrats, the **Rolisteam** source code is on your computer.

## I have a github account but I don't want to fork so many repository

Then, just clone the project from the main repository
    > git clone --recursive https://github.com/Rolisteam/rolisteam.git

The source code appears on your computer.
You won't be able to integrate your work in **Rolisteam**, until we give you permission to do so. 
To do it, we have to accept you in **Rolisteam** organization. [Give us]({filename}20_contactus.md) your github username.

## I don't want to create github account

Then, just clone the project from the main repository
    > git clone --recursive https://github.com/Rolisteam/rolisteam.git 


# Pre-requirements

## Qt5

The first thing is to install **Qt** (v5.7 or higher).  
Get Community version of Qt: [https://www.qt.io/download/ https://www.qt.io/download/]

At the Qt installation, please select Qt package compatible with your compiler. If you don't have any. Select mingw version. 
**Qt** will install mingw on your computer.

On windows, please use visual studio 2015 to compile. 
As it is painful to install it, **Rolisteam** may still be compiled with other compiler but some features will not be working.

## Compiler-specific Features

## Zlib

Rolisteam needs zlib to save its notes editor as *OpenDocument (\*odt) *
This archive containt [http://blog.rolisteam.org/file/zlibapi.zip zlib] the required component for mingw or visual studio 2015.
More recent visual studio versions may work as well but it is better to recompile it.

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


## Disable Feature

These 3 features can switch off:

```
############## FEATURES ######################
CONFIG += HAVE_SOUND
CONFIG += HAVE_WEBVIEW
CONFIG += HAVE_ZLIB
############## END OF FEATURES ######################
```

It makes **Rolisteam** easier to compile.

## FAQ

### I'm getting error like this: RCC: Error in 'rolisteam.qrc': Cannot find file 'translation/rolisteam_fr.qm'
rolisteam_fr.qm is a binary translation file. It's generated from rolisteam_fr.ts. 
Run this command: 
 lrelease translation/rolisteam_fr.ts
Then the compilation must be just fine.

## zlib compilation 
zlib1g can be install on Windows, but there is an issue into zconf.h include:

 #if 1           /* HAVE_UNISTD_H -- this line is updated by ./configure */

replace this line by

 #if HAVE_UNISTD_H  /*-- this line is updated by ./configure */

