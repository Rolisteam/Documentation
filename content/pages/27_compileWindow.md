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
* Fork ![rolisteam]({filename}fork.png) the wanted project and its dependencies.
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
```
git clone --recursive https://github.com/Rolisteam/rolisteam.git
```

The source code comes on your computer.
You won't be able to integrate your work in **Rolisteam**, until we give you permission to do so.
To do it, we have to accept you in **Rolisteam** organization. [Give us]({filename}20_contactus.md) your github username.

Of course, you can send us patch. But it's less pratical this way.

## I don't want to create github account

Then, just clone the project from the main repository  
```
git clone --recursive https://github.com/Rolisteam/rolisteam.git
```


# Pre-requirements

## C++ tools

**Rolisteam** is written in c++, so C++ compiler is required to work on it.
There are several options.

Install [Visual Studio](https://visualstudio.microsoft.com/) or [MinGW](http://www.mingw.org/) (Qt can install it for you).

### Compiler Pros and Cons:

<table>
<tr><th>Compiler</th><th>Pros</th><th>Cons</th></tr>
<tr><td>Visual Studio</td><td>Compile all Rolisteam features<br/>Compile rolisteam in 64bits or 32bits</td><td>difficult to install</td></tr>
<tr><td>MinGW</td><td>Really easy to install (Qt installer does the job)</td><td>can't compile some rolisteam features (webview and PDF viewer).<br/> 32bits only (for the moment)</td></tr>
</table>

## Qt5

The first thing is to install **Qt** (v5.10 or higher).  
Get Community version of Qt: [https://www.qt.io/download/](https://www.qt.io/download/)

At the Qt installation, please select Qt package compatible with your compiler.
If you don't have any. Select mingw version.
**Qt** will install mingw on your computer.

The best option is to compile with visual studio 2015 but it is much easier with mingw. MinGW can make all features of **Rolisteam** working.

On windows, please use visual studio 2015 to compile. 
On Windows 10, you may feel the need to use Visual studio 2017.  
As it is painful to install it, **Rolisteam** may still be compiled with other compilers but some features won't be working.

## Zlib

Rolisteam needs zlib to save its notes as *OpenDocument (odt)*  

Install the right dependency given your compiler.
 * mingw : [zlib](http://blog.rolisteam.org/file/zlibapi.zip)
 * visual studio 2015: [zlib vc2015](http://blog.rolisteam.org/file/zlib_1_2_8.zip)

Note that more recent visual studio versions may work as well but it is better to recompile it.

### where to install

The file hierarchy must be like that:

```
C:\where\you\want
  |-rolisteam\ (source code)
  |-lib\
```

Extract the archive content inside the `lib` directory.
A directory `zlibapi` should appears if you are using mingw.
For visual studio, the directory is called `zlib_1_2_8`.


# Compile **Rolisteam**

At this step, you are ready to compile.

Open `rolisteam.pro` with `qtcreator`. Let qtcreator loads the project and then click on `Build (Ctrl+b)` and `run (F5)`.
**Rolisteam** starts.  


# Remove some features.

Removing some features may help to compile. As feature requires dependencies.

## Zlib.

To remove the need of *Zlib*, edit `rolisteam/client/client.pro` and comment out:

`CONFIG += HAVE_ZLIB` to `#CONFIG += HAVE_ZLIB`

This will disabled saving note as OpenDocument.

## Webengine

**Webengine** is a Qt component. It is dedicated to display web page. **Rolisteam** may uses it inside some charactersheets.
Qt on windows provides it only in the visual studio 2015.

Webview is also used for viewing pdf, in order to compile rolisteam without webview, you must also disable the PDF feature.

In an extreme case, remove the need of *webengine* .
Edit `rolisteam/client/client.pro` and comment out:

<pre>
#CONFIG += HAVE_WEBVIEW  
#CONFIG += HAVE_PDF
</pre>

## Sound

Rolisteam comes with audio players. These player required QtMultimedia module and its backend.

Edit `rolisteam/client/client.pro` and comment out:

```
CONFIG += HAVE_SOUND
```

## PDF

Rolisteam (since 1.9) can display PDF. If you don't want this feature:
Edit `rolisteam/client/client.pro` and comment out:

```
CONFIG += HAVE_PDF
```

# FAQ

### I'm getting error like this: RCC: Error in 'rolisteam.qrc': Cannot find file 'translation/rolisteam_fr.qm'
`rolisteam_fr.qm` is a binary translation file. It's generated from rolisteam_fr.ts.
Run the command below to generate all translation file:
```
 lrelease client/client.pro
```
or run linguist (Qt translator tool) and release translations.
Then the compilation must be just fine.

### zlib compilation
zlib1g can be install on Windows, but there is an issue into zconf.h include:

<pre>
#if 1           /* HAVE_UNISTD_H -- this line is updated by ./configure */
</pre>
replace this line by

<pre>#if HAVE_UNISTD_H  /*-- this line is updated by ./configure */</pre>
