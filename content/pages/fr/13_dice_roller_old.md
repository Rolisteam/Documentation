Title: Dice Roller
Date: 2017-06-11 10:20
slug: dicerollerold
status: hidden
lang: fr


DiceParser
==========

La version 1.7 a introduit un système de dés: DiceParser. Il est
maintenant possible de construire des commandes complexes avec une
succession d\'opérateurs: Une documentation complète de la syntaxe se
trouve ici en anglais.
[1](https://github.com/Rolisteam/DiceParser/blob/master/HelpMe.md)

Voilà la documentation pour rolisteam.

Lancer les dés
--------------

`   !1d6`

Lancera un dés à 6 faces. Il est important de préfixer ses commandes par
un point d\'exclamation.

### Quelques exemples:

`   !1d6`

Lancera un dés à 6 faces.

`   !1d10`

Lancera un dés à 10 faces.

`   !5d10`

Lancera cinq dés à 10 faces.

`   !777d6`

Lancera 777 dés à 6 faces.

Liste des opérateurs
--------------------

`* k : Keep (garder)`\
`* K : Explose And Keep (Explose et garde)`\
`* s : sort (trier)`\
`* c : compter`\
`* r : reroll (relance: relance remplace l'ancienne valeur)`\
`* e : Explose (relance et ajoute à la valeur précédente du dés tant que cela respecte la condition)`\
`* a : reroll and Add (relance et ajoute le résultat. Equivalent a un explose mais une seule fois).`\
`* @ : jump backward (saut en arrière)`\
`* f : filtre`\
`* i : if (si)`\
`* m : merge (rassemble)`\
`* u : split (sépare) `\
`* p : paint (peindre)`

### Garde (Keep)

`   kX`

Cette option trie une série de dés et sélectionne les X meilleurs.

### Explose et Garde (Explose And Keep)

`   KX`

Le dés explose si sa valeur est le maximum du dés, ensuite option trie
la série de dés et sélectionne les X meilleurs.

### garde les plus bas (Keep Lower dice)

`   klX`

Cette option trie une série de dés et sélectionne les X plus bas.

### Tri (sorting)

`   3D10s`

Lance 3 dés à 10 faces et trie le résultat en ordre décroissant.

`   10d6sl `

Lance 10 dés à 6 faces et trie le résultat en ordre croissant.

### Compter

`   3D10c[Validateur]`

Compte combien de dés respecte une condition et affiche le résultat.
L\'opérateur colore les dés qui respecte sa condition (Plus de détails
sur les conditions dans la partie sur les Validateur).

### Relance (Reroll)

`   3D10r[Validateur]`

Relance les dés dont la valeur respecte la condition du Validateur, et
remplace l\'ancienne valeur par la nouvelle. La comparaison avec la
condition est faite qu\'avec la valeur initiale du dés (Plus de détails
sur les conditions dans la partie sur les Validateur). Exemple: Vous
lancez 3D10r\[\>7\], vous obtenez : \[4,8,10\], l\'opérateur r rentre en
jeu pour remplacer les valeurs 8 et 10. Nous obtenons: \[2,9\], le
résultat final du lancer sera: \[4,2,9\]

### Explose

`   3D10e[Validateur]`

Relance les dés dont la valeur respecte la condition du Validateur. La
nouvelle valeur s\'ajoute à l\'ancienne valeur et cela boucle tant que
la nouvelle valeur respecte la condition (Plus de détails sur les
conditions dans la partie sur les Validateur). Exemple: Vous lancez
3D10e\[\>7\], vous obtenez : \[4,8,10\], l\'opérateur r rentre en jeu
pour faire exploser les valeurs 8 et 10. Nous obtenons: \[2,9\], puis
encore \[3\] le résultat final du lancer sera: \[4, 10 \[8,2\], 22
\[10,9,3\] \]

### Ajout

`3D10a[Validateur]`

