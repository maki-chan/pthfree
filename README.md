# pthfree [![Build Status](https://travis-ci.org/maki-chan/pthfree.svg?branch=master)](https://travis-ci.org/maki-chan/pthfree)

Introduction
------------

Notifies you about new freeleech torrents from PTH.

The following command will request every freeleech torrent currently on PTH via its API and checks if you were already
notified about the freeleech torrent in the past. If you weren't, the application sends you a notification that you
should look at the freeleech section at PTH.

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

If everything is done right, you should get a notice that you have to provide your username via command line. Look to
the configuration section further down for more instructions.

If you have an error, try to setup chmod 777 on all files, even maybe on the directory (it's possible you have to try
this as sudo/root):

    $ chmod 777 *

Configuration
-------------

If you are here, that means, you can already run the script and only need to do the configuration once and you are good
to go, hooray!

To configure pthfree, have a look at the help screen which you can bring up yourself by typing the following:

    $ pthfree -h

This is the help screen:

    usage: pthfree [-h] [-u USER] [-p PASSWORD] [--smtp | --no-smtp]
                   [--pushover | --no-pushover] [--pushbullet | --no-pushbullet]
                   [--pushover-api-token PUSHOVER_API_TOKEN]
                   [--pushover-user-key PUSHOVER_USER_KEY]
                   [--pushbullet-token PUSHBULLET_ACCESS_TOKEN]
                   [--smtp-server SMTP_SERVER] [--smtp-port SMTP_PORT]
                   [--smtp-tls | --no-smtp-tls] [--smtp-user SMTP_USER]
                   [--smtp-password SMTP_PASSWORD] [--smtp-email SMTP_EMAIL]
                   [-s SEND_TO] [-q]
                   [--flac-only | --mp3-v0-only | --mp3-320-only]
    
    Notifies you about new freeleech torrents from PTH
    
    optional arguments:
      -h, --help            show this help message and exit
      -u USER, --user USER  stores a new username in the config file
      -p PASSWORD, --password PASSWORD
                            stores a new password in the config file
      --smtp                use smtp (mail) as notification API
      --no-smtp             don't use smtp (mail) as notification API
      --pushover            use Pushover as notification API
      --no-pushover         don't use Pushover as notification API
      --pushbullet          use Pushbullet as notification API
      --no-pushbullet       don't use Pushbullet as notification API
      --pushover-api-token PUSHOVER_API_TOKEN
                            stores a new Pushover API token in the config file
      --pushover-user-key PUSHOVER_USER_KEY
                            stores a new Pushover user key in the config file
      --pushbullet-token PUSHBULLET_ACCESS_TOKEN
                            stores a new Pushbullet access token in the config
                            file
      --smtp-server SMTP_SERVER
                            stores a new smtp server in the config file
      --smtp-port SMTP_PORT
                            stores a new smtp server port in the config file
      --smtp-tls            stores that the smtp server uses SSL/TLS in the config
                            file
      --no-smtp-tls         stores that the smtp server does not use SSL/TLS in
                            the config file
      --smtp-user SMTP_USER
                            stores a new smtp server user in the config file
      --smtp-password SMTP_PASSWORD
                            stores a new smtp server password in the config file
      --smtp-email SMTP_EMAIL
                            stores a new FROM mail address for the smtp server
      -s SEND_TO, --send-to SEND_TO
                            stores a new TO mail address for the notification
                            emails
      -q, --quiet           don't send any email, just collect and save freeleech
                            torrents (useful if you already downloaded all current
                            freeleeches)
      --flac-only           only downloads FLAC torrents (including 24 bit)
      --mp3-v0-only         only downloads V0 torrents
      --mp3-320-only        only downloads MP3 320 torrents

As you can see, there are several options you can use when you want to get notified about freeleech torrents (e.g. you
can use `--flac-only` to only be notified about FLAC torrents and no MP3 torrents at all).

To configure pthfree, you need to provide your PTH username and your password.

Furthermore, if you want notifications via mail, you need to provide a smtp server, the port of the smtp server, the
smtp user, the smtp password, the sender address (FROM) and the recipient address (TO) at least once, for example like
so (please note that you have to turn on the smtp notifications once too):

    $ pthfree --smtp -u IamNobody -p IhaveNoPassword --smtp-server mail.example.com --smtp-port 25 --smtp-user nobody --smtp-password NobodysPassword --smtp-email nobody@example.com -s your@email.com

If you want to turn on Pushover notifications, you need to create a new application with its own api token over at
[Pushover](https://pushover.net). Then you have to provide both, your app token and the user key to this application.
The user key is used as a "receiver", while the app token is used as the "sender". Here you can see an example (don't
forget to provide your PTH username and your password if you haven't already done so before; also tell pthfree at least
once that you want to enable Pushover notifications):

    $ pthfree --pushover -u IamNobody -p IhaveNoPassword --pushover-api-token fvr02if84cgxrv19c2m1fivj0nz43g --pushover-user-key ch4rz5whyop98gx45blzb5j6u4cxu6

If you want to turn on Pushbullet notifications, you need to create a new access token at
[Pushbullet](https://www.pushbullet.com/). Then you have to provide this token to pthfree. The token is used for both,
"receiver" and "sender", so you are sending those notifications officially from yourself to yourself. Have an example
here (don't forget to provide your PTH username and your password if you haven't already done so before; also tell
pthfree at least once that you want to enable Pushbullet notifications):

    $ pthfree --pushbullet -u IamNobody -p IhaveNoPassword --pushbullet-token o.NFT3td8UDpBn4URK6vyufaZI9Ttewy09

If you have done that once and pthfree ran without any problems, congratulations! You don't need to run pthfree with
those arguments all over again. Just run this in the future:

    $ pthfree

It will work without any problems (all values are stored in your user directory under `.pthfree/config` in
**cleartext**, so be sure nobody can access this file except yourself, otherwise your password may be leaked!). You can
provide those configuration switches again, though, if you want to change anything and don't like to change the values
in the configuration file.

**PRO TIP:** pthfree is best run as a cron job on your seedbox (or another suitable server).

**PRO TIP 2:** pthfree is able to provide you with notifications via all its notification APIs at once if you switched
all of them on!

One last thing: The --*format*-only switches are not stored in the configuration, so if you used `pthfree --flac-only`
the last time, the next run with only `pthfree` will download every freeleech torrent, including MP3 files.
