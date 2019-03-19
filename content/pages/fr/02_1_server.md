Title: Roliserver
Date: 2017-06-11 10:20
slug: roliserver
status: hidden
lang: fr

## Overview

Roliserver is dedicated to host several games on the same computer.
RPG players communities may offer this service to their users.

## First run

We strongly recommend to start roliserver as follow:

`roliserver -p config.conf`

It generates an empty configuration file named "config.conf" (change the name if you want).

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


Change value accordingly to your needs.
The order of element is not important.

## Configuration file

### Password

Define password to access the server.
Every password stored in this file must be encrypted with **Sha3_512** method.
Don't worry, it is really easy to do.

first, start the server with -g parameter.

`$ roliserver -g`

It asks you to type the password.
Then it prints the encrypted version of your password.

> P9d63VIxEvincVCutARz0W86GFFX36h0zWEIUomzusZmnv3krtcEsXzZWKKXXv6Ivag+8fR2a7tRWoaaIu3L1w==

Then you can copy/paste this key into your file.

Rolisteam offers graphical tool to get generate password with **Sha3_512**.

**Warning** : be sure, you run the server with Qt5.9 or higher. **Sha3_512** on older version of Qt does not work correctly. You may have difficulties to connect to the server.

### Port

Define connection port, Usual port is 6660 but it can be changed.

### ConnectionMax

Define the maximum number of clients that the server allows.

### ChannelCount

Define the number of channels at the first start of the server.  
Basically, that defines the number of games your server can accept at the same time.

### Admin Password

Define password to protect authentification as server admin.
Password is still encrypted in **Sha3_512**.

Admin can kick users, add/delete channels and many things else.

### LogLevel

The log level is an number value that defines the level of details you want to know.

Possible value:

* 1 : Error
* 2 : debug
* 3 : Warning
* 4 : Information

At *Error level*, the server only displays error message.  
The *debug level* is useful when you want to improve the server, add some features and so on.  
The *Warning* message displays message about unexpected data or behaviors.  
At last, the *Information level* gives details about what the server is doing.

Before posting a bug request, it is a good practice to run the application with information level as log level in order to give to the team as much information as possible.

### DeepInspectionLog

Log every events from server.
Activate this option may make the server slower.

Possible value:

* true
* false

### LogFile

set the path where log are written.

**Example**
> LogFile=/var/log/roliserver.log



### ThreadCount

Define the maximum thread count the server may use.

### TimeToRetry

Waiting time (in millisecond) between two tries to listen the **port**.

The server listens any connection on the **port** define in this file.
In rare occasion, this step may fail. Probably, because another server is already listening this **port**. So, **roliserver** will try several time

### TryCount

Define how many time the server will try to listen the port.
If this number is reached. The server exits on error status.

### TimeStart

Define the time in the day when the server allows connection.

It should be written as: hh:mm
Hours must be defined by two numbers as the minutes.

Examples:
8pm
> 20:00

6am
> 06:00


### TimeEnd

Define the time when the server stops accepting.

It should be written as: hh:mm
Hours must be defined by two numbers as the minutes.

Examples:
8pm
> 20:00

6am
> 06:00

### IpBan

define a list of banned IP addresses.

Examples:
A list with 3 addresses
> 80.80.80.80,127.9.9.1,10.10.10.10


### IpMode

ipv4 or ipv6 or both.

It is not used yet.

### MaxMemorySize

Set the value of the maximum size the server should store.
When the limit is reach, all channels drop their data.

Example:

    :::ini
    MaxMemorySize=8G  #Define the size at 8 Gibibyte
    MaxMemorySize=8M  #Define the size at 8 Mebibyte
    
### Example of working .conf file :

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

This will use 0000 as a password, it's recomended you create your own with the password creation utlity available in the rolisteam client.



## Deploy on SystemD

Let's create our service file

```
$ sudo touch /etc/systemd/system/roliserver.service
```

Then copy paste this in roliserver.service:
    
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

Then enable, and start the service:

    :::shell
    $ sudo systemctl enable roliserver.service
    $ sudo sustemctl start roliserver.service


## Deploy in Docker



## Windows
