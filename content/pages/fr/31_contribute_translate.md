Title: Translate
Date: 2017-06-11 10:20
slug: take-part-translate
status: hidden
lang: fr

# Contact us

You want to help translating **Rolisteam** but you are a bit lost. 
Don't worry, just [contact us]({filename}26_contactUs.md).

# Translation

## Rolisteam or RCSE

If you want to help to translate rolisteam. Please take a look at :
[https://www.transifex.com/projects/p/rolisteam/](https://www.transifex.com/projects/p/rolisteam/)

* Create an account (or use your existing one)
* Make new language resquest in rolisteam project.

Then, I will create the new langage in rolisteam and set your account as
translator for this language. After this step, you will be able to
translate rolisteam through the transifex web site. You may download you
translation and ask rolistem to load it.

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


[Back]({filename}30_TakePart.md)
