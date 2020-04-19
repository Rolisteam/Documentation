Title: First Connection
Date: 2017-06-11 10:20
slug: firststeps
status: hidden
lang: fr


## Tutoriaux

Une bonne introduction pour débuter avec Rolisteam se trouve dans ce tutoriel, il présente l'ensemble des tâches à faire:

*   [Tutoriel # 1](http://www.rolisteam.org/tutorial01.html)


# Rassembler

Pour jouer avec vos amis sur **Rolisteam**, tous les participants doivent rejoindre la table virtuelle.
Il y a 2 moyens de le faire:
* Rejoindre un serveur **Rolisteam**
* Héberger une partie.

## Rejoindre un serveur

Vous pouvez rejoindre une partie hébergée par un autre de vos joueurs ou un serveur offert par une communauté. En effet, il est possible pour une communauté d'installer un serveur Rolisteam et de le rendre accessible pour ses membres. À l'image de ce qui se fait dans les jeux vidéos.
Vous pouvez jeter un coup d'œil à la page [liste des serveurs](http://www.rolisteam.org/serverList.html) pour trouver des informations sur les communautés qui proposent ce service.
Contactez-nous pour faire apparaitre la vôtre dans cette liste.

Si vous voulez installer le serveur Rolisteam pour votre communauté, vous trouverez [des instructions ici]({filename}02_1_server.md)

## Héberger la partie directement

Une partie peut être hébergée sur n'importe quelle machine.
Il suffit de suivre ces quelques étapes.

Attention: Si votre connexion internet repose sur des technologies mobiles (4G…), il vous sera probablement impossible d'héberger une partie.

### Étape 0 : Décider qui doit héberger la partie

Pour sélectionner le meilleur candidat pour l'hébergement, il convient de garder à l'esprit ces quelques points:

* Une bonne connexion internet
* Un ordinateur stable (éviter le wifi dans la mesure du possible)
* Une personne de confiance

### Étape 1 : démarrer **Rolisteam**

![images]({static}/images/en/connection_dialog.jpg)

### Étape 2 :Héberger la partie

Remplissez le nom du profil, votre nom, et choisissez une couleur.  
Sélectionner un port de connexion (défaut: 6660)
Assurez-vous que la case `héberger la partie` soit cochée.
Ajoutez un mot de passe, si vous en sentez le besoin.
Puis cliquer sur `Ok`.


Une fois, cette étape terminée, **Rolisteam** est entièrement accessible pour vous, il convient de permettre aux autres joueurs de se connecter à la partie. Dans le panneau de notification, **Rolisteam** vous affiche les informations importantes à communiquer pour vous rejoindre.
Les autres joueurs doivent avoir ces informations (l'adresse IP, le port et le mot de passe éventuel).

### Étape 3 : Test de  connexion

Nous recommandons fortement de faire des tests de connexion avant la première partie.
En conséquence, nous avons créée ce [test de connexion](http://www.rolisteam.org/php/test_ip.php). Il vous permettra de savoir si votre Rolisteam est joignable depuis l'extérieur de chez vous..

Ajoutez l'adresse IP et le port dans le formulaire puis cliquez sur `Test`.

Si la réponse est **Good News ! Connection succeed!**, félicitation vous pouvez passer à l'étape suivante.  
Toute autre réponse signifie que vous n'avez pas configuré votre installation de façon adéquate.

#### La connexion échoue ? Pas de panique

La cause la plus fréquente est dans cette situation est l'absence de configuration au niveau de votre routeur.
Pour vous expliquer, votre modem/routeur est sur internet et votre ordinateur a accès à internet, car votre routeur vous laisse passer.
En effet, les routeurs acceptent les connexions sortantes sans soucis, mais il s'agit d'une autre histoire quand il doit accepter les connexions rentrantes.
Dans ce cas, il convint de définir 2 règles simples sur votre routeur pour garantir la connexion.
Nous devons nous assurer que l'ordinateur hébergeant Rolisteam ait toujours la même adresse IP locale, puis nous allons dire au routeur de rediriger les connexions entrantes sur le port de Rolisteam vers cet ordinateur.

Cette configuration doit être faite une seule fois.  Si cela a marché une fois, cela continuera à marcher tant que la mémoire de votre routeur n'est pas effacée ou que vous changiez de routeur.

#### Avoir une IP locale fixe

Les étapes précises dépendent fortement de votre matériel et/ou de votre fournisseur d'accès à internet.
Sur l'espace de configuration de votre routeur, chercher les mots-clés: **dhcp**, **local network rule** or **Lan**.
Faites en sorte que votre ordinateur ait toujours la même IP locale (généralement cela ressemble à  192.168.0.XXX ou 192.168.1.XXX)

N'hésitez pas à chercher sur internet comment faire en spécifiant le nom de votre routeur/modem/box.

Pour vous assurer que cela fonctionne, vous pouvez débrancher et rebrancher le réseau de votre machine et vérifier ensuite dans le paramètre réseau sur votre ordinateur que vous avez bien la même IP locale.

#### Redirection de port

Cette étape de configuration dépend très fortement de votre matériel réseau.
Le but ici est de définir une règle qui dit: «Quand une connexion arrive sur le port 6660, peux-tu la transférer vers l'ordinateur ayant l'adresse IP locale suivante … (voir étape précédente)»

Maintenant, vous pouvez retester votre configuration en essayant l'outil décrit plus haut dans ce document.
Quand la connexion fonctionne, vous pouvez donner ces informations aux autres joueurs.

# Rejoindre une partie distante

Votre groupe a une solution fonctionnelle pour héberger la partie.
Les autres joueurs souhaitent vous rejoindre.
Assurez-vous d'avoir l'ensemble des informations nécessaires.

* L'IP public de connexion (ou un nom de domaine)
* Le numéro de port
* Le mot de passe (si besoin)

## Étape 4  : Rejoindre la partie

* Démarrer **Rolisteam**
* Remplir un profil avec les informations suivantes: le nom du profil, le nom du joueur, la couleur du joueur, le nom du personnage, la couleur du personnage, l'avatar du personnage (de préférence une image carrée), puis l'adresse de connexion, le port et le mot de passe.
* Assurez-vous que la case ```MJ``` reflète votre rôle dans la partie à venir.
* Assurez-vous que la case ```héberger la partie``` ne soit pas cochée.
* Puis cliquer sur ```Ok```

Le sélecteur de profils disparaît quand la connexion est établie.

**Félicitation! Bonne partie!**

## Prise en main individuelle

Nous recommandons fortement de tester **Rolisteam** tranquillement avant de vous lancer dans une partie.
Pour le tester, démarrer Rolisteam deux fois et sur le premier, sélectionnez un profil MJ et hébergeur.
Sur le second, définissez l'adresse de connexion sur **localhost** et connectez-vous en client/joueur.

Ainsi, vous pourrez voir les 2 aspects de la partie: côté MJ et côté joueur.


<p style="text-align: left; width:49%; display: inline-block;"><a href="/fr/install.html">Précédent</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/fr/explanation.html">Suivant</a></p>
