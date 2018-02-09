# Musebot Template for Python

_**Note: Template tested under macOS 10.12.6, Python 3.6, and Pyo 0.8.9**_

A template for creating [Musebots](http://musicalmetacreation.org/musebots/) in Python, using [Pyo](http://ajaxsoundstudio.com/) for synthesis and OSC communication.

## Tempate Dependencies

- Python 3.6.x
- Pyo 0.8.9
- wxPython 4.0

## Installation

1. Install Pyo via the installer located [here](http://ajaxsoundstudio.com/software/pyo/) [Recommended]. If you are apt to compile from source you probably know what you are doing. Instructions can be found [here](http://ajaxsoundstudio.com/pyodoc/compiling.html).

   Users running macOS you will probably get an alert saying that Pyo is from an unidentified developer. Open the Security & Privacy tab in System Preferences and click the `Open Anyway` button to proceed with the installation.

2. Pyo will be installed system-wide and you can now import it into any Python 3 project.

## Using the template

0. Familiarize yourself with how to work with Musebots by checking out the info links below.
1. Place a copy of the template directory into your `Musebots` directory. Rename template directory to that which you will be calling your new Musebot (e.g. tb_noisebot). Prefixing the name with your initials to distinguish it from other people's Musebots is generally a good idea.
2. Open the `config.txt` file and change the first line to `id <name>` so that `<name>` matches that of the containing directory (e.g. `id tb_noisebot`).
3. Define your Musebot in `musebot.py`

## More Info

- [Musebots](http://musicalmetacreation.org/musebots/)
- [Musebot Communication Spec](https://docs.google.com/document/d/1UtdLYsOErzXKNFxrM7utHeFXgPNcC_w40lTtUxtCYO8)
- [MuMe Mailing list](https://groups.google.com/forum/#!forum/musicalmetacreation)
- [Pyo](http://ajaxsoundstudio.com/software/pyo/)
