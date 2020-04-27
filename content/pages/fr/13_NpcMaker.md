Title: Npc Maker
Date: 2017-06-11 10:20
slug: npcmaker
status: hidden
lang: fr


La **Forge aux PNJ** permet de créer des jetons pour vos cartes vectorielles.

![Npc Maker]({static}/images/en/npc_makerinfo_screen.jpg)

# Onglets

* Information générale
* Actions
* Formes
* Propriétés

# Information générale

![Npc Maker]({static}/images/en/npc_makerinfo_screen.jpg)

Vous devez saisir les informations suivantes:

* Nom du personnage non joueur
* Gestion des points de vie (min, max et courant)
* La commande d'initiative (une commande de dé, pas besoin de la préfixer par `!`)
* Le score d'initiative  (si vous avez défini une commande d'initiative, vous pouvez laisser vide ce champ)
* L'avatar par défaut
* La taille par défaut
* La couleur du PNJ

(Attention: les versions inférieures à 1.9.3 présentent un problème si aucun avatar n'est défini.)

# Les actions

![Npc Maker]({static}/images/en/npcmake_actions_screen.jpg)

Les personnages PNJ possèdent une liste d'actions.
Ses actions sont des commandes de dés.
Les actions peuvent être exécutées depuis le menu contextuel des jetons sur une carte vectorielle.
Le résultat de ces commandes apparaît dans la messagerie instantanée commune (le commun).

# Les formes

![Npc Maker]({static}/images/en/npcmaker_shape_screen.jpg)

Les formes changent l'avatar du personnage. Très utile pour un personnage ayant des transformations.

# Les propriétés

![Npc Maker]({static}/images/en/npcmaker_property_screen.jpg)

Les propriétés sont une liste de clés et de valeurs. C'est une façon très simple de définir les traits de votre PNJ.
Les actions peuvent exploiter les valeurs issues des propriétés comme paramètre d'une commande.
Exemple:
Mon assassin a 8 en agilité.
Je vais donc créer une propriété «agilite» et lui donner comme valeur 8.
Dans le panneau action, je vais ajouter l'action «tirer à l'arc» et la commande sera: "1d20+${agilite}"

Il devient ainsi facile de faire une gamme complète de personnages. Vous pouvez faire l'assassin débutant, le vétéran, le chef assassin, etc.
Les actions restent les mêmes, mais les valeurs des propriétés changent.

# Charger/sauvegarder un jeton

Pour charger un jeton et l'éditer, il convient d'utiliser le bouton **importer**.
Quand vous avez terminé l'édition, appuyer sur **exporter** pour sauvegarder le jeton (dans un fichier .rtok).

# Ajouter un jeton sur une carte vectorielle.

Les jetons doivent être déposés sur une carte vectorielle. L'avatar par défaut sera alors visible. Un menu contextuel permet de lancer les actions ou encore de changer la forme actuelle.

De plus, les cartes vectorielles offrent la possibilité de lancer l'initiative pour tous les jetons présents sur la carte (tous les PNJ, Tous les PJ ou les deux)

<p style="text-align: left; width:49%; display: inline-block;"><a href="/fr/dicebookmark.html">Précédent</a></p> <p style="text-align: right; width:50%;  display: inline-block;"><a href="/fr/music.html">Suivant</a></p>