Relance les dés dont la valeur respecte la condition du Validateur. La
nouvelle valeur s\'ajoute à l\'ancienne valeur. La comparaison avec la
condition est faite qu\'avec la valeur initiale du dés (Plus de détails
sur les conditions dans la partie sur les Validateur). Exemple: Vous
lancez 3D10e\[\>7\], vous obtenez : \[4,8,10\], l\'opérateur a rentre en
jeu pour relancer et ajouter les dés ayant les valeurs 8 et 10. Nous
obtenons: \[2,9\]. Le résultat final du lancer sera: \[4, 10 \[8,2\], 19
\[10,9\] \].

### Saut arrière

`8D10c[>=7]+@c[=10]`

Cette opérateur permet d\'obtenir le résultat avant le dernier
opérateur. Il est tres utiles si vous souhaitez compter deux éléments
différents dans un même lancer de dés. Cette commande permet de compter
les des supérieurs à 7 et les dés valants dix rajouter un. Les 10
comptent doubles (système exalted v2).

### Filtre

`6d6e6f[!=4]`

Lance 6 dés à 6 faces, les dés explosent sur un 6 mais les 4 sont
ignorés.

L\'opérateur F permet de filtrer un résultat pour sélection des valeurs
ou en éliminer.

### Rassembler

`2d6;2d4mk1 `

Lance 2 dés à 6 faces, lance également 2 dés à 4 faces. Les deux
résultats sont rassemblés en un seul et donnés à l\'opérateur k qui
garde le meilleur des 4 dés. Cet opérateur unit différents résultats de
dés en un seul. Quelque soit le type de dés utilisé.

### Séparer

`1d10e[>8]uf[!=9]c[>7]`

Lance 1 dés à 10 faces, il explose pour 8 ou plus. Les 9 sont filtrés et
supprimer du résultat. En toute fin, le systeme compte le nombre de dés
supérieurs à 7 (mais les 9 ne sont pas dans le résultat). C\'est un peu
l\'inverse du rassembler (m). Il permet de séparer les différentes
valeurs d\'un dés explosé pour mieux traiter chaque valeur.

### Si

L\'opérateur Si (if) vous permets de déclencher une action quand une
condition est remplie. Il possède deux paramètres obligatoires:

-   La condition de test (le validateur)
-   L\'instruction a exécuté quand la condition est remplie.

Il y a également deux paramètres facultatifs:

-   La méthode de comparaison
-   L\'instruction a exécuté quand la condition n\'est pas remplie.

`Syntaxe: i*[]{}{}`

-   \* : La méthode de comparaison
-   \[\] : La condition
-   {} : Instruction quand la condition est remplie
-   {} : Instruction quand la condition n\'est pas remplie

#### Les méthodes de comparaison:

Il en existe 3:

-   Chaque : Cette méthode est la méthode par défaut, pour l\'utiliser,
    il suffit de ne mettre aucun paramètre à la méthode. La condition
    est testé sur chaque dé de résultat du noeud précédent.
    L\'instruction sera exécutée pour chaque dés remplissant la
    condition. L\'instruction \"fausse\" sera exécutée pour chaque dé
    incorrect. \[Méthode par défaut\]
-   Tous : Tous les dés du résultat du nœud précédent doivent remplir la
    condition pour valider la condition. Les instructions pour la
    condition remplie ou non ne sont exécuté qu\'une fois.
-   Au moins un : Si un ou plusieurs dés remplissent la condition alors
    l\'instruction vrai est exécutée. Si aucun dé ne remplit la
    condition alors l\'instruction fausse est exécutée.

Pour activer la méthode **Tous**, vous devez ajouter le paramètre **\***
à l\'emplacement du paramètres. Pour activer la méthode **Au moins un**,
vous devez ajouter le paramètre **.** à l\'emplacement du paramètres.

#### Exemples:

`1d6i[<4]{3}`

Si la valeur du dé est inférieure à 4 alors, la valeur du dés devient 3.
(Donc 1, 2 et 3 se transforme en 3).

`4d6e6i[=4]{-4}`

Pour chaque dé égal à 4, nous soustrayons 4 du résultat. \[Kuro System\]

`4d6i.[=6]{+1d6}`

Si un dés au moins est égal à 6 alors nous lançons un nouveau d6 et nous
ajoutons son résultat.

