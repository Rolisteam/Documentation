Title: Plan vectoriel
Date: 2017-06-11 10:20
slug: vectorialMap
status: hidden
lang: fr

Les plans vectoriels
====================

Une des grosses nouveautés de la version 1.8 est l\'ajout des plans
vectoriels. A la différences des anciens plans, il est maintenant
possible d\'ajouter un objet et de le modifier par la suite. Par
exemple, un rectangle peut-être agrandi, tourné, réduit, déplacé et il
en va de même pour tous les éléments.

Fonctionnalités
---------------

-   Positionnement: Chaque élément est placé au dessus des éléments
    précédents.
-   Taille de plan infini
-   Zoom avant
-   Zoom arrière
-   Déplacement de la portion visible
-   Modification des éléments du plan (Ajouter, agrandir, rétrécir,
    déplacer, tourner, supprimer).
-   Gestion des jetons de joueurs
-   Gestion des Avatars
-   Ajout d\'images
-   Gestion d\'images animées (gif...)
-   Gestion des collisions
-   Gestion par couches
-   Opacité
-   etc.

### Zoom

Il est possible de zoomer: Il faut utiliser la molette et la touche
**Shift**. Les actions sont également accessible le menu contextuel du
plan.

Créer un nouveau plan vectoriel
-------------------------------

Il suffit d\'ouvrir le menu «fichier» puis d\'aller dans la section
nouveau pour cliquer sur «Plan Vectoriel». Une fenêtre s\'ouvre:

[frame\|left](/File:Open_vmap_fr.png "wikilink")

-   Le titre est le nom du plan. Il est important de donner un nom clair
    afin de retrouver facilement le plan.
-   La couleur de fond définie la couleur utilisé par Rolisteam pour
    peindre le fond du plan. Par défaut: Blanc.
-   La visibilité définit comment les joueurs vont voir la carte. En
    caché, les joueurs ne verront qu\'un vaste carré dans la couleur de
    fond. En brouillard de guerre, cela affiche un grand voile noir par
    dessus la carte. En visible, la carte apparaît aux joueurs
    (Peut-être changé en cours de partie).
-   Le mode de permission définit les droits que les joueurs ont le
    droit d\'avoir sur la carte (Peut-être changé en cours de partie).
-   Le schéma de grille définit la forme de la grille: Sans schéma (pas
    de grille), grille carrée, grille hexagonale.
-   La couleur permet de changer la couleur d\'affichage de la grille.
-   La taille permet de définir la taille du schéma en pixels.
-   L\'échelle permet de définir combien mesure un schéma de la carte
    dans l\'unité de votre choix.

Ouvrir un plan vectoriel
------------------------

Pour ouvrir un plan, il convient d\'aller dans le menu **Fichier \>
Ouvrir \> Plan Vectoriel**. Une fenêtre de sélection de fichier
s\'ouvre. Il est maintenant possible d\'aller chercher le fichier dans
votre ordinateur. L\'extension d\'un plan vectoriel est .vmap .

Les éléments graphiques disponibles
-----------------------------------

### Boîte à outils

[left](/File:Toolboxvmap_fr.png "wikilink")

#### Sélecteur de couleur

Le premier carré est la couleur courante. Il est possible de
double-cliquer sur cette zone afin de faire apparaître une boite de
dialogue de choix de couleur. La zone multicolore permet de choisir la
teinte de la couleur courante. Le dernier sélectionneur permet de
choisir si la teinte doit être claire ou sombre.

#### Mode d\'édition

Il existe trois modes d\'édition.

-   Normal, pour peindre normalement sur le plan.
-   Masquer permet d'éditer le brouillard de guerre pour cacher des
    zones à vous joueurs.
-   Démasquer permet d'éditer le brouillard de guerre pour faire
    apparaître des zones.

Après avoir changer de mode utiliser les outils de dessins, les tracés
s'appliqueront sur le plan en mode normal ou sur le brouillard de guerre
pour les deux autres modes.

#### Crayon

Il permet de faire un tracé à main levée. Il suit les mouvements de la
souris.\
La largeur de trait est défini par l\'outil \[Diamètre de l\'outil\].\
Il peut être déplacer mais le changement de la courbure n\'est pas
supporté.\

#### Ligne

