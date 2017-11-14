Title: Look and Feel
Date: 2017-06-11 10:20
slug: look
status: hidden
lang: en

This panel is part of the rolisteam preferences panel. Its goal is to
change and customize the graphical user interface of Rolisteam.

# Default Themes
By default, Rolisteam ships three themes:

-   Default
-   DarkOrange
-   Darkfusion

These three themes can not be modified but you may copy them and make
changes on those copies.

# What can I change ?

The theme is gathering all data to customize **Rolisteam**.

-   Color Palette describes all colors used by the application and there
    are divided into 3 groups: Active, Inactive and disabled. More
    details at: [1](http://doc.qt.io/qt-5/qpalette.html#details)
-   Css code to change several details on the applications (e.g: size of
    scrollbar, background color, size of button text…)
-   Background color
-   Background image
-   Positioning rule for the image.
-   Dice result Highlight color.

## Example 

### Change the color of current tab

<pre>

</pre>


### Change font size in chatwindow

<pre>

</pre>

Import/Export
-------------

You can export themes in text file (.rSkin). You can edit the file
with regular text editor and test your modification by importing the
file into rolisteam.

Example of rSkin file
-------------------------------
   
<pre>
   {
   "bgColor": "#bfbfbf",
   "bgPath": ":/resources/icons/workspacebackground.bmp",
   "colors": [
       {
           "color": "#000000",
           "group": 0,
           "name": "WindowText",
           "role": 0
       },
       {
           "color": "#efebe7",
           "group": 0,
           "name": "Button",
           "role": 1
       },
       {
           "color": "#ffffff",
           "group": 0,
           "name": "Light",
           "role": 2
       },
       {
           "color": "#cbc7c4",
           "group": 0,
           "name": "Midlight",
           "role": 3
       },
       {
           "color": "#9f9d9a",
           "group": 0,
           "name": "Dark",
           "role": 4
       },
       {
           "color": "#b8b5b2",
           "group": 0,
           "name": "Mid",
           "role": 5
       },
       {
           "color": "#000000",
           "group": 0,
           "name": "Text",
           "role": 6
       },
       {
           "color": "#ffffff",
           "group": 0,
           "name": "BrightText",
           "role": 7
       },
       {
           "color": "#ffffff",
           "group": 0,
           "name": "Base",
           "role": 9
       },
       {
           "color": "#efebe7",
           "group": 0,
           "name": "Window",
           "role": 10
       },
       {
           "color": "#767472",
           "group": 0,
           "name": "Shadow",
           "role": 11
       },
       {
           "color": "#308cc6",
           "group": 0,
           "name": "Highlight",
           "role": 12
       },
       {
           "color": "#ffffff",
           "group": 0,
           "name": "WindowText",
           "role": 13
       },
       {
           "color": "#0000ff",
           "group": 0,
           "name": "Link",
           "role": 14
       },
       {
           "color": "#ff00ff",
           "group": 0,
           "name": "LinkVisited",
           "role": 15
       },
       {
           "color": "#f7f5f3",
           "group": 0,
           "name": "AlternateBase",
           "role": 16
       },
       {
           "color": "#ffffdc",
           "group": 0,
           "name": "ToolTipBase",
           "role": 18
       },
       {
           "color": "#000000",
           "group": 0,
           "name": "ToolTipText",
           "role": 19
       },
       {
           "color": "#000000",
           "group": 0,
           "name": "NoRole",
           "role": 17
       },
       {
           "color": "#000000",
           "group": 2,
           "name": "WindowText",
           "role": 0
       },
       {
           "color": "#efebe7",
           "group": 2,
           "name": "Button",
           "role": 1
       },
       {
           "color": "#ffffff",
           "group": 2,
           "name": "Light",
           "role": 2
       },
       {
           "color": "#cbc7c4",
           "group": 2,
           "name": "Midlight",
           "role": 3
       },
       {
           "color": "#9f9d9a",
           "group": 2,
           "name": "Dark",
           "role": 4
       },
       {
           "color": "#b8b5b2",
           "group": 2,
           "name": "Mid",
           "role": 5
       },
       {
           "color": "#000000",
           "group": 2,
           "name": "Text",
           "role": 6
       },
       {
           "color": "#ffffff",
           "group": 2,
           "name": "BrightText",
           "role": 7
       },
       {
           "color": "#ffffff",
           "group": 2,
           "name": "Base",
           "role": 9
       },
       {
           "color": "#efebe7",
           "group": 2,
           "name": "Window",
           "role": 10
       },
       {
           "color": "#767472",
           "group": 2,
           "name": "Shadow",
           "role": 11
       },
       {
           "color": "#308cc6",
           "group": 2,
           "name": "Highlight",
           "role": 12
       },
       {
           "color": "#ffffff",
           "group": 2,
           "name": "WindowText",
           "role": 13
       },
       {
           "color": "#0000ff",
           "group": 2,
           "name": "Link",
           "role": 14
       },
       {
           "color": "#ff00ff",
           "group": 2,
           "name": "LinkVisited",
           "role": 15
       },
       {
           "color": "#f7f5f3",
           "group": 2,
           "name": "AlternateBase",
           "role": 16
       },
       {
           "color": "#ffffdc",
           "group": 2,
           "name": "ToolTipBase",
           "role": 18
       },
       {
           "color": "#000000",
           "group": 2,
           "name": "ToolTipText",
           "role": 19
       },
       {
           "color": "#000000",
           "group": 2,
           "name": "NoRole",
           "role": 17
       },
       {
           "color": "#bebebe",
           "group": 1,
           "name": "WindowText",
           "role": 0
       },
       {
           "color": "#efebe7",
           "group": 1,
           "name": "Button",
           "role": 1
       },
       {
           "color": "#ffffff",
           "group": 1,
           "name": "Light",
           "role": 2
       },
       {
           "color": "#cbc7c4",
           "group": 1,
           "name": "Midlight",
           "role": 3
       },
       {
           "color": "#beb6ae",
           "group": 1,
           "name": "Dark",
           "role": 4
       },
       {
           "color": "#b8b5b2",
           "group": 1,
           "name": "Mid",
           "role": 5
       },
       {
           "color": "#bebebe",
           "group": 1,
           "name": "Text",
           "role": 6
       },
       {
           "color": "#ffffff",
           "group": 1,
           "name": "BrightText",
           "role": 7
       },
       {
           "color": "#efebe7",
           "group": 1,
           "name": "Base",
           "role": 9
       },
       {
           "color": "#efebe7",
           "group": 1,
           "name": "Window",
           "role": 10
       },
       {
           "color": "#b1aeab",
           "group": 1,
           "name": "Shadow",
           "role": 11
       },
       {
           "color": "#918d7e",
           "group": 1,
           "name": "Highlight",
           "role": 12
       },
       {
           "color": "#ffffff",
           "group": 1,
           "name": "WindowText",
           "role": 13
       },
       {
           "color": "#0000ff",
           "group": 1,
           "name": "Link",
           "role": 14
       },
       {
           "color": "#ff00ff",
           "group": 1,
           "name": "LinkVisited",
           "role": 15
       },
       {
           "color": "#f7f5f3",
           "group": 1,
           "name": "AlternateBase",
           "role": 16
       },
       {
           "color": "#ffffdc",
           "group": 1,
           "name": "ToolTipBase",
           "role": 18
       },
       {
           "color": "#000000",
           "group": 1,
           "name": "ToolTipText",
           "role": 19
       },
       {
           "color": "#000000",
           "group": 1,
           "name": "NoRole",
           "role": 17
       }
   ],
   "css": "",
   "diceHighlight": "#000000",
   "name": "default",
   "position": 0,
   "removable": false,
   "stylename": "fusion"
   }
</pre>
