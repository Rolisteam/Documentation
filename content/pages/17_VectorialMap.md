Title: Vectorial Map
Date: 2017-06-11 10:20
slug: vectorialMap
status: hidden
lang: en

# Vectorial Maps


One of the biggest new features is the vectorial map. The main
difference between this new plan and the older maps is that new plans
allow to add items and modify them. For example, you can add a rectangle
and change its size, rotate it or move it. All items can manage these
kinds of transformation.

## Features

-   Z Positioning : each item is added above the previous ones.
-   Infinite Plan Size
-   Zooming Up
-   Zooming Down
-   Move the camera on the plan
-   Amend item on map (Add, upsize, downsize, move, rotate, delete)
-   Management of Character Token
-   These token can show a picture of character.
-   Add images
-   These images can be animated (gif…)
-   Management of collision
-   Item can be placed into set (ground, object or character)
-   Opacity
-   others…

## Make a new vectorial map

You just have to go on **file** menu then to go in the **new** submenu
then **Vectorial Map** A dialog opens:

![new vmap]({static}/images/tuto/13_newVMap_en.jpg)

-   The title appears at the top of the map frame. It makes easier to
find it in your workspace.
-   The background color is used as global color of the map (default:
white).
-   The visibility defines how your players see the map. Hidden means
they see nothing. Fog Of War hides all map's elements (you can amand
the fog to make visible some elements). Visible, all map items can
be seen by the players. You can change the visibility at any moment
in the game).
-   Permission Mode describes which actions players can do. You can
change it at any moment.
-   Grid scheme defines the shape of the grid: ne scheme (no grid),
square grid, hexagonal grid.
-   You can change the Grid color.
-   The size set how many pixels one single grid scheme is.
-   The scale defines in the unit of your choice the size of one grid
scheme.

## Open Vectorial map


You have to click on **File &gt; Open &gt; Vectorial Map**. Open file
dialog appears. You must find the map on your computer. The extension
for vectorial map is **.vmap**.

## Graphic Item available

### Tool box

![toolbox vmap]({static}/images/tuto/ToolBox_009.jpg)

#### Color selector

The first square is the current color. Double-click on it causes the
appearance of a color selector dialog. By clicking on the multi-color
square, you can select the hue of the current color. You can make it
darker or lighter with the last slide bar.

#### Edition Mode

There are three edition modes.

-   Normal to paint on the map
-   Veil to hide some part of the map with fog of war.
-   Unveil to make visible some part of the map by cutting the fog of
war.

After changing the mode, you just have to use regular painting tools.
Given the mode, painting has effect on the right element (map or fog of
war).

#### Pen

![pen]({static}/images/pictos/pen.png)

You can paint line which follow your mouse.
The diameter selector defines the width of the line.
You can move the item but changing its curve is not supported.

#### Straight Line
![pen]({static}/images/pictos/line.png)

You must define two points to add straight line to the map: the starting
point and the ending point.
The diameter selector defines the width of the line.
You can move the item and change the position of starting point or
ending point.

#### Empty Rectangle
![pen]({static}/images/pictos/emptyrectangle.png)

You can add empty rectangle on the map.
The diameter selector defines the width of the border.
You can move the rectangle and change its size by moving its corner.

#### Filled Rectangle
![pen]({static}/images/pictos/filledrectangle.png)

You can add Filled rectangle on the map.
You can move the rectangle and change its size by moving its corner.

#### Empty Ellipse
![pen]({static}/images/pictos/emptyellipse.png)

You can add empty ellipse on the map.
The diameter selector defines the width of the border.
You can move the rectangle and change its size by moving its two
handles.

#### Filled Ellipse
![pen]({static}/images/pictos/filledellipse.png)

You can add Filled ellipse on the map.
You can move the rectangle and change its size by moving its two
handles.

#### Text
![pen]({static}/images/pictos/text.png)

Add text element on the map. The text can be changed. The border defines
the maximum width of the text. The text is wrapped automatically. The
zone height adapts itself given the number of line. It is possible to
add blank line manually to improve the readability. The text item
manages HTML. To make it possible, you may paste webpage, the formatting
is the same or directly you can edit the text thank of the rich text
editor.
![Text editor]({static}/images/panel/RichTextEditor.jpg)

This editor allows modifications of properties of the text: Color, size,
font, underline, italic… It supports the copy/paste. You can create a
list. It is also possible to edit html code.

#### Handle
![pen]({static}/images/pictos/hand.png)

This tool allows to catch items on the map and move them. It is also
useful to catch control square to make bigger or rotate the item (Ctrl +
Mouse motion) It is also possible to move the item the whole map by
keeping pressed the Shift pressed and clicking on the map.

#### Rule
![pen]({static}/images/pictos/rule.png)

This tool gets the distance between two points on the map given the
current defined scale.

#### Path
![pen]({static}/images/pictos/path.png)


Path is several lines. It can be closed and filled (right-click on the
path) and each point can be moved individually.

#### Anchor
![pen]({static}/images/pictos/insert-link-2.png)

It is possible to make a item anchored on another. This defines a
parenthood relationship. If A is anchored on B. B is the parent of A. If
B is moved, A is moved as well. If A is moved, B does not move.

This feature makes easier any vehicles. You can move the vehicle, which
means you move all passengers.

#### Color Picker
![pipette]({static}/images/pictos/pipettecursor.png)

Click on any item. Its color becomes the current color.

#### Diameter Tool

Many items such as path, empty rectangle, empty ellipse, line and pen
use the diamter value to paint itself. The value can not be change
dynamically. When the item is created, it reads the value and keep it.

#### NPC
![NPC]({static}/images/pictos/add.png)