Il permet de faire un tracé un segment droit. Il convient de définir son
point de départ puis son point d'arrivée.\
La largeur de trait est défini par l'outil \[Diamètre de l'outil\].\
Il peut être déplacer et le point de départ ou d'arriver peuvent être
changer.\

#### Rectangle Vide

Il permet de tracer des rectangles ou seul la bordure est visible.\
La largeur de la bordure est défini par l'outil \[Diamètre de
l'outil\].\
Il peut être déplacer ou modifier en déplaçant ses coins.

#### Rectangle Plein

Il permet de tracer des rectangles pleins.\
Il peut être déplacer ou modifier en déplaçant ses coins.

#### Ellipse Vide

Il permet de tracer des ellipses où seul la bordure est visible.\
La largeur de la bordure est défini par l'outil \[Diamètre de
l'outil\].\
Il peut être déplacer ou modifier en déplaçant les poignées.\

#### Ellipse Pleine

Il permet de tracer des ellipses.\
Il peut être modifier en déplaçant les poignées.\

#### Texte

Ajoute un élément texte sur la plan. Ce texte peut être modifier. Le
cadre définit la largueur maximum du texte. Il y a passage à la ligne
automatiquement. La hauteur de la zone s\'adapte en fonction du nombre
de ligne. Il est possible d\'ajouter des sauts de lignes manuellement
pour contrôler le découpage du texte. L\'élément Texte supporte le
langage HTML pour la mise en page. Il est possible de copier/coller
depuis une page web ou directement d\'éditer le texte avec l\'éditeur de
texte riche:
[<File:RicheTextEditor.png>](/File:RicheTextEditor.png "wikilink")

L\'éditeur permet de modifier facilement la taille, la couleur,
l\'affichage du texte. Il supporte le copier/coller. Il est également
possible de souligner, mettre en italique de barrer. Il supporte
également la création de liste. Il est également possible d\'éditer
directement le code Html, du message.

[200px](/File:SourceEdit.png "wikilink")

Tout le langage HTML n\'est pas supporté.

#### Main

Cet outil permet d\'attraper les éléments du plan et de les déplacer. Il
permet aussi d\'attraper les coins d\'un élément pour l\'agrandir ou le
tourner (grâce à la touche: Ctrl) Il est également possible de déplacer
le plan dans son ensemble en tenant enfoncé la touche Shift et en
cliquant sur le plan.

#### Règle

Cet outil permet de mesurer la distance entre 2 points du plan en
fonction de l\'échelle choisie.

#### Chemin

Un chemin est une ligne brisée. Il peut être fermé (clique droit sur le
chemin) et chaque point peut être déplacé individuellement.

#### Ancre

Il est possible d\'ancrer un élément à un autre. Cela définit une
relation de parenté. Si A est ancré à B. B est le parent de A. Si B est
déplacé, A est déplacé également. Si A est déplacé, cela n\'a aucun
impact sur B.

Cela permet de facilement simuler un véhicule par exemple. Il est
pratique de déplacer le véhicule, provoquant le déplacement des
personnages dans le véhicule.

#### Pipette

Il est possible de récupérer la couleur d\'un élément sur le plan.

#### Diamètre de l\'outil

Les chemins, les rectangles vides, les ellipses vides, les lignes et
l\'outil crayon utilise le diamètre pour se dessiner.

#### PNJ

L\'outil de création de PNJ, il est possible de définir un nom au PNJ,
le Plus est l\'outil qui permet d\'ajouter des PNJ sur le plan (à
l\'endroit du click). Le numéro de PNJ est augmenté après chaque nouvel
ajout de PNJ. Il est possible de le remettre à zéro en cliquant sur le
bouton (compteur).

#### Opacité

Cet outil permet de définir l'opacité de l\'élément courant.

### Barre d\'outils

[<File:Toolbarvmap_fr.png>](/File:Toolbarvmap_fr.png "wikilink")

Pour faire apparaître/disparaître cette barre d\'outil, il suffit
d'appuyer F9.

#### Couleur de fond

Contrôle la couleur de fond du plan courant.

#### Grille

Vous trouverez ici l\'ensemble des paramètres utiles pour gérer
l\'affichage de la grille. Dans l\'ordre, un bouton permettant
d\'afficher ou non la grille. Ensuite, vous pouvez choisir la forme de
la grille: Aucune, Carrée ou hexagonale. Si la grille n\'a pas de forme,
elle ne s\'affichera pas.

Il est également possible de définir la taille d\'un motif de la grille
et sa représentation dans l\'unité de votre choix.

#### Permission

La permission définit les actions réalisables par les joueurs. Il existe
trois mode de permission.

-   MJ seulement : dans ce mode, les joueurs n\'ont le droit de rien
    faire.
-   Personnage : les joueurs peuvent déplacer leur personnage sur le
    plan.
-   Tous : les joueurs peuvent modifier l\'ensemble des éléments et en
    ajouter.

#### Visibilité

Il existe trois mode de visibilité.

-   Caché: Tous les éléments sont cachés aux joueurs, le MJ voit tout.
-   Brouillard de guerre: Les éléments sont cachés par le brouillard qui
    peut être modifier par le MJ (Voir mode d\'édition).
-   Visible : Tous les éléments deviennent visibles pour les joueurs.

### Menu contextuel (clique-droit)

Depuis le menu contextuel, vous pouvez contrôler divers éléments de
l\'élément sous le curseur de la souris. Voici les différents types de
menu disponible.

#### Menu de la carte

[frame\|left](/File:MenuContextCarte.jpg "wikilink")

-   Éditer le calque permet de changer le calque courant du plan.
    [Fr:vMaps\#Gestions_des_Calques](/Fr:vMaps#Gestions_des_Calques "wikilink")
-   Changer la visibilité permet de définir comment les joueurs voient
    le plan.
    [Fr:vMaps\#Visibilit.C3.A9](/Fr:vMaps#Visibilit.C3.A9 "wikilink")
-   Zoom avant permet d\'agrandir les éléments visibles dans le plan.
-   Zoom arrière permet de voir plus d\'éléments du plan (ils
    apparaîtront plus petits).
-   Zoom avant Max permet d\'agrandir les éléments visibles du plan au
    maximum autorisé.
-   Zoom normal redéfinit le facteur de zoom à 1. Les éléments ne sont
    ni agrandis ni rétrécis.
-   Zoom arrière Max permet d\'élargir au maximum la zone de vision, les
    éléments seront petits.
-   Importer une image ajoute une image de votre ordinateur dans le plan
    (accessible aussi en déposant l\'image sur le plan).
-   Propriétés affiche la boute de dialogue de création de plan avec les
    données du plan actuel. Il est possible de les modifier.

#### Pour un élément

[frame\|left](/File:MenuContextuelRectangle.jpg "wikilink")

-   Descendre : positionne l\'élément courant sous les éléments qu\'il
    chevauche.
-   Monter : positionne l\'élément courant au dessus les éléments le
    chevauchants.
-   Tout en bas : positionne l\'élément courant sous tous les autres
    éléments.
-   Tout en haut : positionne l\'élément courant au dessus de tous les
    autres éléments.
-   Supprimer supprime l\'élément courant (accessible aussi avec la
    touche **Suppr**).
-   Duplication crée un nouvel élément ayant les mêmes propriétés que
    l\'élément courant.
-   Rotation permet de définir l\'angle de rotation avec précision.
-   Changer de calque permet de définir dans quel calque cet élément
    appartient.

#### Menu d\'un chemin

[frame\|left](/File:PathMenuContextual.jpg "wikilink")

-   **Fermer le chemin** ferme la forme géométrique.
-   **Remplir le chemin** remplit la forme géométrique.

#### Menu d\'un élément texte

[frame\|left\|upright=0.35](/File:TexteContextualMenu.jpg "wikilink")

-   **Modifier le texte...** permet d\'ouvrir l\'éditeur de texte
    [Fr:vMaps\#Texte](/Fr:vMaps#Texte "wikilink").
-   **Adapter au contenu** force l\'élément à reprendre une forme la
    plus proche possible du contenu.
-   **Taille de police** vous propose d\'augmenter ou réduire la taille
    de police.

#### Menu pour une sélection multiples

[frame\|left](/File:MenuSeveralItemsFR.png "wikilink")

-   **Supprimer** supprime les éléments courants (accessible aussi avec
    la touche **Suppr**).
-   **Descendre** positionne les éléments courants sous les éléments
    qu\'ils chevauchent.
-   **Monter** positionne les éléments courants au dessus des éléments
    les chevauchant.
-   **Tout en bas** positionne les éléments courants sous tous les
    autres éléments.
-   **Tout en haut** positionne les éléments courants au dessus de tous
    les autres éléments.
-   *\'Verrouiller* fixe la taille des éléments courants à leur taille
    actuelle. Cela empêche des modifications.
-   **Tourner** permet de définir l\'angle de rotation avec précision
    sur l\'ensemble des objets sélectionnés.
-   **Calque courant** définit le calque courant des objets
    sélectionnés.
-   **Normaliser les tailles** modifie les tailles des objets
    sélectionnés. Il est possible de prendre la taille moyenne, la
    taille la plus grande du lot, la taille la plus petite du lot ou la
    taille de l\'élément sous la souris.

Gestions des Calques
--------------------

Les calques sont des groupes dans lesquels les éléments se trouvent.
Cela permet de gérer facilement l\'interaction des éléments entre eux.
Il est conseillé d\'ajouter dans votre carte tous les éléments
définissants le sol, puis de passer par les objets de votre plan pour
finir par les personnages.

Attention, les calques ne permettent pas de gérer le chevauchement des
éléments. Le chevauchement est contrôlable par le menu contextuel.

**Chaque élément appartient à un et un seul calque**. L'appartenance
peut ềtre défini à l\'aide du menu contextuel. Au niveau du plan, vous
pouvez/devez définir le calque courant (par défaut **Sol**). **Tous les
éléments étrangers au calque courant ne pourront pas être modifiés**.
Pour un plan simple, il est possible de travailler uniquement dans un
seul calque par soucis de commodité.

### Sol

Les éléments appartenants au sol n\'entrent pas en collision avec les
personnages.

### Objet

Les objets de ce calque rentrent en collision avec les personnages.

### Personnage

Les personnages peuvent entrer en collision avec les objets quand la
gestion des collisions est active.

Brouillard de Guerre
--------------------

Le brouillard de guerre s'active grâce la barre d'outil. Il prend la
forme d'un voile noir cachant l'ensemble des éléments de la carte. Ce
voile est complètement opaque pour les joueurs et semi-transparent pour
le maître de jeu.

Pour modifier ce brouillard afin de faire apparaître des éléments (ou
les recacher). Il convient de passer les outils de dessin dans le mode
adéquate. Le sélecteur de mode d\'édition se trouve ici: [Mode
d'Edition](/Fr:vMaps#Mode_d.27.C3.A9dition "wikilink")
