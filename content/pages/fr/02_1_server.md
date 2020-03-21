Title: Roliserver
Date: 2017-06-11 10:20
slug: roliserver
status: hidden
lang: fr

## Explication

Roliserver est un serveur conçu pour héberger plusieurs parties de **Rolisteam** en même temps, grâce à un systeme de canaux (salons).
Ainsi, il est possible d'offrir ce service à votre communauté.

Cette page explique comment configurer le **Roliserver**.

## Premier lancement

Nous recommendons de lancer le serveur une première fois, afin de générer un fichier de configuration propre:

`roliserver -p config.conf`

Le fichier généré s'appelle `config.conf`. Vous pouvez changer le nom si vous le souhaitez.

    :::ini
    [General]
    AdminPassword=@Invalid()
    ChannelCount=@Invalid()
    ConnectionMax=@Invalid()  
    IpBan=@Invalid()
    IpMode=@Invalid()
    IpRange=@Invalid()
    LogLevel=@Invalid()
    DeepInspectionLog=@Invalid()
    ThreadCount=@Invalid()
    TimeEnd=@Invalid()
    TimeStart=@Invalid()
    TimeToRetry=@Invalid()
    password=@Invalid()
    port=@Invalid()
    TryCount=@Invalid()
    MaxMemorySize=@Invalid()


Il convient ensuite de modifier ce fichier en fonction de vos besoins.
L'ordre des éléments n'est pas important et peut changer entre la version générée et l'exemple ci-dessus.

## Les champs

### Password

Le champ `password` permet de définir le mot de passe d'accès au serveur.
Ce mot de passe doit être transmit à toutes les personnes souhaitant se connecter à votre serveur.
Pour des raisons de sécurité, le mot de passe n'est pas conservé "en clair". Il est chiffré en utilisant la méthode: **Sha3_512**.
Pour convertir votre mot de passe, il existe deux méthodes. **Rolisteam** offre un panneau dans le menu **Réseau** qui permet de faire cette conversion.
Sinon vous pouvez appeler le serveur en ligne de commande avec le paramètre `-g`.

`$ roliserver -g`

Si vous saisissez `0000` comme mot de passe. Le serveur doit vous donner: 

> tnjOmGIvYntbNcoej2VvG9M1RdJCtZ8BWjHek4r6OvvmhThbjjzJ/zfYwq+G7r/TGe7WWr20vkGBzULuTzcPYQ==

