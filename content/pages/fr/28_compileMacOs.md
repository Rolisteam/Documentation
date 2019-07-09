Title: Compile on Mac Os X
Date: 2017-06-11 10:20
slug: compmacos
status: hidden
lang: fr

# Before working on Rolisteam

Please discuss with us, so we can share the effort to make new features and your work will fulfill **Rolisteam** needs and goals.
Please take a look at our [roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=900739263)

# Get Source code

The way to get source code changes given your objectives.

## I want to compile stable version

To get the source, just [download the zip archive](http://www.rolisteam.org/download.html)

## I want to take part in **Rolisteam** development


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
To share your work, just make a pull request (github does it very well).

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
`git clone --recursive git@github.com:Your_login/rolisteam.git`

Congrats, the **Rolisteam** source code is on your computer.

## I have a github account but I don't want to fork so many repositories

Then, just clone the project from the main repository  
`git clone --recursive https://github.com/Rolisteam/rolisteam.git`

The source code comes on your computer.
You won't be able to integrate your work in **Rolisteam**, until we give you permission to do so.
To do it, we have to accept you in **Rolisteam** organization. [Give us]({filename}26_contactUs.md) your github username.

Of course, you can send us patch. But it's less pratical this way.

## I don't want to create github account

Then, just clone the project from the main repository
    > git clone --recursive https://github.com/Rolisteam/rolisteam.git


# Compile **Rolisteam**

At this step, you are ready to compile.

Open `rolisteam.pro` with `qtcreator`. Let qtcreator loads the project and then click on `Build (Ctrl+b)` and `run (F5)`.
**Rolisteam** starts.  


Otherwise, these commands can be helpful:
<pre>
 cd rolisteam
 lrelease rolisteam.pro
 qmake -r rolisteam.pro
 make
</pre>
(make sure to use qt5 qmake)


## start rolisteam

In terminal, just run:
`> rolisteam`

It may be possible to find rolisteam on graphical user menu, depending of your system.

Qt creator is able to start it.

## FAQ
### Having trouble with Qt4 and Qt5
If qt4 and qt5 are both installed on your computer, that may cause troubles.
While you compile Rolisteam v1.7.X (or higher), you must use qt5.
So you may need to run:
<pre>
  lrelease-qt5 rolisteam.pro
  qmake-qt5 rolisteam.pro
  make
</pre>

### How to make the installer


1. Copy/paste rolisteam.app into packaging/MacOs
2. Run installZlib.sh
3. appdmg  nodedmg.json rolisteam_v1.7.1-MacOsX_setup.dmg

<pre>
install_name_tool -change "/usr/lib/libz.1.dylib" "@executable_path/../Frameworks/libz.framework/libz.1.dylib" rolisteam

appdmg  ../../rolisteam/packaging/MacOS/nodedmg.json rolisteam_v1.7.1-MacOsX_setup.dmg
</pre>
