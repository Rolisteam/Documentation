Title: Thèmes
Date: 2017-06-11 10:20
slug: look
status: hidden
lang: fr

Version 1.7
===========

Les thèmes
----------

Rolisteam propose un panneau pour modifier le visuel de la fenêtre. Par
defaut, il y a trois hèmes:

-   Défaut
-   DarkOrange
-   Darkfusion

Ces trois thèmes ne peuvent pas être modifié. Cependant vous pouvez les
copier puis modifier leur copie.

Un theme pour rolisteam, c\'est:

-   Les couleurs de la palette réparties en trois groupe: Active,
    Inactive et désactivée. Pour plus d\'information:
    [1](http://doc.qt.io/qt-5/qpalette.html#details)
-   Du code Css pour changer de nombreux détails de l\'application.
-   Une image de fond
-   une couleur de fond
-   une position
-   Une couleur pour la valeur de dés.

Import/Export
-------------

Il est possible d\'exporter les thèmes dans un format texte (json). Ce
format vous permet d\'éditer le style tranquillement et de faire vos
propres modifications. Pour tester, il suffit d\'importer le fichier
json.

Exemple de fichier Thème
------------------------

`   {`\
`   "bgColor": "#bfbfbf",`\
`   "bgPath": ":/resources/icons/workspacebackground.bmp",`\
`   "colors": [`\
`       {`\
`           "color": "#000000",`\
`           "group": 0,`\
`           "name": "WindowText",`\
`           "role": 0`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 0,`\
`           "name": "Button",`\
`           "role": 1`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 0,`\
`           "name": "Light",`\
`           "role": 2`\
`       },`\
`       {`\
`           "color": "#cbc7c4",`\
`           "group": 0,`\
`           "name": "Midlight",`\
`           "role": 3`\
`       },`\
`       {`\
`           "color": "#9f9d9a",`\
`           "group": 0,`\
`           "name": "Dark",`\
`           "role": 4`\
`       },`\
`       {`\
`           "color": "#b8b5b2",`\
`           "group": 0,`\
`           "name": "Mid",`\
`           "role": 5`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 0,`\
`           "name": "Text",`\
`           "role": 6`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 0,`\
`           "name": "BrightText",`\
`           "role": 7`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 0,`\
`           "name": "Base",`\
`           "role": 9`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 0,`\
`           "name": "Window",`\
`           "role": 10`\
`       },`\
`       {`\
`           "color": "#767472",`\
`           "group": 0,`\
`           "name": "Shadow",`\
`           "role": 11`\
`       },`\
`       {`\
`           "color": "#308cc6",`\
`           "group": 0,`\
`           "name": "Highlight",`\
`           "role": 12`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 0,`\
`           "name": "WindowText",`\
`           "role": 13`\
`       },`\
`       {`\
`           "color": "#0000ff",`\
`           "group": 0,`\
`           "name": "Link",`\
`           "role": 14`\
`       },`\
`       {`\
`           "color": "#ff00ff",`\
`           "group": 0,`\
`           "name": "LinkVisited",`\
`           "role": 15`\
`       },`\
`       {`\
`           "color": "#f7f5f3",`\
`           "group": 0,`\
`           "name": "AlternateBase",`\
`           "role": 16`\
`       },`\
`       {`\
`           "color": "#ffffdc",`\
`           "group": 0,`\
`           "name": "ToolTipBase",`\
`           "role": 18`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 0,`\
`           "name": "ToolTipText",`\
`           "role": 19`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 0,`\
`           "name": "NoRole",`\
`           "role": 17`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 2,`\
`           "name": "WindowText",`\
`           "role": 0`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 2,`\
`           "name": "Button",`\
`           "role": 1`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 2,`\
`           "name": "Light",`\
`           "role": 2`\
`       },`\
`       {`\
`           "color": "#cbc7c4",`\
`           "group": 2,`\
`           "name": "Midlight",`\
`           "role": 3`\
`       },`\
`       {`\
`           "color": "#9f9d9a",`\
`           "group": 2,`\
`           "name": "Dark",`\
`           "role": 4`\
`       },`\
`       {`\
`           "color": "#b8b5b2",`\
`           "group": 2,`\
`           "name": "Mid",`\
`           "role": 5`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 2,`\
`           "name": "Text",`\
`           "role": 6`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 2,`\
`           "name": "BrightText",`\
`           "role": 7`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 2,`\
`           "name": "Base",`\
`           "role": 9`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 2,`\
`           "name": "Window",`\
`           "role": 10`\
`       },`\
`       {`\
`           "color": "#767472",`\
`           "group": 2,`\
`           "name": "Shadow",`\
`           "role": 11`\
`       },`\
`       {`\
`           "color": "#308cc6",`\
`           "group": 2,`\
`           "name": "Highlight",`\
`           "role": 12`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 2,`\
`           "name": "WindowText",`\
`           "role": 13`\
`       },`\
`       {`\
`           "color": "#0000ff",`\
`           "group": 2,`\
`           "name": "Link",`\
`           "role": 14`\
`       },`\
`       {`\
`           "color": "#ff00ff",`\
`           "group": 2,`\
`           "name": "LinkVisited",`\
`           "role": 15`\
`       },`\
`       {`\
`           "color": "#f7f5f3",`\
`           "group": 2,`\
`           "name": "AlternateBase",`\
`           "role": 16`\
`       },`\
`       {`\
`           "color": "#ffffdc",`\
`           "group": 2,`\
`           "name": "ToolTipBase",`\
`           "role": 18`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 2,`\
`           "name": "ToolTipText",`\
`           "role": 19`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 2,`\
`           "name": "NoRole",`\
`           "role": 17`\
`       },`\
`       {`\
`           "color": "#bebebe",`\
`           "group": 1,`\
`           "name": "WindowText",`\
`           "role": 0`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 1,`\
`           "name": "Button",`\
`           "role": 1`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 1,`\
`           "name": "Light",`\
`           "role": 2`\
`       },`\
`       {`\
`           "color": "#cbc7c4",`\
`           "group": 1,`\
`           "name": "Midlight",`\
`           "role": 3`\
`       },`\
`       {`\
`           "color": "#beb6ae",`\
`           "group": 1,`\
`           "name": "Dark",`\
`           "role": 4`\
`       },`\
`       {`\
`           "color": "#b8b5b2",`\
`           "group": 1,`\
`           "name": "Mid",`\
`           "role": 5`\
`       },`\
`       {`\
`           "color": "#bebebe",`\
`           "group": 1,`\
`           "name": "Text",`\
`           "role": 6`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 1,`\
`           "name": "BrightText",`\
`           "role": 7`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 1,`\
`           "name": "Base",`\
`           "role": 9`\
`       },`\
`       {`\
`           "color": "#efebe7",`\
`           "group": 1,`\
`           "name": "Window",`\
`           "role": 10`\
`       },`\
`       {`\
`           "color": "#b1aeab",`\
`           "group": 1,`\
`           "name": "Shadow",`\
`           "role": 11`\
`       },`\
`       {`\
`           "color": "#918d7e",`\
`           "group": 1,`\
`           "name": "Highlight",`\
`           "role": 12`\
`       },`\
`       {`\
`           "color": "#ffffff",`\
`           "group": 1,`\
`           "name": "WindowText",`\
`           "role": 13`\
`       },`\
`       {`\
`           "color": "#0000ff",`\
`           "group": 1,`\
`           "name": "Link",`\
`           "role": 14`\
`       },`\
`       {`\
`           "color": "#ff00ff",`\
`           "group": 1,`\
`           "name": "LinkVisited",`\
`           "role": 15`\
`       },`\
`       {`\
`           "color": "#f7f5f3",`\
`           "group": 1,`\
`           "name": "AlternateBase",`\
`           "role": 16`\
`       },`\
`       {`\
`           "color": "#ffffdc",`\
`           "group": 1,`\
`           "name": "ToolTipBase",`\
`           "role": 18`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 1,`\
`           "name": "ToolTipText",`\
`           "role": 19`\
`       },`\
`       {`\
`           "color": "#000000",`\
`           "group": 1,`\
`           "name": "NoRole",`\
`           "role": 17`\
`       }`\
`   ],`\
`   "css": "",`\
`   "diceHighlight": "#000000",`\
`   "name": "default",`\
`   "position": 0,`\
`   "removable": false,`\
`   "stylename": "fusion"`\
`   }`
