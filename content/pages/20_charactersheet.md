Title: Character Sheet
Date: 2017-06-11 10:20
slug: charactersheet
status: hidden
lang: en


## Rolisteam CharacterSheet Editor (RCSE)

Making character sheet required to follow several steps:

### 1/ Import image

The first step is to drop background image. This image can be created
from the PDF file of the official charactersheet of your game or you can
design it yourself.

There are two ways to import image:

-   Drag and drop image from your computer to RCSE.
-   You can also import from the menu &gt; Define Background Image

In the case, where you need several pages into your charactersheet. You
can easily add pages with the button dedicated to this task. Then you
will have to define the background of new pages by importing background
images.

### 2/ Put fields on the sheet

Then, it is important to set the position of each text field. This work
can be really long but thanks to RCSE you can make it graphically.

Each field is also added into the right table. You can remove field from
this table.

There are many field kinds available into RCSE :

| Name      | Description                                                                                              | Icon |
|-----------|----------------------------------------------------------------------------------------------------------|------|
| TextInput | it stores one line of text, it has no border and no decoration. It can be change to selector (see below) |      |
| TextField | It stores one line of text, it has border and decoration.                                                |      |
| Checkbox  | It stored a 0 or 1 value and display it as checkbox.                                                     |      |
| TextArea  | It stores text (several lines) with decoration and border.                                               |      |
| Button    | it stores a dice command. Clicking on it, run the command.                                               |      |
| Image     | Display a image, the path to the image should be url, such as <http://myimage.org/character.jpg>         |      |

#### Change Textinput to selector

Easy Peasy, you just have to set possible values in the dedicated column
into the right table. Values are separated by comma. Example: red,blue,
green, brown, yellow, black,white, orange, purple.

### 3/ Edit fields

when all yours field are set, it is important to name them. This name
can be use into formula.

Including the name, many other properties can be edited. All you have to
do is to edit from the right table on the first tab.

Columns:

#### Id

This property is the unique id for that data. By default, RCSE generates
automatically the value. It is recommended to keep the default value. It
is possible to get access to the data by its id. Example: =${id_5}+4

#### Label

This property is a human readable id for that data. It is left empty
when you add new field. The writer of the character sheet must set this
value. It is possible to get access to the data by its label. Example:
=${intelligence}+4

#### Value

The value is displayed into the character sheet. It is also the element
which is used into formula or dice command.

#### Possible values

This field is only useful for TextInput. It allows to change a TextInput
to selector. Selector (also known as Combobox) are items dedicated to
select one value from limited list.

#### Type

This column give you a reminder of the type of the field: TextInput,
TextField, checkbox, TextArea, Button, Image…

#### X

Field Position on X-axis (width). You can change it to align the field
precisely.

#### Y

Field Position on Y-axis (height). You can change it to align the field
precisely.

#### width

Width of the field. You can change it to align the field precisely.

#### Height

Height of the field. You can change it to align the field precisely.

#### Font adaptation

This option can be enable to adapt font size to the size of the
character sheet.

#### Text Alignment

You can set where the text should be displayed in the field.

#### Text color

You can set the text color.

#### Background Color

You can set the background color

#### Border

You can set where the border should display (Top, right, left bottom,
all or no border)

## Generate sheet

When you have added all the fields you want, you may generate the sheet
by clicking on « **edit &gt; Generate Code and Sheet** ».

Sheet is visible in the **View** tab. The tab shows sheet exactly as it
will be in Rolisteam.

The code tab sees its content changed by this action. It shows qml code.

You can adjust the sheet (in the editor tab) and generate again and
again until it fits your needs.

#### For veterans / experts

It is also possible to amend QML code directly to add new features to
the sheet. You can play music, videos or add animations and many other
stuffs. Be careful, when you modify the generated code, you must not ask
to generate code and sheet. It will erase all your modifications.

### 5/ Add character

When your charactersheet is all set. As last step, you must add
characters. There are two ways to do so.

The first one leads you to the Characters tab in RCSE. The first column
shows all fields that you added in your charactersheet. Thanks to the
contextual menu, you can click on **Add character**. Add as many
character as you want. New column will appears for each new character.
Then, you must set a value to each field. RCSE provides some features to
make the edition easier. There are reachable from the contextual menu.

The second method is to share character with their owners thanks to
rolisteam and let them set all the values.

## Rolisteam

### Open/load character sheet

When you save character sheet with RCSE, you get a .rcs file. This file
must be loaded in Rolisteam (**File &gt; Open &gt; Character Sheet** or
**CTRL+U**). A new window opens and you see a data tab and on tab by
character. The data tab is the same that the last tab in RCSE. It shows
all values from characters. GM can have a good overview about all
PCs/NPCs at once. Then, other tabs show the character sheet of one
character in the view mode.

### Share sheet to Character

GM must share the character sheet with their player's character in order
to make it appear to the player. To do that, you must click on the Share
sub-menu from the contextual menu. Then, you have to pick a character.
The tab title is changed to the name of the chosen character. On player
screen, the charactersheet window appears with two tabs: data and view.
The player can change values from both view.

### many pages

As we saw, it is possible to create character sheet with several pages.
In the view tab, you can change page by pressing **Left** or **Right**
key. You can also copy the view and/or detach the tab. This is the way
to show several pages at once.

## Computation formula

Charactersheet embeds formula engine. You can compute automatically
values. It may be useful to make game mechanism easier. To add a new
formula, you just have to start the line with :**=** such as any
spreadsheet software.

### Possible Operation

The formula system can manage many functions and operations.

###  Get value

As we saw, you can get the value of any field thank of its label or id.
You must encapsulate id or label like this: ${label} ou ${id}.

### Arithmetic

You can do all usual operations.

Examples:

#### Sum

> 4+4

> ${intelligence}+3


#### Subtraction

> 12-3

> ${intelligence}-3

#### Multiplication

> 2\*7

> 2x7
> =${intelligence}\*3

#### Division

> 15/5

> 15÷5
> =${intelligence}/3
> =${intelligence}÷3

#### abs

Absolue value takes only one argument.

> =abs(-3)
3

> =abs(3)
3

> =abs(${intellegence}-11)
8

#### min

This function takes several arguments.

> =min(3,8,10,1)
1

> =min(${wits},${dexterity})
3

#### max

This function takes several arguments.

> =max(3,8,10,1)
10

> =min(${wits},${dexterity})
4

#### concat

This function takes several arguments.

> =concat(${investigation}+${perception},"G",${perception})
7G3

> =concat(${investigation},"d10k",${perception})
4d10k3

#### floor

the function takes one argument.

> =floor(3.9)
3

> =floor(3.1)
3

> =floor(${force}/2)
1

#### ceil

the function takes one argument.

> =ceil(3.9)
4

> =ceil(3.1)
4

> =ceil(${force}/2)
2

#### avg

This function takes several arguments.

> =avg(10,10)
10

> =avg(8,4)
6

> =avg(${intelligence},${dexterity})
3.5


<p style="text-align: left; width:49%;  display: inline-block;"><a href="/sharednotes.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/webview.html">Next</a></p>
