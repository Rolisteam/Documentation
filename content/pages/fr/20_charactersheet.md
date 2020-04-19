Title: Fiche de Personnage
Date: 2017-06-11 10:20
slug: charactersheet
status: hidden
lang: fr


## Rolisteam CharacterSheet Editor (RCSE)

La création de fiche de personnage suit ces étapes: L'étape 0 est bien
sûr de lancer RCSE.

![rcse]({filename}/images/rcse.png)

### 1/ Importer une image


La première étape consiste à déposer une image de fond. Cette image est
le fond de votre fiche de personnage.

Elle peut être directement obtenu par le PDF de la fiche. Pour
transformer votre PDF en image, vous pouvez vous rendre sur ces sites:

-   <http://pdf2jpg.net/fr/>
-   <http://pdftoimage.com/fr/>
-   <https://www.freepdfconvert.com/fr/pdf-jpg>

Si vous avez des talents de graphistes, vous pouvez également la
dessiner vous même dans un logiciel de dessin.

Il existe deux moyens pour importer cette image:

-   Vous pouvez glisser/déposer l'image de votre choix
-   Vous pouvez l'importer par le menu \" \> Définir l\'image de
    background\"

Dans le cas, ou vous avez plusieurs pages dans votre fiche de
personnage. Vous pouvez ajouter une page avec le bouton prévu à cet
effet et définir le fond de cette page par les deux méthodes vues
plutôt. *\' Attention, si vous utilisez des fiches de personnages avec
plusieurs pages. Leurs arrières-plans doivent avoir la même
résolution.*\'

[<File:Inconnu_-_%C3%89diteur_de_fiche_de_personnage_pour_Rolisteam_002.png>](/File:Inconnu_-_%C3%89diteur_de_fiche_de_personnage_pour_Rolisteam_002.png "wikilink")

### 2/ Placer les champs textes


Une fois, les images de fond définies, il convient de placer les champs
sur cet panneau. Ce travail peut-être assez long mais il est quand même
plus efficace de le faire avec RCSE en graphique, plutôt qu'en «code».

Chaque champs nouvellement ajouté apparaît dans le tableau de droite. Si
vous avez fait une erreur, vous pouvez supprimer un champs depuis ce
tableau.

Il vous est possible de créer différents types de champs.

|Nom             |Nom dans le code |  Description                                                                                                                                           |   Icône|
|---------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
|Entrée texte    |TextInput          |Champs texte d'une ligne, sans bordure ni décoration. Peut se transformer en boite de sélection (voir plus bas)||
|Champs Texte    |TextField         | Champs texte d'une ligne, avec bordure et décoration.||
|Case à cocher   |Checkbox           |Case à cocher permet d'activer un état ou un élément. La donnée correspondante est un entier à 1 quand l'élément est coché et 0 quand il est décoché.||
|Zone de texte   |TextArea          | Champs texte de plusieurs lignes avec décoration et bordure.||
|Bouton         | Button            | Un bouton clickable pour lancer une commande de dés.||
|Image          | Image             | Affiche une image, la donnée correspondante est le chemin vers cette image. Principalement utile pour mettre des URLs: <http://monimage.fr/avatar.jpg>||

![Editor Rcse]({filename}/image/rcse2.jpg)

#### Transformer un Textinput en liste à choix

Il n'y a rien de plus simple. Il suffit de mettre les valeurs possibles
dans la colonne prévue à cet effet dans le tableau de droite. Chaque
valeur doit être séparée par une virgule, exemple:
rouge,bleu,vert,marron,jaune,noir,blanc,orange,violet

### 3/ Éditer les champs


Une fois les champs positionnés, il est important de leur donnée un nom.
Ce nom, nous le verrons plus tard sera utilisable dans les calculs de
formule.

En plus du nom, de nombreuses propriétés peuvent être changées. Tout
cela est modifiable par le tableau de droite dans le premier onglet.

Les colonnes:

|Nom                       |Description|
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|Id  |                      Cette propriété représente l'identifiant unique d'une donnée. Par défaut, il est généré automatiquement par RCSE. Il est recommandé de garder cette valeur. Il est possible d'accéder à la valeur de la donnée par l'id dans le système de dés et de formule. Exemple: =\${id_5}+4|
|Libellé                  | Cette propriété représente l'identifiant lisible d'une donnée. Il est laissé vide à l'ajout d'une donnée. C'est à l'auteur de la fiche de personnage de renseigner cette information. Il est possible d'accéder à la valeur de la donnée par le libellé dans le système de dés et de formule. Exemple: =\${intelligence}+4|
|Valeur                   | La valeur est affichée dans la fiche. Dans l'onglet d'édition, cette colonne sert à l'affichage de la fiche dans l'onglet vue. Les formules définies dans cette colonne n'auront pas d'impact. Il convient de les définir dans l'onglet personnage.|
|Valeur Possible           |Ce champs n'est utile uniquement pour les entrées textes (TextInput). Il permet de transformer une entrée texte en «sélecteur». Une sélecteur (ou un combobox ou menu déroulant) permet de choisir une valeur parmi une liste limitée.|
|Type                      |Rappel du type de données : Entrée Texte, Champs Texte,Case à cocher, Zone de texte, Bouton, Image.|
| X                         |Position en largeur de l'élément sur la fiche. Il est possible de modifier cette valeur pour aligner précisément l'élément.|
|Y                        | Position en Hauteur de l'élément sur la fiche. Il est possible de modifier cette valeur pour aligner précisément l'élément.|
|Largeur                  | Position en largeur de l'élément sur la fiche. Il est possible de modifier cette valeur pour aligner précisément l'élément.|
|Hauteur                 | Position en hauteur de l'élément sur la fiche. Il est possible de modifier cette valeur pour aligner précisément l'élément.|
|Adaptation de la police |  Cette propriété peut-être activer pour rendre les polices de caractères adaptables à la taille de la fiche.|
|Alignement du texte    |   Cette propriété permet de choisir la position du texte dans l'espace (larguer et hauteur) du champs.|
|Couleur du texte    |      Vous permet de changer la couleur de texte.|
|Couleur de fond      |     Vous permet de changer la couleur de fond du champs.|
|Bordure          |         Vous permet de choisir la présence ou non de bordure autour du champs.|

![Editor Rcse]({filename}/image/rcse3.jpg)

### 4/ Générer la fiche
-------------------

Quand vous avez fini d'ajouter les différents champs, vous pouvez
générer la fiche en cliquant sur « **Édition > Générer Code et fiche**
».

La fiche sera visible dans l'onglet **VUE**. Cette onglet montre la
fiche exactement comme elle sera dans rolisteam.

L'onglet «code» est également rempli par cette action. Il présente le
code.

Si vous remarquez des défauts ou des changements à faire sur la **VUE**,
vous pouvez revenir dans l'onglet **Editeur** pour faire quelques
changements sur les champs. Il convient en suite de générer le code et
la fiche. Vous pouvez faire ces étapes autant de fois que vous le
désirer pour obtenir le résultat parfait.

![Editor Rcse]({filename}/image/rcse4.jpg)

### Pour les experts

Il est également possible de modifier le code à la main pour ajouter des
fonctionnalités à la fiche. Le code en question est du QML. Il peut vous
permettre de jouer des sons, des vidéos, des animations et bien d'autres
choses encore. Faite attention, si vous modifiez le code, il ne faut pas
redemandé une génération car cela effacera vos modifications.

![Editor Rcse]({filename}/image/rcse5.jpg)

### 5/ Ajouter des personnages
--------------------------

Quand vous avez fini avec la création des champs et qu'ils s\'affichent
comme vous le désirer. La dernière étape est d'ajouter les personnages.
Il y a deux façons de le faire.

La première consiste à créer les personnages dans RCSE grâce à l'onglet
Personnages. La première colonne représente les champs que vous avez
défini précédemment. Grâce au menu contextuel, vous pouvez ajouter
autant de personnages que vous le souhaite. Une colonne nouvelle
apparaît pour chaque personnage. Il vous faudra saisir la valeur pour
chaque donnée. RCSE propose des fonctionnalités pour faciliter
l'édition.

La deuxième méthode consiste à créer les personnages dans rolisteam et
les partager avec vos joueurs et ainsi mutualiser l'édition. Chaque
joueur saisira les valeurs de son personnage. Voir le chapitre suivant,
plus bas dans la page pour plus d'information.

C'est dans ces cellules là qu'il est intéressant de mettre des
**formules**.

![Editor Rcse]({filename}/image/rcse6.jpg)

# Rolisteam


## Charger une fiche


