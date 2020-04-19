Title: Preferences
Date: 2017-06-11 10:20
slug: preferences
status: hidden
lang: fr

==================

Les préférences sont réparties dans cinq catégories:

-   Général
-   Les thèmes
-   Chemins de l\'application
-   Les règles
-   Diagnostic

Général
-------

Le panneau Général des préférences permet de définir la couleur du
brouillard de guerre, ainsi que sa transparence. Tout changement sera
pris en compte pour les prochaines cartes. Les cartes déjà existantes ne
seront pas modifiés.

De plus, le panneau Général permet d\'ajuster le comportement de
Rolisteam. -Il est possible d\'activer/désactiver la vérification des
\"mise à jour\" (Activé par défaut). -Il est possible de demander à
Rolisteam de se lancer en plein écran au démarrage (Activé par défaut).
-Les images s\'ouvrent avec l\'option \"ajuster à la fenêtre\" par
défaut (Activé par défaut). -Vous pouvez définir les permissions par
défaut de vos plans. Vous serez toujours capable de définir les
permissions à la création d\'un plan (défault no permission). -Vous
pouvez définir un chemin vers un fichier de traduction. Il sera utilisé
pour le prochaine démarrage.

Thèmes
------

Pour consulter l\'aide de ce panneau voir l\'article qui lui est
consacrée: [thèmes](/thèmes "wikilink")

Chemins de l\'application
-------------------------

Ce panneau vous permet de sélectionner le dossier par défaut pour ouvrir
ou enregistrer le chemin par défaut de tous les types de média. Ainsi,
vous pouvez définir le chemin vers les musiques quand vous êtes MJ ou
joueur, le dossier de vos images, de vos plans, de vos scénarios (.sce),
de vos notes et de vos tchats.

Les règles
----------

### Les alias de dés

Ce panneau vous propose de superviser les alias de votre partie. Vous
pouvez ajouter, supprimer, modifier les alias et changer leur priorité
(ordre dans la liste). Le panneau propose également un moyen simple pour
tester l\'alias. Les alias du MJ sont automatiquement partagés avec ses
joueurs. Il est possible de désactiver un alias pour qui ne soit pas
considérer temporairement. Il est également possible d\'ajouter une
commentaire pour expliquer l\'alias.

#### substitution : Remplacement

C'est le mode par défaut. Il est très simple à comprendre. Rolisteam
effectue un remplacement trait pour trait de l'alias.

Exemple:

Alias: G =\> d10e10k Utilisations:

-   !6G3 = !6d10e10k3
-   !8G4 = !8d10e10k4

Ce mode convient bien quand les éléments changeants de la commande sont
sur les extérieurs.

#### substitution : Expression Régulière

Quand il vous faut définir un élément au milieu de la commande. Vous
êtes obligés de passer par une substitution en expression régulière. La
première chose à faire est de cocher la case afin d'activer la
substitution.

Exemple:

Alias: (.\*)wod(.\*) =\> \\1d10e10c\[\>=\\2\] Utilisations:

-   !6wod3 = !6d10e10c\[\>=3\]
-   !8wod4 = !8d10e10c\[\>=4\]

Exemple 2: Alias: (.\*)dd(.\*),(.\*) =\> \\1d\[0-9\]k\\2c\[\>=\\3\]

-   !6dd3,4 = 6d\[0-9\]k3c\[\>=4\]

### États des personnages

Ce tableau vous permet de mettre en place des états de personnages et de
redéfinir ceux par défaut.

Un état possède un nom, une couleur et une image. A l\'image des alias
de dés, les états de personnages du MJ sont partagés avec les autres
joueurs.

Diagnostic
----------

Ce panneau a pour but de lister et tester les fonctionnalités de votre
machine. Vous pouvez communiquer la sortie de la commande si vous
rencontrez un problème avec rolisteam.
<p style="text-align: left; width:49%; display: inline-block;"><a href="/fr/diceroller.html">Précédent</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/fr/look.html">Suivant</a></p>
