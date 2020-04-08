Title: Install Rolisteam
Date: 2017-06-11 10:20
slug: install
status: hidden
lang: en



First, it is important to know what to install.  
Rolisteam mow means 3 different programs.  

*  Rolisteam
*  Rolisteam Character Sheet Editor (RCSE)
*  Roliserver

## Rolisteam

The first one is the main program.   
It is the virtual table software. It provides every features   
for hosting games or joining games and play.


## Rolisteam Character Sheet Editor (RCSE)

RCSE is dedicated to create and edit Character sheet.  
It provides features to make character sheet looks like official paper ones.

## Roliserver

It is useful for communities which want to provide rolisteam as service to their members.  
Prepare a home sweet home for your community's.  

Roliserver runs on any computer but it is designed to be operate on distant server.  
There is no Graphical User Interface and the configuration is made though a configuration file.  

More information available [here]({filename}02_1_server.md)

# Windows

![image]({static}/images/logo/windows_logo.jpg)

## Get Rolisteam

Get **Rolisteam** on the [download](http://www.rolisteam.org/download.html) page.

## Start installation

Double click on *Rolisteam-v1.8.2-setup.exe*  

The installation wizard appears:  

*  Agree to license
*  Choice where to install
*  Let the installation go
*  Install shortcut to start rolisteam
*  Start Rolisteam.

**Attention:** It appears some features does not work when rolisteam has been started at the end of installation (such as drag and drop).
It is recommanded to close it and start it again from desktop shortcut.

# Mac Os X

![image]({static}/images/logo/maxoslogo.png)

## Get Rolisteam and RCSE

Get **Rolisteam** and **RCSE** on the [download](http://www.rolisteam.org/download.html) page.
Pay attention that there are two different packages.

## Start installation

Double click on **Rolisteam-v1.8.2-setup.dmg**  
The installation wizard appears then, copy **Rolisteam** to the app folder.

Double click on **RCSE-v1-setup.dmg**  
The installation wizard appears then, copy **RCSE** to the app folder.

# GNU/Linux

![image]({static}/images/logo/linux-logo.jpg)

Distribution may provide **Rolisteam** as package.  
Check if the rolisteam package is up-to-date.  
Please, contact the package maintener to ask update.

# on Ubuntu

Run these commands:

        sudo add-apt-repository ppa:rolisteam/ppa
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install rolisteam rcse diceparser


# Compilation

The last way, to get rolisteam is to compile it.
[compilation]({filename}29_compileLinux.md)


# Issues

## On Windows, Rolisteam does not start due to missing MSVCP140.DLL

You have to install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-US/download/details.aspx?id=48145) from Microsoft: 



<p style="text-align: left; width:49%; display: inline-block;"><a href="/overview.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/firststeps.html">Next</a></p>
