Title: Take part
Date: 2017-06-11 10:20
slug: take-part-coding
status: hidden
lang: en

# Contact us

Don't hesitate to [contact us]({filename}26_contactUs.md) and tell us what you want to do.

# Rolisteam Roadmap

Please, take a look at the [Rolisteam roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=769324568) before writing any code.

# Source code

**Rolisteam** is written in C++(11) and it is based on Qt5 framework. Its source code is managed on github. We use git.

[Official Rolisteam Page](https://github.com/Rolisteam/rolisteam)

## Getting the source code

Depending on how deep you want to be in **Rolisteam** development, there is two main ways to contribute.

### One task or few tasks (oneshot)

This approach is great for people who want to implement one feature, fix few stuffs or test current development tools.
The workflow is simple:

1. Get a github account
2. Fork rolisteam and its submodules (common, diceparser, charactersheet, RPlugins), all projets appears on your github profile
3. clone those git project on your computer.
4. Write the modification
5. Test the modification
6. Make "pull request"

### Be part of the project

1. Get a github account
2. Ask to be part of Rolisteam's team
3. When its granted you can clone official rolisteam repositories (and its subproject)
4. Write your code and commit your change.

To show your motivation is a good start to contribute several times as programmer. Then ask to be part of the team.

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

## Technical help

In order to work on **Rolisteam**, you need to set up a working environment and be able to compile **Rolisteam**.
It requires installation of several tools.

* [windows]({filename}27_compileWindow.md)
* [Linux]({filename}29_compileLinux.md)
* [MacOsX]({filename}28_compileMacOs.md).

The page should have all needed information.

Don't hesitate to contact us to speak about your wishes. So we can support your effort.


[Back]({filename}30_TakePart.md)
