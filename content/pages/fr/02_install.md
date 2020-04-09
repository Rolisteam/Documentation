Title: Install Rolisteam
Date: 2017-06-11 10:20
slug: install
status: hidden
lang: fr



Pour bien débuter clarifions les noms des éléments installables.  
Rolisteam c'est 3 programmes differents.  

*  Rolisteam
*  Rolisteam Character Sheet Editor (RCSE)
*  Roliserver

## Rolisteam

Le premier est le programme principal. Il peut être client ou serveur.
C'est un logiciel de table virtuelle. Il fournit toutes les fonctionnalités pour jouer à plusieurs.

## Rolisteam Character Sheet Editor (RCSE)

RCSE est l'éditeur de fiche de personnage. Il permet de les créer et les éditer.
Sa philosophie est d'aider à produire des fiches de personnages identiques à la version papier.

## Roliserver

Le serveur est utile pour des communautés qui voudrait fournir un hébergement de parties à ses membres.
Cela permet de réunir tout le monde autour d'un seul serveur.  

Roliserver tourne sur n'importe quel ordinateur mais il a été pensé pour fonctionner sur un ordinateur distant. 
Il n'y a pas d'interface graphique et la configuration passe par un unique fichier.  

Plus d'information [ici]({filename}fr/02_1_server.md)

# Windows

![image]({static}/images/logo/windows_logo.jpg)

## Obtenir Rolisteam

Pour obtenir **Rolisteam**, il suffit d'aller sur [la page download](http://www.rolisteam.org/download.html).

## L'installation

Double click sur *Rolisteam-v1.9.0-setup.exe*  

L'assistant d'installation apparaît:  

*  Accepter la licence GPL
*  Choisir où installer
*  L'installation se passe
*  Accepter l'installation des raccourcis sur le bureau
*  Démarrer Rolisteam.

**Attention:** Il semblerait que lancer Rolisteam en fin d'installation provoque un problème sur le glisser/déposer (drag and drop). 
Il est recommandé de le démarrer à partir d'un raccourci sur le bureau.

# Mac Os X

![image]({static}/images/logo/maxoslogo.png)

## Obtenir Rolisteam et RCSE

Pour obtenir **Rolisteam** et **RCSE**, aller sur la page [download](http://www.rolisteam.org/download.html).
Faites attention, il convient de télécharger 2 packages.

## Start installation

Double clicker sur **Rolisteam-v1.9.0-setup.dmg**  
L'assistant d'installation apparait, il suffit de copier **Rolisteam** dans le dossier app.

Double clicker sur **RCSE-v1.9.0-setup.dmg**  
L'assistant d'installation apparait, il suffit de copier **RCSE** dans le dossier app.

# GNU/Linux

![image]({static}/images/logo/linux-logo.jpg)

Certaines distributions fournissent **Rolisteam** sous forme de pacquet.  
Vérifier d'abord, si c'est le cas pour la votre. 
Si cela n'est pas le cas, vous pouvez remplir une demande de pacquet dans votre distribution.
Si la version proposée n'est pas la dernière, contactez le mainteneur du pacquet.

Il reste les installeurs génériques et la compilation.


# sur Ubuntu

Executer ces commandes:

        sudo add-apt-repository ppa:rolisteam/ppa
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install rolisteam rcse diceparser


# Compilation

La dernière solution c'est la compilation.
[compilation]({filename}29_compileLinux.md)



<p style="text-align: left; width:49%; display: inline-block;"><a href="/overview.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/firststeps.html">Next</a></p>