`4d6i*[=6]{+1d6}`

Si tous les dés sont égaux à 6 alors nous lançons un nouveau d6 et nous
ajoutons son résultat.

#### Afficher un message

Il est possible d\'afficher un texte grâce à l\'opérateur Si. Dans ce
texte, il vous est possible d\'afficher le résultat total RT et la liste
des valeurs des dés (LR).

RT est positionné dans la chaîne de sortie par %1. LR est positionné
dans la chaîne de sortie par %2.

Si vous ne lancez qu\'un dé, RT et LR sont égaux.

#### Exemples

`1d100i[<30]{"Réussite: %1"}`

Affichera \"Réussite 29\"

`1d100i[<30]{"Réussite: %1"}{"Echec %1"}`

Affichera \"Réussite 29\" ou \"Echec 55\"

`1d100i[<30]{i[<6]{"Réussite Critique: %1"}{"Réussite %1"}}{"Echec %1"}`

Affichera \"Réussite Critique 3\", \"Réussite 29\" ou \"Echec 55\"

`5d100i.[<30]{"Réussite: %1 [%2]"}`

Affichera \"Réussite 230 \[90,26,54,45,15\]\"

### Paint

C\'est opérateur permet de peindre un ou plusieurs dés dans un lancer.

`6D10e10p[1:blue,2:red]`

Cette commande lance 6 dés à 10 faces. Ils explosent sur un 10. Le
premier dés est peint en bleu et les deux suivants (le 2ème et 3ème) en
rouge.

