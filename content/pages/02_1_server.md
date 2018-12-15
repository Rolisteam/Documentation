Title: Roliserver
Date: 2017-06-11 10:20
slug: roliserver
status: hidden
lang: en

## Presentation

Roliserver is dedicated to host several games on the same computer. 
RPG players communities may offer this service to their users.

## First run

We strongly recommend to start roliserver as follow:

```roliserver -p config.conf```

It generates an empty configuration file named "config.conf" (change the name if you want).

```
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
``` 

Change value accordingly to your needs.
The order of element is not important.

## Configuration file

### Password

Define password to acces the server.
Every password stored in this file must be encrypted with Sha3_512 method.
Don't worry, it is really easy to do.

first, start the server with -g parameter. 

```$ roliserver -g```

It asks you to type the password.
Then it prints the encrypted version of your password.

> P9d63VIxEvincVCutARz0W86GFFX36h0zWEIUomzusZmnv3krtcEsXzZWKKXXv6Ivag+8fR2a7tRWoaaIu3L1w==

Then you can copy/paste this key into your file.

### Port

Define connection port, Usual port is 6660 but it can be changed.

### ConnectionMax

Define the maximum number of clients that the server allows.

### ChannelCount

Define the number of channels at the first start of the server.

### Admin Password

Define password to protect authentification as server admin.
Password is still encrypted in Sha3_512.

### LogLevel

Possible value:
* 1 : Error
* 2 : debug
* 3 : Warning
* 4 : Information

### DeepInspectionLog

Log every events from server. 
Activate this option may make the server slower.

Possible value:
true
false

### LogFile 

set the path where log are written.

**Example**
> LogFile=/var/log/roliserver.log



### ThreadCount 

Define the maximum thread count the server may use. 

### TimeToRetry

Waiting time after server fails to listen in millisecond. 

### TryCount

Define how many time the server will try to listen the port.
If this number is reached. The server will quit. 

### TimeStart 

Define the time in the day when the server allows connection. It should be written as: 

### TimeEnd

Define the time when the server stops accepting. 

### IpBan

define a list of baned IP address 

### IpMode 

ipv4 or ipv6 or both

### MaxMemorySize

Set the value of the maximum size the server should store.
When the limit is reach, all channels drop their data.

Example:

MaxMemorySize=8G *Define the size at 8 Gibibyte*
MaxMemorySize=8M *Define the size at 8 Mebibyte*


## Deploy on SystemD

This is an example to run rolisteam as deamon with systemd.
```
[Unit]
Description=Rolisteam Server Daemon
After=network-online.target

[Service]
Type=forking

User=renaud
Group=renaud
UMask=007

ExecStart=/usr/local/bin/roliserver -f /path/to/conf/roliserver.conf

Restart=on-failure

TimeoutStopSec=300

[Install]
WantedBy=multi-user.target
```

## Deploy in Docker



## Windows

