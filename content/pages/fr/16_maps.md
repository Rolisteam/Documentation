Title: Plan
Date: 2017-06-11 10:20
slug: map
status: hidden
lang: fr

Les plans
=========

Dans toute partie de jeu de rôles, il arrive un moment où le MJ saisit
un bout de papier pour dessiner un plan, gribouiller un rapide schéma
d\'un mécanisme, ou bien sort de derrière son paravent un magnifique
plan photocopié dont il essaie de cacher la majeure partie. Les plans de
[Rolisteam](/Rolisteam "wikilink") sont là pour remplir cette fonction.
Vous allez pouvoir dessiner vos cartes à main levée, ou les importer à
partir de votre bibliothèque d\'images, ou bien encore préparer vos
plans à l\'avance, en les annotant et en masquant les zones hors de vue
des PJ. Les plans permettent d\'afficher des cartes issues de fichiers
images (JPEG, PNG, BMP), sur lesquels il vous sera possible de dessiner
et d\'ajouter des personnages.

D\'une manière générale le plan peut être considéré comme la
superposition de trois calques :

-   le calque du fond est soit une image, soit une couleur unie (si vous
    créez un plan vide) ;
-   vous pouvez dessiner sur le calque du milieu (et effacer vos
    annotations à l\'aide de la couleur d\'effacement) sans altérer le
    calque inférieur ;
-   le calque du dessus permet de masquer les deux autres (à l\'aide des
    couleurs de masquage/démasquage).

Les fenêtres plan sont reconnaissables dans l\'espace de travail par
leur icône. Seul le MJ a la possibilité d\'ouvrir des plans. Il existe
pour cela trois manières de procéder :

-   Vous pouvez créer un plan vide de couleur unie, en cliquant sur
    *Nouveau plan vide* dans le menu *Fichier*. Vous pourrez alors
    spécifier le nom du plan, ses dimensions et sa couleur de fond. Le
    nouveau plan s\'ouvre alors chez tous les joueurs.
-   vous pouvez créer un plan à partir d\'un fichier image (JPEG, PNG ou
    BMP), en cliquant sur *Ouvrir plan* dans le menu *Fichier*, et en
    sélectionnant une image. L\'image est alors transférée aux joueurs
    et un nouveau plan est créé, aux dimensions de l\'image. Si vous
    préférez que le plan apparaisse masqué aux yeux des joueurs, il vous
    suffit d\'ouvrir le plan en utilisant *Ouvrir et masquer plan* dans
    le menu *Fichier*, puis en sélectionnant le fichier image.
-   Vous avez également la possibilité d\'ouvrir un plan préalablement
    sauvegardé avec [Rolisteam](/Rolisteam "wikilink"), en cliquant sur
    *Ouvrir plan* dans le menu fichier et en sélectionnant un plan
    (fichier .PLA). Le plan est alors transmis en l\'état aux autres
    joueurs. Notez que lors de la sauvegarde d\'un plan, les PJ sont
    remplacés par des PNJ (qui portent le numéro 0), charge à vous de
    remettre les personnages des joueurs présents à la place de ces PNJ.
    Vous avez là aussi la possibilité de masquer entièrement le plan,
    sans tenir compte des informations de masquage déjà présentes sur
    celui-ci, en l\'ouvrant avec *Ouvrir et masquer plan*.

Une fois le plan ouvert, il est possible de dessiner dessus à l\'aide
des outils de dessins de la barre d\'outils. Vous pouvez également
ajouter des PNJ toujours grâce à la barre d\'outils, et faire apparaître
les PJ en cochant les cases appropriées dans la liste des utilisateurs.
Le MJ a également la possibilité de masquer certaines parties du plan à
l\'aide de la couleur spéciale *masquer* qui peut être utilisée avec
n\'importe quel outil de dessin. La zone couverte devient alors opaque
pour les joueurs, tout en restant transparente pour le MJ. Le plan se
démasque avec la couleur spéciale *démasquer*.

Vous pouvez sauvegarder un plan en l\'état en cliquant sur *Sauvegarder
plan* dans le menu *Fichier*. Dans le fichier sauvegardé les PJ sont
transformés en PNJ : ils gardent le même nom, la même couleur et portent
le numéro 0. Cette transformation permet d\'ouvrir le plan même si tous
les joueurs présents lors de la sauvegarde ne le sont pas au moment de
l\'ouverture de celui-ci. Un plan peut également être sauvegardé dans le
cadre d\'un scénario (*Sauvegarder scénario* dans le menu *Fichier*).
Lorsque le MJ sauvegarde un scénario, Rolisteam crée un fichier .SCE
contenant tous les plans et images actuellement ouverts, ainsi que les
notes de l\'utilisateur. À l\'ouverture d\'un scénario les plans et les
images contenus dans celui-ci sont transmis à l\'ensemble des joueurs
connectés, et les notes du MJ sont mises à jour.

