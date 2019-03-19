Title: Take part
Date: 2017-06-11 10:20
slug: take-part-ux
status: hidden
lang: fr

# How to help

**Rolisteam** needs attention in many domains.
It is always appreciated.

# Contact us

You want to help but don't how. The first step is to [contact us]({filename}26_contactUs.md).
It is better to plan together what to do.

# Source code

Interested in writing **Rolisteam** code.
**Rolisteam** is written in C++(11) and it is based on Qt5 framework. its source code is managed on github. We use git.

[Official Rolisteam Page](https://github.com/Rolisteam/rolisteam)

Depending on how deep you want to be in **Rolisteam** development, there is two main ways to contribute.

## Alone programmer

This approach is great for people who want to implement one feature or fix few stuff.
The workflow is simple:

1. Get a github account
2. Fork rolisteam and its submodules (common, diceparser, charactersheet, RPlugins), all projets appears on your github profile
3. clone those git project on your computer.
4. Write the modification
5. Test the modification
6. Make "pull request"

## Be part of the project

1. Get a github account
2. Ask to be part of Rolisteam's team
3. When its granted you can clone official rolisteam repositories (and its subproject)
4. Write your code and commit your change.

To show your motivation is a good start to contribute several times as programmer. Then ask to be part of the team.


Please take a look here to compile it on [windows]({filename}27_compileWindow.md), on [Linux]({filename}29_compileLinux.md), on [MacOsX]({filename}28_compileMacOs.md).
The page should have all needed information.

Don't hesitate to contact us to speak about your intensions. So we can support your effort.

To know what to do on **Rolisteam**, there is a [development roadmap](https://docs.google.com/spreadsheets/d/18jDGViuOm6KjqEAumW1RU2qccQQ4-TxiXPtAg0X_M2o/edit#gid=769324568).

# Ux design or graphics design

Please, [contact us]({filename}26_contactUs.md).

# Translation

## Rolisteam 

We give information about **translating rolisteam** in the [last section of this page]({filename}24_translation.md)

## Documentation

Translated documentation is really helpful and it just requires few steps to work autonomously.
First, learn how to write in [markdown](https://en.wikipedia.org/wiki/Markdown).

Secondly, it is important to use [Git hub](https://github.com/Rolisteam/Documentation).

1. Create a [github account](https://github.com)
2. [Fork](https://github.com/Rolisteam/Documentation#fork-destination-box) the documentation.
3. Modify the documentation inside your git repository. Github provides preview on markdown file.
4. Make pull request to share your work.

In details, the second step will create a copy of the documentation into your own github account.
So you have permission to do whatever you want on the documentation: fix it, improve it and so on.
When the work is finished, you can create a pull request from your documentation copy to rolisteam's documentation. Then, modifications are reviewed. If they look good. The pull request is accepted and your modification are now integrated inside the official documetation.

### Translate the documentation in new language

Do the first three steps above and those following:

1. Create new directory inside `content\pages` and name it with the [639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).
2. Dupplicate all the page, pay attention to change the first four lines of each file.
3. Translate files
4. Make pull request to share your work

### Generated the documentation

The documentation is generated in html thank of [Pelican](https://blog.getpelican.com/).
1. Install it
2. Get the documentation project:  
    `clone https://github.com/Rolisteam/Documentation.git`
Adapt the url to your github account if needed.
3. Change project configuration to adapt it to your installation of Pelican.
4. Install required plugin and theme to get the exact same aspect of online **Rolisteam** documentation.
5. Generate html: 
> make html

It is better to generate the documentation to see the final result. It may be difficult to set all the required tools. When doing a pull request, don't forget to tell us that you did not test the generation.

# Promotion

Talk about **Rolisteam** as often as possible.

Don't hesitate to contact us to explain your initiative. We will be glad to talk about your videos, tutorials or games.


<p style="text-align: left; width:49%;  display: inline-block;"><a href="/contactus.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/">Home</a></p>

