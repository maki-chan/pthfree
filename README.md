# pthfree

Introduction
------------

Downloads all current freeleech torrents from PTH.

The following command will request every freeleech torrent currently on PTH via its API and download the \*.torrent files to the chosen target directory. You can choose to only download FLAC files, MP3 V0 or MP3 320 files if you wish.

Installation
------------

You need to install some requirements before using pthfree.

To begin with, you need to install **Python 3.x** in order to use pthfree (untested on Python 2.x).

Once you've got Python installed, you will need one module: requests. Try this as sudo/root:

    # pip install -r requirements.txt

Or without sudo:

    $ pip install --user -r requirements.txt

You can also install it directly via pip as sudo/root:

    # pip install requests

Or without sudo:

    $ pip install --user requests

Alternatively, if you have setuptools installed, you can do this (in the source directory):

    $ python setup.py install

This should theoretically install the required dependency automatically. 

At this point you may execute the following command:

    $ pthfree

If everything is done right, you should get a notice that you have to provide your username via command line. Look to the configuration section further down for more instructions.

If you have an error, try to setup chmod 777 on all files, even maybe on the directory (it's possible you have to try this as sudo/root):

    $ chmod 777 *

Configuration
-------------

If you are here, that means, you can already run the script and only need to do the configuration once and you are good to go, hooray!

To configure pthfree, have a look at the help screen which you can bring up yourself by typing the following:

    $ pthfree -h

This is the help screen:

    usage: pthfree [-h] [-u USER] [-p PASSWORD] [-d DIRECTORY] [-f]
                   [--flac-only | --mp3-v0-only | --mp3-320-only]

    Downloads all freeleech torrents from PTH

    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  stores a new username in the config file
      -p PASSWORD, --password PASSWORD
                            stores a new password in the config file
      -d DIRECTORY, --directory DIRECTORY
                            stores a new .torrent target directory in the config
                            file
      -f, --force           overwrites already existing .torrent files
      --flac-only           only downloads FLAC torrents (including 24 bit)
      --mp3-v0-only         only downloads V0 torrents
      --mp3-320-only        only downloads MP3 320 torrents

As you can see, there are several options you can use when you want to download freeleech torrents (e.g. you can use `--flac-only` to only download FLAC torrents and no MP3 torrents at all).

To configure pthfree, you need to provide your PTH username, your password and the torrent file output directory (target directory) at least once, for example like so:

    $ pthfree -u IamNobody -p IhaveNoPassword -d /this/is/my/torrent/file/directory

If you have done that once and pthfree ran without any problems, congratulations! You don't need to run pthfree with those arguments all over again. Just run this in the future:

    $ pthfree

It will work without any problems (all values are stored in your user directory under `.pthfree/config` in **cleartext**, so be sure nobody can access this file except yourself, otherwise your password may be leaked!). You can provide those configuration switches again, though, if you want to change anything and don't like to change the values in the configuration file.

One last thing: The --*format*-only switches are not stored in the configuration, so if you used `pthfree --flac-only` the last time, the next run with only `pthfree` will download every freeleech torrent, including MP3 files.