Comme pour les autres fenêtres de l\'espace de travail, les plans
peuvent être fermés, ce qui a pour seule conséquence de masquer la
fenêtre. Pour faire à nouveau apparaître le plan il suffit de cliquer
sur son titre dans le menu *Fenêtre*. Si vous désirez enlever le plan de
la partie en cours, c\'est à dire qu\'il soit définitivement fermé chez
l\'ensemble des joueurs, vous devez cliquer sur *Fermer plan/image* dans
le menu *Fichier*. Le plan disparaît alors chez tous les utilisateurs.
Seul le MJ peut fermer définitivement un plan.

Version 1.6.0
-------------

Le menu d\'ouverture d\'un plan permet la sélection du titre, du mode de
permission, du chemin du plan, et si le plan est caché ou non.

Il existe 3 modes de permissions, les permissions correspondent au droit
des joueurs:

-   **Aucun Droit**: Ils n\'ont le droit de rien faire.
-   **Personnage**: Il peuvent placer que leur personnage.
-   **Tous les droits**: Il ont le droit de tout faire.

Actions possibles
-----------------

Les actions réalisables sur un plan sont principalement issue des outils
de la barre d\'outil de dessins

Barre d\'outils
===============

[right\|top\|\|frame\|400px\|\|Toolbar](/Image:_Toolbar.png "wikilink")
Cette barre regroupe tous les outils permettant d\'agir sur les plans
(l\'outil main peut également être utilisée sur les images). Elle est
divisée en deux parties : la partie haute contient les outils de dessin,
alors que la partie basse contient les outils de manipulation des
PJ/PNJ. Les outils de dessin permettent de dessiner un plan (s\'il est
vide) ou bien d\'en annoter un (s\'il a été importé). Description des
outils de dessin :-

Couleur actuelle
----------------

indique la couleur actuellement employée pour dessiner. En cliquant sur
la couleur vous ouvrez un sélecteur de couleur permettant de choisir
précisément une teinte, et de définir les couleurs personnelles (si vous
êtes sous Windows). A tout moment, et avec n\'importe quel outil de
dessin il est possible de sélectionner sur le plan la couleur se
trouvant sous le pointeur de la souris, en effectuant un clic droit (le
pointeur se transforme alors en pipette);

Couleurs prédéfinies
--------------------

un ensemble de couleurs sélectionnables;

Couleurs personnelles
---------------------

Il s\'agit des couleurs définies par l\'utilisateur. Si vous êtes sous
Windows vous pouvez les choisir à l\'aide du sélecteur de couleur qui
s\'ouvre lorsque l\'on clique sur la couleur actuelle : les couleurs
personnelles peuvent être modifiées à l\'intérieur de ce dernier. Si
vous êtes sous MacOS vous pouvez modifier une couleur en double-cliquant
dessus;

Couleurs spéciales
------------------

[Image: Erase.png](/Image:_Erase.png "wikilink") ou [Image:
ShowMap.png](/Image:_ShowMap.png "wikilink")

Il existe trois couleurs spéciales qui sont, de gauche à droite, la
couleur pour effacer, la couleur de masquage, et celle de démasquage. La
couleur pour effacer permet de gommer le dessin avec n\'importe quel
outil (sans toucher à l\'image de fond du plan), elle permet de créer
une gomme de n\'importe quelle forme. Les couleurs pour masquer et
démasquer permettent au MJ de cacher ou montrer aux joueurs certaines
parties du plan et les PNJ qui y sont disposés. Ces trois couleurs
peuvent être utilisées avec n\'importe quel outil de dessin;

Crayon
------

[Image: Pen.png](/Image:_Pen.png "wikilink")

permet de dessiner à main levée;

Ligne
-----

[Image: Line.png](/Image:_Line.png "wikilink")

trace une ligne entre le point où le bouton gauche de la souris a été
enfoncé et celui où il a été relâché;

Rectangle vide
--------------

[Image: Emptyrectangle.png](/Image:_Emptyrectangle.png "wikilink")

dessine un rectangle vide entre le point où le bouton gauche de la
souris a été enfoncé et celui où il a été relâché;-

Rectangle plein
---------------

[Image: Filledrectangle.png](/Image:_Filledrectangle.png "wikilink")

idem, avec un rectangle plein;

Ellipse vide
------------

[Image: Emptyellipse.png](/Image:_Emptyellipse.png "wikilink")

dessine une ellipse vide centrée sur le point où le bouton gauche de la
souris a été enfoncé;

Ellipse pleine
--------------

[Image: Filledellipse.png](/Image:_Filledellipse.png "wikilink")

idem, avec une ellipse pleine;

Texte
-----

[Image: State.png](/Image:_State.png "wikilink")

Le bouton permet de sélectionner l\'outil, alors que la zone de saisie
contient le texte à inscrire sur le plan. Un clic gauche sur le plan
fait apparaître le texte contenu dans la zone de saisie, vous pouvez
alors déplacer la souris pour le positionner à l\'endroit approprié, la
relâche du bouton dessine le texte à l\'emplacement du pointeur.

Main
----

[Image: Hand.png](/Image:_Hand.png "wikilink")

La main permet de se déplacer sur le plan sque celui-ci est plus grand
que la fenêtre qui le contient. Pour déplacer la vue du plan, cliquez
sur une zone du plan, maintenez le bouton enfoncé et déplacez la souris,
puis relâchez le bouton. L\'outils main fonctionne également sur les
images;

Grosseur du trait
-----------------

Le curseur permet de choisir la taille du trait qui sera utilisée pour
le crayon, les lignes, les rectangles et les ellipses vides. La zone
d\'affichage présente la grosseur du trait sélectionnée.Un PJ ou PNJ est
représenté par un disque de couleur sous lequel est affiché son nom et
son numéro (pour les PNJ). Les PJ se différencient par la présence d\'un
point au centre du disque. Il est parfois nécessaire de savoir dans
quelle direction regarde un personnage, pour cela il est possible de
faire un apparaître un indicateur de direction ou de le masquer. De même
il est possible d\'indiquer l\'état de santé d\'un personnage.
Description des outils de manipulation des PJ/PNJ :

Déplacer PJ/PNJ
---------------

[Image: MoveNpc.png](/Image:_MoveNpc.png "wikilink")

A l\'aide de cet outil, vous pouvez déplacer les PJ et PNJ présents sur
la carte : effectuez un clic gauche sur le personnage, maintenez le
bouton enfoncé et déplacez-le avant de relâcher le bouton. A cet instant
un déplacement identique a lieu chez les autres utilisateurs. En
effectuant un clic droit sur un personnage vous faites apparaître
l\'orientation de celui-ci, un nouveau clic droit la masque. Pour
modifier l\'orientation cliquez avec le bouton droit sur le point vers
lequel le personnage doit regarder;

Changer état PJ/PNJ
-------------------

[Image: State2.png](/Image:_State2.png "wikilink") A chaque clic sur un
personnage, son état de santé évolue :sa couleur change, et la bulle
d\'aide qui apparaît lorsque l\'on place la souris au dessus de lui est
mise à jour avec son nouvel état. Les états de santé sont les suivants :
sain, blessé léger, blessé grave, mort, endormi, ensorcelé. En
effectuant un clic droit sur un personnage vous faites apparaître
l\'orientation de celui-ci, un ouveau clic droit la masque. Pour
modifiez l\'orientation cliquez avec le bouton droit sur le point vers
lequel le personnage doit regarder;

Ajouter PNJ
-----------

[Image: Add.png](/Image:_Add.png "wikilink")

A chaque clic gauche sur le plan un nouveau PNJ apparaît. Vous pouvez le
positionner en maintenant le bouton gauche enfoncé et en déplaçant la
souris. Une fois le bouton relâché le PNJ apparaît chez les autres
utilisateurs. Le nouveau PNJ a la couleur actuelle, la taille
actuellement sélectionnée, le nom entré dans la zone de saisie, et le
numéro indiqué. Le numéro de PNJ est automatiquement incrémenté, ainsi
un ensemble de PNJ ajoutés à la suite portent tous un numéro différent.
Notez qu\'il est impossible d\'ajouter un PNJ lorsque l\'une des trois
couleurs spéciales est sélectionnée. Un clic droit sur un PJ ou un PNJ
permet de récupérer sa couleur, son nom et sa taille, vous pouvez ainsi
dupliquer un type de personnage déjà présent sur le plan;

Supprimer PNJ
-------------

[Image: Remove.png](/Image:_Remove.png "wikilink")

Les PNJ sélectionné est supprimé du plan. N\'a aucun effet sur les PJ.
Un clic droit sur un PJ ou un PNJ permet de récupérer sa couleur, son
nom et sa taille, vous pouvez ainsi dupliquer un type de personnage déjà
présent sur le plan;

Remise à 0 du numéro de PNJ
---------------------------

[Image: Chronometre.png](/Image:_Chronometre.png "wikilink")

En cliquant sur ce bouton le numéro du prochain PNJ repasse à 1;

Numéro du PNJ
-------------

Il s\'agit du numéro que portera le prochain PNJ qui sera ajouté sur le
plan. Après 99 le numéro repasse à 1;

Nom du PNJ
----------

Zone de texte où doit être saisie le nom du PNJ à ajouter sur le plan

Taille du PNJ
-------------

Permet de choisir la taille du PNJ que l\'on souhaite ajouter sur le
plan.

<p style="text-align: left; width:49%; display: inline-block;"><a href="/fr/images.html">Précédent</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/fr/vectorialMap.html">Suivant</a></p>
