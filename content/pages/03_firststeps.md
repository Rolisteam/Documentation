---
title: En:First steps
permalink: /En:First_steps/
---

How this work
=============

[Rolisteam](/Rolisteam "wikilink") is based on a host/client
architecture. It mean that a user have to be the host and all other will
be client that connect themselves to host. Host computer relay
information of clients: when a client send data (messages, plans, images
or music request for the GM), it send them to host, and the host next
send them to all other clients.

So host is the only one which has direct contact with all users.

In facts, at startup, you need to decide with other users who will be
the host.

When the host is started, other users (clients) can connect themselves
to host and the game can begin.

when the game is started, there is no differences between host and
clients, except that if host leave, the game end automatically. The host
choice should be determined by some considerations like:

Technique
---------

-   Is the computer stable, or did he have the bad habit to reboot every
    time?
-   Is the connection good? ([Rolisteam](/Rolisteam "wikilink") is not
    very greedy in bandwidth, but if you transfer many big images, or if
    you have many players, maybe a poor connection will hang transfers)
-   In general, it is a good thing that the host have a good upload rate
    (you can find many sites who offers such measurement, just try to
    make a research with "test upload" in your favorite web search
    engine);

Personal
--------

-   Is the host user have the "midnight permission" or his girlfriend
    (maybe it's her boyfriend I don't know) allow him (her?) to play
    more?
-   Is the player is "awkward", and could terminate the program if his
    character die?
-   After few tries, I have no doubt that you'll find the ideal host
    between your friends' and players' computers.

Network configuration
---------------------

There are two kind of connection in rolisteam: **Client** and
**server**.

To play with rolisteam, one person must be the server and the others
must start rolisteam as client. Client user must connect to the server.

### Clients

There is no specific configuration.

### Server

The server mode may require some settings to work perfectly.

Basically There are two ways for your computer to get online.

1.  your computer has modem connected to the Internet.
2.  your computer is in a home network which has access to internet
    through a bridge or router.

#### Direct Connection (case 1)

In this case, the only thing which can provide clients to connect to
your server may be firewall on your computer. You must allow "in
connection" through the rolisteam port (Default 6660).

#### Local network connected to the Internet (case 2)

This case may require several configuration steps. You must configure
your router to forward connections to your computer (which host
rolisteam as server) with the expected port.

You may find on the internet many How-Tos to do it. The keyword are :
-**Open Port (tcp)** -Model of your network equipment

#### Requirements

-   IP address of your machine (the local one: 192.X.X.XXX)
-   The port number for rolisteam (defaut: 6660).
-   The connection type: TCP.

Be careful, if you change the port number in rolisteam this rule will
not work any more and no body will be able to reach your server.

First launch
------------

[right\|border](/File:Connexion.png "wikilink")

### Players (and Game Master)

-   Start Rolisteam and type your name (can be changed on the fly in the
    game).
-   Change your color (can be changed on the fly in the game).
-   If you are the GameMaster, check the given checkbox. There is only
    one MJ by game.

### Cient Connection

-   Make sure the **Host the game** checkbox is unchecked.
-   Type the server address: ip adresses and host name are supported
    (80.80.80.80 or rolisteam.org)
-   Change port according to your server configuration (default: 6660)

### Server Mode

If you want to host the game, please pay attention to this page [How it
works](/How_it_works "wikilink") et [Network
file](/Network_file "wikilink").

-   Check the *Host the game*.
-   You may change the port but be aware than you must configure your
    network according to this port.

Rolisteam displays the network address at the connection. The public
address which must be communicated to your players. You may also visit
[this page](http://whatismyipaddress.com/fr/mon-ip).