Title: Instant Messaging
Date: 2017-06-11 10:20
slug: chatting
status: hidden
lang: en


# Chatroom

At start, **Rolisteam** adds automatically several chatroom.
Every chatrooms are listed in the *Chat messaging* panel.
The first one is always the *global* chatroom.

![chatrooms]({static}/images/tuto/02_ChatList_en.jpg)

## Global chatroom

This chatroom brings together everyone. When new person connect to the server it is automatically added to the global chatroom.

## One to One chatroom

**Rolisteam** prepares one to one chatrooms. When you want to chat with only one person is the best way to do it.

## Display chatroom

<!--Two ways to do it:-->
* Check the chatroom on the *Chat messaging* panel
<!--* Click on the chatroom name on the `sub-windows` menu.-->

## Hide chatroom

<!--//Two ways to do it:-->
* Uncheck the chatroom on the *Chat messaging* panel
<!--//* Click on the chatroom name on the `sub-windows` menu.-->

## Flicking Chatroom

Flicking Chatroom (green to red) means there are unread message.

## Add chatroom

Just click on `Add a chat` and select every one who should attend to this chatroom.
Chatroom may have 1 or several participants.

![add chatroom]({static}/images/tuto/15_nouveauChat_en.jpg)


## Delete chatroom

Select the chatroom to remove and click on `Delete a Chat`.


Enough about the chatroom, lets take a look at what we can do with ChatWindow.

# Chatwindow

![images]({static}/images/tuto/25_tchat_commun_en.jpg)

Message starts with its sender's name in the sender's color.
Url links are clickable. They open with you default web browser.
The top zone displays the conversation and the bottom text zone is the writing zone.

## Write message

Select the bottom zone on chatroom. Then write the text.
To send multiline text, paste your text inside the writing zone.

## Send message

Press `Enter` to send the message.

## Resend an old message

Press `up` or `down` to navigate in the history of sent messages.

## Send message with your character

Change the selected person in the sender list from your player identity to your character.

## Send dice command

Start with `!` and the command.

Example:
> !1d20

Every one in the chatroom sees the result.

To roll secret dice command, start with *&* (instead of !)
To display the result only to the GM, start commands with *#* (instead of !)

More details about dice rolls: please read [dice roller]({filename}21_dice_roller.md) page.

## Send command

*Chatwindow* supports *emote* command.

Start your text with `/me`.
Example:

> /me leaves the castle.

result (assuming Kallice is the selected person):

> Kallice leaves the castle.


## Save conversation

Click on ![icons]({static}/images/pictos/chat_save.png)
Conversation are saved in *html*.

## Show contextual menu

![menu]({static}/images/panel/chat_contextual_menu.jpg)

There are two different context in chatwindow.
One for writing zone, it is really simple and provides standard text action (copy, paste etc.)

On the conversation zone, there are more features.

## Timestamps

Show contextual menu.  
Click on `Display time`.  
New messages start with time of arrival.  

Set this behaviour as default, see [Preferences]({filename}22_preferences.md) page.

## Change background color

Show contextual menu. 
Click on `Background color` 
Color selector dialog appears.  
Select the color.  
Click on `Ok`  

## Word Warp

By default, **Word warp** is enabled.
When text is longer than the window width. **Rolisteam** tries to split the text between two words (a new line instead of space).

When dice commands with a lot dice are rolled, the result displays no space between two rolled values. It may cause some slowness.
Disable **word wrap** prevent that slowness.

## Detach the view

Show contextual menu.
Click on `Detach the view`
The *chatwindow* disappears from **Rolisteam** workspace and it appears somewhere on you screen.

## Reattach

Show contextual menu.
Click on `Detach the view`
The *chatwindow* appears inside **Rolisteam** workspace.


## Change Font size

Press `Ctrl+mouse wheel`.
The text size changes directly.

To make this parameter permanent, see [theme]({filename}23_look_and_feel.md)

<p style="text-align: left; width:49%;  display: inline-block;"><a href="/connected.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/resources.html">Next</a></p>