Il est possible de définir une couleur par son nom (voir liste des noms
acceptés ici: <https://www.w3.org/TR/SVG/types.html#ColorKeywords> ) Il
est également possible de donner les valeurs de la couleur avec la
notation html (\#RRGGBB: plus d\'info sur
<http://doc.qt.io/qt-5/qcolor.html#setNamedColor>)

Arithmétique
------------

Le systeme de dés de rolisteam est capable de calculer des expressions
avec les opérateurs principaux de l\'arithmétique: +, -, /, \*. Il est
aussi capable de gérer la priorité de ces opérateurs ou bien encore, les
parenthèses.

`   8+8+8`

Resultat: 24

`   24-4`

Resultat: 20

`   (3+4)*2`

Resultat: 14

`   7/2`

Resultat: 3.5

### Arithmétique et les dés

Il est possible d\'utiliser les opérateurs arithmétiques avec les dés.
Il faut bien comprendre qu\'un résultat de plusieurs dés formes une
liste de nombre; pas un nombre. Donc, quand vous lancez 3d6, le resultat
sera une liste de trois valeurs: \[2,5,1\]. Maintenant, nous souhaitons
l\'utiliser avec un opérateur arithmétique: 3d6+4. Cela résolut comme
ceci: \[2,5,1\]=8; 8+4=12; Le résultat final sera donc 12.

#### série d\'exemples

`   3d6+4`

Lance 3 dés à 6 faces; Somme les résultats et ajoute 4.

`   10D10-2`

Lance 10 dés à 10 faces; Somme les résultats et soustrait 2.

`   87-1D20`

Soustrait le résultat d\'un dés à 20 faces à 87.

`   (6-4)D10`

Soustrait 4 à 6, et lance deux dés à 10 faces.

`(3+2D6)D10`

Lance 2 dés à six faces et ajoute le résultat à 3. La somme résultante
détermine le nombre de dés à 10 faces qui sera lancés.

`   1D10/2`

Divise par deux le résultat d\'un dés à 20 faces.

### Lancer plusieurs dés différents en même temps

Vous devez séparez vos différentes commandes par un point-virgule (;):

`   1d10;1d6`

ou

`   5d6;1d10;4d100;3d20`

C\'est très équivalent à 1d10+1d6 ou 5d6+1d10+4d100+3d20, en interne, il
ne se passe pas les mêmes choses mais pour présenter la sortie,
Rolisteam fait la sommes des dés.

### Validateur

Il y a trois types de validateur: -Les expressions logiques, les
numériques et les intervalles.

Tout opérateur qui nécessite un validateur (\'a,r,e,c\') peut utiliser
les trois types.

### Les expressions logiques

Une expression logique est encadrée par des crochets \[\], et elle
contient un opérateur et une valeur. Exemple:

`   4d10c[>7]`

Lance 4 dés à 10 faces et compte le nombre de dés qui dépassent 7.

#### Les opérateurs logiques

The Rolisteam Dice Parser allows you to use several logic operator:
Rolisteam supporte tous les opérateurs suivants:

`   Egal : =`\
`   Supérieur ou égal : >=`\
`   Inférieur ou égal : <=`\
`   Inférieur : <`\
`   Supérieur : >`

### Le Validateur Numerique

Il suffit de mettre juste après l\'opérateur, un nombre. L\'opérateur
s\'activera pour les dés dont la valeur est égale à ce nombre.

`   4d10e10`

Lance 4 dés à 10 faces et les dés exploses sur les 10. C\'est
strictement équivalent à

`   4d10e[=10]`

### Intervalle

Un intervalle est définie par deux nombres séparer par un tirer \'-\'.
Le tout est encadre par des crochets \[\]. Exemple:

`   4d10c[8-10]`

### Série d\'exemples pour les opérateurs

Série d\'exemples
-----------------

`   3D100`

Roll 3 dice with 100 faces

`   10D10e[=10]s`

Roll 10 dice with 10 faces, 10 exploses, and sort the result.

`   100291D66666666s`

Roll 100291 dice with 66666666666 faces and sort result

`   15D10c[>7]`

roll 15 dice with 10 faces and it counts number of dice which are above
7

`   1D8+2D6+7`

roll 1 die with 8 faces and add the result to 2 dice with 6 faces and
add 7.

`   D25`

roll 1 die with 25 faces

`   88-1D20`

88 minus the value of 1 die of 20 faces

`   8+8+8`

compute: 24

`   1L[sword,bow,knife,gun,shotgun]`

One of this word will be picked.

`   8D10c[Validator1]-@c[validator2]`

Roll 8 dice with 10 faces then it counts how many dice respect the
condition Validator1 and substract the number of dice which respect the
validator2 and display the number (See Validator for more details about
syntax)

`   8D10c[>=6]-@c[=1]`

Old World in darkness system.

`   8D10c[>=7]+@c[=10]`

Exalted 2nd edition system.

Ancienne Version
================

Il est aussi possible de lancer les dés dans un tchat en entrant des
messages particuliers dans la zone de saisie. Actuellement, il existe 2
systèmes de jet de dés.

### Système généraliste

Tapez un point d\'exclamation suivi d\'expressions du genre 2d6 et de
nombres qui s\'ajoutent ou se soustraient. Quelques exemples :

` !5d6`\
` !1d6-1d6`\
` !3d6+1`

Ces expressions peuvent se combiner avec les précédentes. Par exemple :

` !3g2 + 1d6 - 1`

Il est aussi possible de cacher le jet en remplaçant le point
d\'exclamation par une esperluette . Dans ce cas le jet de dés n\'est
visible que par le joueur qui l\'a fait. Il n\'est pas communiqué aux
autres joueurs.

### Système pour ShadowRun 4

-   Tapez un astérisque suivi du nombre de dés suivi de la lettre d.
-   Pour *rusher* ajoutez la lettre r.
-   Pour les *gremlins* ajoutez la lettre g suivie de l\'indice.
-   Pour relancer les 6 ajoutez un symbole plus.
-   Pour ne pas afficher les détails du lancé ajoutez la lettre c.
-   Pour n\'afficher que le résultat du jet ajoutez la lettre s.

Exemples :

` *8d`\
` *8drg3`\
` *12d+s`

### Système pour L5R / L5A

-   L\'opérateur g est utilisé. En minuscule, vous ne relancez pas
    les 10. Avec G majuscule, vous relancez les dix. Le résultat est
    trié pour une meilleure lecture.
-   Vous pouvez ajouter une valeur comme n\'importe quel jet.

Exemples:

` !3g2`\
` !7G4`\
` !7G4+5`