(**Attention**: Si ce n'est pas la cas, cela signifie que le serveur tourne avec une ancienne version de Qt)

En suite, il suffit de copier/coller cette clé dans votre fichier de configuration.

### Port

Définit le port tcp de connexion, Par défaut le port est le 6660 mais vous pouvez le changer.

### ConnectionMax

Définit la capacité maximume du serveur en personnes connectées.

### ChannelCount

Définit le nombre de canaux. Cela signifie que cela définit également le nombre de parties simultanées possibles sur votre serveur.

### Admin Password

Définit le mot de passe pour s'authentifier en tant qu'administrateur du serveur.
Il convient de générer un mot de passe en **Sha3_512** (comme expliqué dans la section **password**.

L'administrateur peut expulser un joueur, ajouter/détruire un canal etc...

### LogLevel

Le niveau de log définit le niveau d'information que vous souhaitez rendre visible dans le fichier de log. La valeur est un nombre.

Valeurs possibles:

* 1 : Error
* 2 : debug
* 3 : Warning
* 4 : Information

En *Error*, le serveur ne préviendra qu'en cas d'erreur.  
En *debug*, il affichera des versions utiles si vous souhaitez modifier le code du serveur. 
En *Warning*, le serveur prévient en cas de données étranges et de comportements inattendus.  
En *Information*, le serveur donne autant de détails qu'il peut.

Si vous constatez un problème et que vous souhaitez prévenir l'équipe. Il est conseilé de venir avec un fichier de log en information.

### DeepInspectionLog

Active les logs profonds du serveur.
Attention, cette option peut ralentir grandement les performences du serveur.

Valeurs possibles:

* true
* false

(true => vrai et false => faux)

### LogFile

Définit le chemin du fichier de log.

**Exemple**
> LogFile=/var/log/roliserver.log



### ThreadCount

Définit le nombre maximum de thread utilisable par le serveur.

### TimeToRetry

Au démarrage, le serveur se mets en mode "écoute" sur le port défini. Si cela échoue, le serveur réessaie plusieurs fois avant de s'arrêter en erreur. Le temps définit ici est le temps à attendre avant un nouvel essai.

### TryCount

Définit le nombre d'essais d'écoute du port avant de sortir en échec.
Sortir signifie que le serveur s'arrête.

### TimeStart

L'heure à partir de laquelle, les connexions sont acceptées.

Le format: hh:mm
Les heures et les minutes doivent être écrites sur deux chiffres.

Exemples:

> 20:00

(20h)


> 06:00

(6h)

### TimeEnd

Le temps de fin d'acceptation des connexions.

Exemples:

> 20:00
(20h)


> 06:00
(6h)

### IpBan

Si vous souhaitez banir une ou plusieurs adresses IP. Il suffit de les ajouter dans ce champs.

Exemples:
Ici, nous avons 3 adresses banies.

> 80.80.80.80,127.9.9.1,10.10.10.10


### IpMode

Ce champs n'est pas encore utilisé.

### MaxMemorySize

Le serveur garde en mémoire beaucoup d'information quand une partie à lieu pour accélérer la reprise du jeu en cas de déconnexion ou autre. 
Cette fonctionnalité demande beaucoup de mémoire. 
Nous ponvons demander au serveur de vider sa mémoire si cela devient trop gros.

Exemple:

    :::ini
    MaxMemorySize=8G  #Define the size at 8 Gibibyte
    MaxMemorySize=8M  #Define the size at 8 Mebibyte
    
### Exemple d'un fichier complet:

<pre>
AdminPassword=tnjOmGIvYntbNcoej2VvG9M1RdJCtZ8BWjHek4r6OvvmhThbjjzJ/zfYwq+G7r/TGe7WWr20vkGBzULuTzcPYQ==
ChannelCount=8
ConnectionMax=50
IpBan=@Invalid()
IpMode=@Invalid()
IpRange=@Invalid()
LogLevel=3
LogFile=
ServerPassword=tnjOmGIvYntbNcoej2VvG9M1RdJCtZ8BWjHek4r6OvvmhThbjjzJ/zfYwq+G7r/TGe7WWr20vkGBzULuTzcPYQ==
ThreadCount=8
TimeEnd=@Invalid()
TimeStart=@Invalid()
TimeToRetry=100
TryCount=10
port=6660
</pre>

Quand votre fichier de configuration est près, vous pouvez le tester en lancant:

```
roliserver -c config.conf
```
Vous pouvez essayer de vous connecter à votre serveur.
Si tout s'est bien passé, nous pouvons passer à l'étape suivante: Le lancement automatique. 

## Créez un service SystemD

Il faut créer un fichier de service systemd.

```
$ sudo touch /etc/systemd/system/roliserver.service
```

Puis vous pouvez ajouter ce contenu dans le fichier roliserver.service:
    
    :::ini
    [Unit]
    Description=Rolisteam Server
    After=network.target
    StartLimitIntervalSec=0
    
    [Service]
    Type=simple
    Restart=always
    RestartSec=1
    User=#your_username#
    ExecStart=/usr/local/bin/roliserver -c /home/#your_username#/.roliserver.conf
    
    [Install]
    WantedBy=multi-user.target

Les dernières étapes consistent à activer le service et à la démarrer. 

    :::shell
    $ sudo systemctl enable roliserver.service
    $ sudo systemctl start roliserver.service


## Deployer avec Docker



## Le cas Windows
