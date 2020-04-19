Title: Resources Manager
Date: 2017-06-11 10:20
slug: resources
status: hidden
lang: en


# Goals

![image]({static}/images/en/resources_explorer.jpg)

The *Resource manager* is new way to see all assets required in your game.
It keeps track of every loaded files to offer an quick and easy way to (re)-open them the next session.
It is more than a way to restore **Rolisteam's** state. It provides way to order resources.

Chapter is like a directory which can accepts resources.

Supported ressources are :

* Map
* Vectorial Map
* Picture
* Charactersheet
* Note
* Shared note
* Audio Playlist
* NPC
* PDF file
* Web page (url)

# Columns

Each *Resource* have properties which describes its current status.

## Name

Obviously, the first column is the *resource* name.
Edit the cell to rename the *resource*.

## Loading mode

This property defines how the **resource manager** keeps track of this resource.

### Understand the flow

#### New Media

New created media (```File > new > ...```) have no path. By default, their loading mode is *Internal*.
If you try to save it (any internal media) by ```Ctrl+S```. It will in fact save the scenario (and this new media in it).

To save the media only, you must use ```Save as...``` action. It defines the resources path and set its loading mode to linked.

#### Opened Media

Opened Media are stored as linked by default.

#### Exception about PDF

PDF file are always managed as linked. They can't be internal due to heaviness of RPG pdf files.

There are two values.

### Linked

Only the path is saved inside the scenario file.
It makes the file small and don't dupplicate any data.
If original data are deleted or moved, the **resource manager** won't be able to access it.

### Internal

Data are saved inside scenario file.
It makes the scenario heavier but it becomes a standalone file. So, it can be shared.
The original data can be deleted. It is stored inside the .sce file.

## Displayed

### Shown

The resource is displayed on your workspace. It can be shown or hidden to all the other participants.
The shown status in *resources manager* means displayed or minimized.

### Hidden

The resource is hidden. It can be displayed through the `Sub-windows` menu.
It can be shown or hidden to all other participants.

### Unloaded

The resource isn't loaded. The scenario offers a quick way to open it (and show it).

## Path

The path is the fill path to the file.  
If the file does not exist anymore (relocated, renammed or deleted), the line appears red.



# Save/Restore

Saving the scenario is in fact, saving the *resources manager*.


# Context Menu

![menu]({static}/images/panel/resources_manager_contextual_menu.jpg)

* Change loading mode
* Add chapter
* Remove chapter or resources
* Show/hide loading mode
* Show/hide displayed mode
* Show/hide full path

# Example:

![manager with data]({static}/images/panel/resouces_manager_with_data.jpg)

In this case, we have 3 folders (rules, NPC and places). Each of them contains medias.
The icon gives information to the type. The resource manager lists PDF, images, map, vectorial map, charactersheet, notes.
*Linked* medias have been dropped on the application, when `Sake House` is a new document (make it `internal`).  

# Use cases

## Share media once but Don't keep tracks of the image.

To forget a media, just remove it from the **resources manager**.

## Close media to every one but keep it in **resources manager**

Ensure the media, you want to close is the current one.

Menu: ```File > close```

## Some medias have red background, what does it mean ?

It means the media has never been saved, and **Rolisteam** does not know where to save it (no path).
Saving the document or the scenario will fix it.

## Close media and forget it


Menu: ```File > close```
then, just remove it from the **resources manager**.

In one action, you can use the context menu on the resource to close and remove it.



<p style="text-align: left; width:49%;  display: inline-block;"><a href="/chat.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/namegenerator.html">Next</a></p>
