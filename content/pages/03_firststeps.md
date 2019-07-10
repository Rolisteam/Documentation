Title: First Connection 
Date: 2017-06-11 10:20
slug: firststeps
status: hidden
lang: en


## Tutorials

As an introduction of what rolisteam can do and how to use rolisteam, this tutorial should answer many of your questions.

*   [Let's get started](http://www.rolisteam.org/tutorial01.html)


# The gathering

To play together with **Rolisteam**. All participants must join the same virtual place.
There are two ways to do so:

* Online rolisteam server.
* Host the game.

## Join online server

Player/RPG communities can now install rolisteam server on remote server. Just like any video game server.
Please go to the [server list](http://www.rolisteam.org/serverList.html) to know online servers. Not all of them are listed there.
[Contact us]({filename}26_contactUs.md) to add your server to the list.

If you want to install rolisteam server for your community, find [instruction here]({filename}02_1_server.md)

## Host the game

Game can be hosted with rolisteam on any computer.
Please follow these step.

### Step 0 : Decide who should host the game

To select the best candidate for hosting, please keep in mind these points:

* Good network bandwidth
* Stable computer
* Reliable Person

### Step 1 : Start **Rolisteam**

![images]({static}/images/en/connection_dialog.jpg)

### Step 2 : Make profile

1. Fill up your name, select a color.  
2. Select a port (default: 6660)  
3. Ensure the `host the game` checkbox is checked.  
4. Define a password if you want of let it blank.  
5. Then, click on `Ok`.  

The address field becomes disable when `host the game` is checked.

[more details]({filename}03_firststeps.md) about Connection profile

The profile selection dialog disappears and then, Rolisteam is waiting for other players to join. In the notification panel, **Rolisteam** gives you all informations required to join your game. Players must have those information ( ip address to join and port).  
Don't forget to give them the password as well.

### Step 3 : Connectivity test

We strongly recommand to test the connection before your first game.
So we developed a [connection test](http://www.rolisteam.org/php/test_ip.php) to know if your network let incomming connections reach **Rolisteam**.

Set the ip address and port on the webpage and click on `Test`.

The response should be **Good News ! Connection succeed!**.  
Any other response means it does not work.

#### Connection failed ? don't worry

The most frequent cause about connection issue is the separation between your local network and the internet.  
In this case, the device on the internet is not your computer but it's your network device (modem/router/...).  
So the incoming connection reaches your network device but it does not know what to do with it.  

Settings rule to forward incoming connection to your computer fixes it. But at First, we must be sure your computer has always the same address inside your local network.

The configuration must be made once. When it had worked it should work until you change your network device or erase its memory.

There are plenty of tutorials online, just search for **port forwarding** and the name of your **ISP**.

#### Fixed Ip address

The process here is highly network device dependent or ISP dependent.  
On the network device configuration page, you must look for **dhcp**, **local network rule** or **Lan**.
Set your computer to have always the same local Ip address (commonly 192.168.0.XXX or 192.168.1.XXX)

To make sure it works, unplug and replug your computer several times or restart it and check that the local ip address does not change.

#### Forwarding Connection

This configuration steps are highly dependent of your network device.  
The goal here is to define a rule. This rule says: "when an incoming connection using the port 6660 reaches you (network device). Please forward it to my computer's ip local address (previous step)".

Test your connection with the tool described ealier in this document. 
When the connection works, you should give information to the other players.

# Join remote game

Your group has a working solution to host the game.
So players must join. 
Ensure you have all needed data.
-Connection address (or hostname)
-Port number
-Password (if necessary)

## Step  : Join game

* Start **Rolisteam**
* fulfill your profile: player Name, player color, character name, character color, character avatar (square image are better), connection adress, port and password.
* Ensure the ```GM``` checkbox state is revelent to your role in the game to come.
* Ensure ```host the game``` is not checked
* then click on ```Ok```

The connection dialog disappears when is connection with the server is set.

**Congratulations!! Game on!**

## Test alone 

It is strongly recommended to test **Rolisteam** before playing with it. 
To test it, start rolisteam twice and on the first one, select an hosting profile (GM/Host).
On the second, set address to **localhost** and connect as client/Player.

Now, you can play around with **Rolisteam** and see how it will appears to your player's screens.


<p style="text-align: left; width:49%; display: inline-block;"><a href="/install.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/explanation.html">Next</a></p>
