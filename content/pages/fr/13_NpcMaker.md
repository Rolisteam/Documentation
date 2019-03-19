Title: Npc Maker
Date: 2017-06-11 10:20
slug: npcmaker
status: hidden
lang: fr


**Npc Maker** can create vmap tokens.


![Npc Maker]({static}/images/en/npc_makerinfo_screen.jpg)

# Tabs

* General infos
* Actions
* Shapes
* Properties

# General Info

![Npc Maker]({static}/images/en/npc_makerinfo_screen.jpg)

General information are:

* Name of NPC
* Life points (Min, current and max)
* Initiative Command (dice command)
* Initiative Score  (set it if you don't set initiative command)
* Default avatar
* Default Size
* Npc Color

# Actions

![Npc Maker]({static}/images/en/npcmake_actions_screen.jpg)

Npc Character may have an action list. 
An action is a dice command.
Action can be triggered from token's contextual menu on vmap.
The result appears in the global chat window.

# Shapes

![Npc Maker]({static}/images/en/npcmaker_shape_screen.jpg)

Shape can change how your character looks. It changes its avatar.

# Properties

![Npc Maker]({static}/images/en/npcmaker_property_screen.jpg)

Properties is a list of name and values. It is a simple way to define the NPC. 
Action can use dice command with properties as parameters of the command.
Example:
My assassin agility level is 8.
So I add a property called "agility" and set the value to 8.
In action panel, I add the action "shot arrow" and set the command to be: "1d20+${agility}"


# Load/Save token

To load token file and edit it, please press the button **import**.
When the editing is done, please press the button **export**. 

# Token on vmap

Token can be dropped over vmap. It shows the main avatar and with the contextual menu, it is possible to run action, change current shape of the token. 

Moreover, vmap can roll initiative for all tokens (NPC or NPC and PC).
In one click, the GM can make all initiative rolls.

<p style="text-align: left; width:49%;  display: inline-block;"><a href="/dicebookmark.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/music.html">Next</a></p>
