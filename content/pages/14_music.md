Title: Music Player
Date: 2017-06-11 10:20
slug: music
status: hidden
lang: en

![Complete Music Widget]({static}/images/panel/Background_Music_en_006.png)


# Overview

![MusicSolo]({static}/images/en/3_audio_players.jpg)

Please pay attention to all action buttons (from left to right):

-   Play
-   Pause
-   Stop
-   Playing mode: one file (and stop playing at the end)
-   Playing mode: playing the file again and again.
-   Add: You may open audio files (one or many), Playlist files, remote stream url, or load the playlist from [tabletopaudio.com](http://tabletopaudio.com)
-   Save your playlist with any kind of media (local file or stream)
-   Remove media : remove one media or all.

## Actions

![Menu contextuel]({static}/images/tuto/27_music_contextual_menu_en.jpg)

The contextual menu shows all actions. Some of them have shorcuts, offering direct access to this actions.

It is possible to hide one, two or all players (any of them).

* Play current file
* Pause
* Stop
* Add file
* Add Stream
* Open Playlist
* Load TableTopAudio.com playlist
* Save playlist
* Clean list
* Remove file from the list

## Open file, playlist or URL

Audio players in rolisteam may open file from user's computer. They can also load playlist. They can also load stream or remote file.

### Example:

* remote file: http://myOwnWebServer.com/music/village.mp3
* Local file: c:\My Documents\audio\village.mp3
* Local Playlist: c:\My Documents\audio\rpg_playlist.m3u

## Drag and Drop



It is possible to drag and drop files onto player widgets. The files are added to the list. The items are put at your cursor position.
Horizontal line appears. You may also directly drop file in the main window. Then, they are added to the first player.

## Three tracks at the same time



By default, rolisteam has 3 music players.
They are completely seperated to one another. It allows you to have background music, sound effects and environment sounds at the same time.
The goal is to improve the experience.

## Streaming music

Rolisteam is not streaming any audio files. It send stream information (such as URL) or filename to play. If you want to play your own audio files.
You must send them to each of your players. Your players must put them into one directory and then, set the directory as music directory in audio player.
Each audio player has it own directory.

Rolisteam can not be used as streaming server. So, music files are not
transferred to each players. There are two reasons for that:

* Bandwidth issue
* This feature would make rolisteam a piracy software according to french laws.


## Play music from TableTopAudio.com

Rolisteam provides a playlist with many background music from [TableTopAudio.com](TableTopAudio.com).
This playlist can be loaded from the contextual menu.

![TableAudio.com]({static}/images/)

# Music Player when I'm a player (no GM)

When rolisteam is in player mode (instead of GM), The music player shows lesser elements.
It provides a text field to indicate error message. When there is no error, it hides the filename.
A folder button is available to define the root directory to check. And player user can also manage the volume.

# File format ?

Rolisteam uses platform specific backend to play sound file. Which means the supported file formats are the same as default audio player.

## Windows

On windows, it is recommended to install: [https://xiph.org/dshow/](https://xiph.org/dshow/)

## Linux

Please install gstreamer backend for QtMultimedia.


<p style="text-align: left; width:49%;  display: inline-block;"><a href="/npcmaker.html">Previous</a></p>
<p style="text-align: right; width:50%;  display: inline-block;"><a href="/images.html">Next</a></p>
