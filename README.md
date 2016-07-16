# Musebot Template for Python

_**Note: This template is a work in progress and currently does not work in any way, shape, or form!**_  
_**Note: This template has only been tested under OS X, Python 2.7.12+, and Pyo 0.8.0**_

A template for creating MusebBots in Python. This template uses [Pyo](http://ajaxsoundstudio.com/) for synthesis and OSC communication.

## Installation

1.  a. If you don't have Git installed, start by [downloading](https://github.com/tribayf/py-musebot-template/archive/master.zip) this repository from Github.  
    b. If you do have git installed, open Terminal and clone the repo to an appropriate directory:

    ```
    cd <dir>
    git clone https://github.com/tribayf/py-musebot-template.git
    ```

2. Run the install script:

    ```
    cd py-musebot-template
    ./install.sh
    ```

    This will prompt you to install Homebrew and/or Git if not found on your computer. You will also be prompted to enter your password to install Pyo itself.

3. Pyo will be installed system-wide and you can now import it into any Python 2 project.

### Dependencies

Template Dependencies:
- Homebrew (http://brew.sh/)
- Git (https://git-scm.com/)
- Python 2.7.x (https://www.python.org/)
- Pyo (http://ajaxsoundstudio.com/)

Pyo dependencies:
- liblo (http://liblo.sourceforge.net/)
- libsndfile (http://www.mega-nerd.com/libsndfile/)
- portaudio (http://www.portaudio.com/)
- portmidi (http://portmedia.sourceforge.net/portmidi/)
- wxPython (https://wxpython.org)

## Using the template

0. Familiarize yourself with how to work with MuseBots by checking out the info links below.
1. Copy the template directory into your `Musebots` directory (you do not need to copy the `pyo` directory). Rename template directory to be that which you will be calling your new MuseBot (e.g. noisebot). You may want to prefix the name with your initials to distinguish it from other people's MuseBots and to keep all of your Musebots together as you start building a collection (e.g. tb_noisebot).
2. Open the `config.txt` file and change the first line to `id <name>` so that `<name>` matches that of the containing directory (e.g. `id tb_noisebot`).
3. Define your MuseBot in `musebot.py`

## Caveats

- Currently Pyo can only be used with Python 2.6/2.7, and this template targets Python 2.7 only.

## More Info

- [Musebots](http://musicalmetacreation.org/musebots/)
- [MuseBot communication spec](https://docs.google.com/document/d/1UtdLYsOErzXKNFxrM7utHeFXgPNcC_w40lTtUxtCYO8)
- [Pyo](http://ajaxsoundstudio.com/software/pyo/)
