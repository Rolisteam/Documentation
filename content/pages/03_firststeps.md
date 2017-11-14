Title: First steps
Date: 2017-06-11 10:20
slug: firststeps
status: hidden
lang: en
 
## Tutorials

As an introduction of what rolisteam can do and how to use rolisteam, this tutorial should answer many of your questions.

*   [Let's get started](http://www.rolisteam.org/tutorial01.html)

## Step 0 : Decide who should host the game

To select the best candidate for hosting, please keep in mind these points:

* Good network bandwidth
* Stable Pc (Linux is best :-p)
* Reliable Person

## Step 1 : Start **Rolisteam**

![images]({filename}connection_panel_en.png)

## Step 2 : Host the game

At the beginning of all games played with rolisteam, there is always someone who start rolisteam to host the game.

### Configure Rolisteam to host

It is really simple. Start rolisteam and make sure the checkbox `Host the game` is checked. Then, click on `Ok`. 

Then, Rolisteam may accepts other players to join. In the notification panel, **Rolisteam** gives you all informations required to join your game. Your players must have those information. 

But before that, you may want to test your connection.
We developed a [little tool](http://www.rolisteam.org/php/test_ip.php) to test if your network let incomming connections reach the host.

Set the ip address and port on the webpage and click on `Test`.

The response should be *Good News ! Connection succeed!*. Any other response means it does not work.

### Configure your local network

The most frequent cause about connection issue is the separation between your local network and the internet.
In this case, the device on the internet is not your computer but it's your network device (modem/router/...).
So the incoming connection reaches your network device but it does not know what to do with it.
We have to set a rule to forward incoming connection to your computer. But at First, we must be sure your computer has always the same address inside your local network.

#### Fixed Ip address

I can't give you details about that because it changes given your network device or ISP.
On the network device configuration page, you must look for **dhcp**, **local network rule** or **Lan**.

To make sure it works, unplug and replug your computer several times or restart it and check that the local ip address does not change.

#### Forwarding Connection

The configuration steps are highly dependent of your network device.  
The goal here is to define a rule. This rule says: "when an incoming connection using the port 6660 reaches you (network device). Please forward it to my computer (ip local)".

Test your connection with the tool described ealier in this document. When the connection works, you should give information to the other players.

## step 3 : Fulfill the Profile

Connection profiles are dedicated to save all connection information (such as Hosting or join the game, GM or player, character, avatar ).
When all the data are set. You may start to play.

## Step 4 : Join game

There is no specific task to do to join game. Set the appropriate value to address and port and it just works.



## Technical explaination

**Rolisteam** is based on a host/client architecture. 
It mean that a user have to be the host and all other will be client that connect themselves to host. 
Host computer relay information of clients: when a client send data (messages, plans, images or music request for the GM), it send them to host, and the host next send them to all other clients.

So host is the only one which has direct contact with all users.

In facts, at startup, you need to decide with other users who will be the host.

When the host is started, other users (clients) can connect themselves to host and the game can begin.

if the host leaves, the game ends for every players. 

## Network configuration


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

More information about hosting the game are available on these pages [How to host]({filename}25_hosting.md) and [Network]({filename}26_network.md).

-   Check the *Host the game*.
-   You may change the port but be aware than you must configure your
    network according to this port.

Rolisteam displays the network address at the connection. 
The public address which must be communicated to your players.
