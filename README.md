# Rolisteam Documentation Website

## What you'll need

1. Python : versions 3.6 and up are supported
2. virtualenvwrapper : https://virtualenvwrapper.readthedocs.io/en/stable/install.html


## Get the code

```
$ git clone --recurse-submodules git@github.com:Rolisteam/Documentation.git
$ cd Documentation 
```

## Installation

```
$ mkvirtualenv roli
$ pip install -r requirements.txt
```

## Runing the dev server

```
$ pelican -lr
```

Now open http://localhost:8000 in your browser