You can add PNJ, you can define the NPC name. The Plus symbol is the
tool to add NPC on map. The NPC number est increase after adding NPC on
map. It is possible to reset that number by clicking on the counter
button.

#### Opacity

This tool allows you to define the opacity of the current item. It can
be changed dynamically.

### Tool bar
![tool bar]({static}/images/pictos/)

To show/hide the tool bar, you can press F9 key.

#### Background Color
![pen]({static}/images/en/vectorial_map_toolbar.jpg)

You can change the current color of the map.

#### Grid
![pen]({static}/images/pictos/grid.png)

There is all you need to control the grid. First, the button to
show/hide the grid. Then, you can chose the grid scheme: no scheme,
square or hexagon. if the current scheme is no scheme, the grid will not
be visible. You can change the size of grid scheme or its unit.

#### Permission

The permission defines the action that player can do on the map. There
are 3 permission modes.

-   Only GM: in this mode, players have no rights.
-   Character: players can move their character items.
-   All : players can do whatever they want.

#### Visibility

There are 3 visibility mode:

-   Hidden: all items are hidden. Only the GM can see them all.
-   Fog of war: Item are under the fog of war, the GM can erase the fog
of war to show part of the map (details see edition mode).
-   Visible : all items are visible.

### Contextual Menu (right-click)
![pen]({static}/images/panel/menu_vmap.jpg)

From the contextual menu on vectorial map, you can control many aspects from the map or selected items.
All actions are reachable from the menu. At the top of it, there are actions for selected items.
The second part is dedicated to amend properties of map.

-   Change current layer.
-   Change the visibility.
-   Zoom in makes items bigger.
-   Zoom out allows you to see more items on the map (they will appear
smaller).
-   Zoom in Max makes items bigger at the maximum value.
-   Zoom normal set the zoom level to 1 meaning no zoom.
-   Zoom out Max makes the scene fit as much as possible the view.
-   Import image from your computer to the map.
-   "Properties" displays dialog box with parameters for vectorial map.
You can change parameters from it.

#### SubMenu: Overlapping [Item]

![layers]({static}/images/panel/submenu_vmap_overlapping.jpg)

Selected Items can be the lowest, the highest, or just lower or higher than their current position.

#### SubMenu: Rotation [Item]

![layers]({static}/images/panel/submenu_vmap_item_rotation.jpg)

Rotate selected Items (the center of rotation is the item center).

#### SubMenu: Layers [Item]

![layers]({static}/images/panel/submenu_vmap_layer.jpg)

Put item in a specific layer.

#### SubMenu: Resize [Item]

![layers]({static}/images/panel/submenu_vmap_resize.jpg)

Resize selected items given rules.

#### SubMenu: Layers [Maps]

![layers]({static}/images/panel/submenu_vmap_layer.jpg)

Set the current layer. Only items in this layer can be edited.

#### SubMenu: Visibility [Maps]

![layers]({static}/images/panel/submenu_vmap_visibility.jpg)

Define how players see the map.


#### SubMenu: Roll initiative [Maps]

![layers]({static}/images/panel/submenu_vmap_roll_init.jpg)

Roll initiative.

#### SubMenu: Roll initiative [Maps]

![layers]({static}/images/panel/submenu_vmap_roll_init.jpg)

Unset initiative value.


#### SubMenu: Zoom [Maps]

![layers]({static}/images/panel/submenu_vmap_zoom.jpg)

Zoom in or out.

#### Item


-   Down puts current item under items below it.
-   Up puts current item above all items which hide it.
-   Bottom puts the current item under all others.
-   Top puts current item above all others.
-   Delete the current item (You can also select an item and press the
key **Del**).
-   Duplicate creates a copy of the current item (same color and size).
-   Rotate allows you to select precisely the angle of rotation.
-   Change the layer where current item belongs to.

#### Path


-   **Close the path** closes the path geometry (line between the last
point to the first one).
-   **Fill the path** fill the path with its color.

#### Text


-   **Edit the text…** opens the text editor
-   **Adapt to content** makes the item to shape itself close to its
content.
-   **Font Size** allows you to increase or decrease the font size.

#### Several Items


-   **Delete** removes current items supprime (press key **Del**).
-   **Down** puts current items under items below them.
-   **Up** puts current items above items which hide them.
-   **Bottom** puts current items under all others.
-   **Top** puts current items above all others.
-   **Lock up** prevents item to change size.
-   **Rotate** allows you to define the rotation angle precisely on all
current items.
-   **Current layer** set all current items into another layer.
-   **Normalize size** changes the size of the selection to fit one of
these rules: as the smallest, as the biggest, as average or as the
one under the mouse.

## Layers management

Layers are set of items. There are dedicated to define interactions you
can have with them. We recommend to add first ground items, then to put
object items and at the end, add character into the map.

Warning, layers do not manage the overlapping of items. You can control
it thank of the contextual menu.

**Each item belongs to one and only one layer**. You can change the
layer of item with the contextual menu. You can define the current layer
of the map. Which means new items will be added at this layer. By
default, it is the ground. You can only edit item from the current
layer.

To make it simple, it is possible to use only one layer.

### Ground

Items belongs to the ground and character token cannot enter in
collision with them.

### Object

Items inside this layer can enter in collision with character token (if
Collision is enable of course).

### Characters

Item inside this layer can enter in collision with item from Object
layer (if Collision is enable of course).

### Fog of war

The fog of war can be enable from the toolbar. It hides the map under
black screen. This black screen is fully opaque for players but
half-transparent for the GM. To modify the fog of war to make appear
items, you have to set the proper edition mode and select any tool from
the toolbox.

<p style="text-align: left; width:49%;  display: inline-block;"><a href="/map.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/minutes.html">Next</a></p>
