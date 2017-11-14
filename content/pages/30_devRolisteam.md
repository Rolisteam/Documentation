Title: Coding Rules
Date: 2017-06-11 10:20
slug: coding-rules
status: hidden
lang: en



## Rules

This page is made for helping rolisteam developers to improve the quality of their work. 
So, We need to respect few rules to prevent any troubles. Please, read this attentively!

### Rule 0
Write it in English!!

## Style

### Rule 1.1: class
Each word of class name, structures, typedef and enum identifier must start with uppercase letter. 
Example: *class GameServer*

### Rule 1.2: variable
The first word starts with lowercase letter. All other words start with uppercase letter.
Example: *int documentCount=0*

<font color="f00">Do not use the [http://en.wikipedia.org/wiki/Hungarian_notation Hungrarian notation]</font>

### Rule 1.3 : template
No templates should be implemented in the project. If you have no choice, discuss it on the mailing list first.

### Rule 1.4 : member
All class members must have "*`m_`*" as prefix. 
Example: _int m_clientId = 0_

### Rule 1.5 : global variable
Please, do not use global variables. If you can't do by another way use the "*`g_`*" prefix.

### Rule 1.6 : line length
Source lines must be equal or lesser than 120 characters.

### Rule 1.7 : readability
One instruction per line.
One new line between two functions.
```
 void foo()
 {
 }
 
 void bar()
 {
 }
```
### Rule 1.8 : indentation
Indentation step is four spaces. Do not use "tabs".

### Rule 1.9 : space
* Assignment:
It must have a space between the left variable and the assignment sign, same thing between the right variable.
 var1 = var2
 var1 += var2
 var1 *= var2

* Unary operators:
No space.
 *cp
 &cp
 -n

* Bi/ternary operators:
All binary and ternary operators must have space around them, except for the semicolon in a for.
 if (a % 10)
 return (cp ? cp : DEFAULT_STRING)
 for (int i = 0, int j = -1; i++; j >= 42)

* Bracket:
It must have a space between a keyword and a bracket. No space between a function name and a bracket.
 if (truc)
 while (machin)
 int fonction();
 int Classe::method(char toto, const std::string &tutu);

* Function parameters:
It must have a space after the comma, no space before.

* Chevron:
Same as bracket.
 int toto = static_cast<int>(5.4);

### Rule 1.10 : relevance
Please, use relevant identifier names. And use full English word.

### Rule 1.11 : Public, protected and private section
The class definition start with the public section, followed by the protected one and at last, the private one. 
Example:
```
 class Person
 {
 public:
    Person();
 protected:
    /*Somethings..*/
 private:
   QString* m_name;
 }
```
### Rule 1.12 : Comments   
All Comments are one a line by themselves. 
Example:
```
 int result = rand(); //bad
 //good
 int result = rand();
```
### Rule 1.13 : instruction block
The braces must be placed in the same column, on separate lines directly before and after the block. (Allman/BSD style)
Example:
```
 if (varName  name)
 {
 }
 else
 {
 }
```

### Rule 1.14 : Qt
Use Qt's classes as much as you can. Qt provides container classes, so use them.
Do not use C-style code. Rolisteam is a Qt/C++ application: no C-array, use QList or QVector instead.

### Rule 1.15: Other libraries
No libraries should be included in the project. If you have no choice, discuss it on the mailing list first.

## Code Size and Complexity

### Rule 2.1 : function size
Any one function must contain no more than 200 instruction lines.

### Rule 2.2 : Function path
Any one function can contain 20 different path or less.

Example: this function has two different path.
```
 void DrawWindows::DrawScene
 {
    if(this->visible())
    {
         /*do something*/
    }
    else
    {
        /*do something else*/
    }
 }
```

## Header Files

### Rule 3.1 : misc
Header files contain the declarations only.
Do not include unnecessary files.

### Rule 3.2 : multiple inclusions
Header files must prevent multiple inclusions of themselves.
   
### Rule 3.4 : forward declarations
Use forward declarations for any member which is either a reference or pointer.

### Rule 3.5 : naming files
Hearder files have the ".h" extension.

### Rule 3.6 : license text
Header files must start with license instructions.

### Rule 3.7 : #include
System include first, personal include after.
Include must be in alphabetical order.
 #include <bar>
 #include <foo>
 #include "barbar.h"
 #include "foofoo.h"

## Class files

### Rule 4.1 : constructor
The first function definitions have to be the constructors (the default in first).
Followed by the destructor. 

### Rule 4.2 : naming files
Class files have the .cpp extension and they have to keep the same name that the header file.
File are written with lowercase letters, because it's the default behavior of Qt Creator.
Example:
class Person
person.h
person.cpp

### Rule 4.3 : license text
cpp files must start with license instructions.

## Comments

### Rule 5.1 : Doxygen 
Each functions must be commented in the header file. Please, use Doxygen Tags as follow:

```
 /**
  * @brief Hide an internal window.
  * 
  * @param windowHandle the identifier of the window to be hide.
  * @return Whether or not the windows was successfully hidden.
  */
 bool Workspace::HideWindows(int windowHandle)
```

PS: Add @param line per parameter.

### Rule 5.2 : class 
Each class have a comment section as follow:
Example:
```
 /**
  * @brief Manage the workspace
  * @date 01/01/2010
  */
```

### Rule 5.3 : informations for others 
Feel free to add bug, warning or Todo items, in the class/function comment section.

Example :

* @bug SegFault when ....
* @warning Make sure ....
* @todo Refactoring in two functions.

## Example
Keep in mind: comments in header file explain "what the class does"
```
 /***************************************************************************
 *	Copyright (C) 2007 by Romain Campioni   			   *
 *	Copyright (C) 2009 by Renaud Guezennec                             *
 *                                                                         *
 *                                                                         *
 *   rolisteam is free software; you can redistribute it and/or modify     *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
 #ifndef DISPLAY_DISK_H
 #define DISPLAY_DISK_H
 #include <QWidget>
 /**
  *
  * @brief Display a disk
  * @version 1.0
  * @date 10/01/2009
  *                                                     
  */
 class DisplayDisk : public QWidget
 {
    Q_OBJECT
    public :
        /**
         * @brief Constructor 
         * 
         * @param parent its parent widget
         * @param fill the disk must be filled or not.
         * @param minimum set the minimum diameter
         */
        DisplayDisk(QWidget *parent = 0, bool fill = true, int minimum = 1);
    public slots :
        /**
         * @brief Change the diameter of the disk and call to redraw it
         * 
         * @param newDiameter the new diameter
         */
        void changeDiameter(int newDiameter);
    protected:
        /**
         * @brief Overwriting the paintevent. To draw the disk. 
         * 
         * @param event gathering many details about the event.
         */
        void paintEvent(QPaintEvent *event);
    private :
        /**
         * store the current diameter
         */
        int m_currentDiameter;
        /**
         * store the minimum diameter
         */
        int m_minimumDiameter;
        /**
         * store fill state
         */
        bool m_fill;
 };
 #endif
```


### Rule 5.3 : Cpp files
Feel free to add comments where you want, to explain complex instructions. Do not repeat header comment. Use Cpp comment fashion: // cool. Do not use Doxygen tags in cpp file, except if you notice a bug or any troubles.
Keep in mind, comments in cpp files explain "how it works".



## Commit on Git 
### Rule 6.1: comment
All commits have to be sent with description (The description must be in english).
The description must give the list of modifications, the ID for each bug fixed: ( issue #18) and the name of the branch: 2.0.0 or 1.0.0. It will help to generate the ChangeLog file.
Example:
[branch 2.0.0]
-Adding feature on the permission management
-Fix the issue #24 for crash when cat jumps on the keyboard
-Adding Doxygen Tag for the coffeemaker.h and coffeemaker.cpp files


## Rules for about creation of new file
### Rule 7.1 : header 
add this header to all new files:
```
 /***************************************************************************
 *	Copyright (C) $year by $name            			   *
 *                                                                         *
 *                                                                         *
 *   rolisteam is free software; you can redistribute it and/or modify     *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
```
Don't forget to replace:
$year by the current year
$name by your complete name.



PS: please, use the [[Rolisteam_mailing_list|mailing list]] to  discuss about these rules.