Après l'édition de la fiche avec RCSE, vous devez avoir un fichier .rcs.
Ce fichier doit être chargé dans Rolisteam (**Fichier \> Ouvrir \> Fiche
de personnage** , **CTRL+U** ). Après cette étape, une fenêtre s'est
ouverte dans rolisteam. Elle contient un onglet données et un onglet par
personnage. L'onglet données est identique à l'onglet «Personnages» dans
RCSE. Cet ongle montre l'ensemble des valeurs de tous les personnages.
Il est facile pour un Maître du Jeu d'avoir un résumé des personnages.
Les autres onglets montrent chacun la fiche d'un personnage.

## Partager une fiche avec un joueur


Le MJ doit partager la fiche d'un personnage avec le joueur. Pour cela,
il doit être faire apparaître le menu contextuel (click droit), puis
aller dans le sous-menu «**Partager**» et choisir un personnage. Le
titre de l'onglet sera modifier afin de correspondre avec le personnage
choisi. Chez le joueur, une fenêtre apparaît avec deux onglets: un de
données et un autre avec le visuel de fiche. Il est possible de modifier
les valeurs depuis les deux vues.

## Plusieurs pages


Nous l'avons vu, il est possible de créer une fiche de personnage avec
plusieurs pages. Dans l'onglet vue, il est possible de passer d'une vue
à l'autre en utilisant les flèches **droite** et **gauche**. Il est
également possible de copier une vue et de la détacher. Par ce biais,
vous pouvez afficher en même temps les différentes pages d'une fiche.

## Formule de calcul

Les fiches de personnages gèrent un système de formule. Cela peut être
très utile pour effectuer des calculs automatiques afin de faciliter la
gestion mécanique du jeu. Pour activer la gestion des formules, il
suffit de démarrer la valeur d'une cellule par un symbole égal:**=**.
Suivi du reste de la formule.

# Formule - Opération possible


Le système de formule est capable de comprendre différents fonctions ou
opérations.

## Accéder à une valeur de la fiche

Comme nous l'allons vu plus haut dans la page. Il est possible d'obtenir
la valeur d'un champs en utilisant son Id ou son libellé. Le système a
besoin de voir les valeurs encadrées: \${libellé} ou \${id}.

## L'arithmétique

Il est possible d'effectuer des opérations arithmétiques classiques.
Exemple:

**Somme**

* `4+4`
* `${intelligence}+3`


**Soustraction**

* `12-3`
* `${intelligence}-3`

**Multiplication**

* `2*7`
* `2x7`
* `=${intelligence}*3`

**Division**

* `15/5`
* `15÷5`
* `=${intelligence}/3`
* `=${intelligence}÷3`

## Fonctions

### abs

Valeur absolue ne prend qu'un argument.


> =abs(-3)  
3

> =abs(3)  
3

> =abs(${intellegence}-11)  
8

### min

La fonction minimum retourne la valeur minimum de ses paramètres. Elle
peut en prendre un ou plusieurs.

> =min(3,8,10,1)  
1

> =min(${astuce},${dexterité})  
3

### max

La fonction maximum retourne la valeur maximum de ses paramètres. Elle
peut en prendre un ou plusieurs.

> =max(3,8,10,1)  
10

> =max(${astuce},${dexterité})  
    4

### concat

La concaténation prend plusieurs paramètres, minimum deux. Elle fusionne
plusieurs valeurs en une. Cela peut être pratique pour former des
chaines des commandes de dés par exemple.

>  =concat(${enquête}+${perception},"G",${perception})  
    7G3

> =concat(${enquête},"d10k",${perception})  
    4d10k3

### floor

floor ne prend qu'un argument. Elle transforme un nombre à virgule en
nombre entier supérieure.

> =floor(3.9)  
    3

> =floor(3.1)  
    3

> =floor(${force}/2)  
    1

### ceil

ceil ne prend qu'un argument. Elle transforme un nombre à virgule en
nombre entier supérieure.

> =ceil(3.9)  
    4

> =ceil(3.1)  
    4

> =ceil(${force}/2)  
    2

### avg

Cette fonction prend plusieurs paramètres pour en faire la moyenne.

> =avg(10,10)  
    10

> =avg(8,4)  
    6

> =avg(${intelligence},${dexterite})  
    3.5




<p style="text-align: left; width:49%; display: inline-block;"><a href="/fr/sharednotes.html">Précédent</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/fr/webview.html">Suivant</a></p>
