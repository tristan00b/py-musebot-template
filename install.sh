################################################################################
#
# file:    install.sh
# author:  Tristan Bayfield
# created: July 09, 2016
#
# Installs dependencies for the Python Musebot template. This script requires an
# administrator's password to build Pyo with Jack Audio.
#
# Dependencies:
#   - Homebrew (http://brew.sh/)
#   - Python (https://www.python.org/)
#   - python-osc (https://pypi.python.org/pypi/python-osc)
#   - Git (https://git-scm.com/)
#   - Pyo (http://ajaxsoundstudio.com/)
#       - liblo (http://liblo.sourceforge.net/)
#       - libsndfile (http://www.mega-nerd.com/libsndfile/)
#       - portaudio (http://www.portaudio.com/)
#       - portmidi (http://portmedia.sourceforge.net/portmidi/)
#       - wxPython (https://wxpython.org)
#
################################################################################
#!/usr/bin/env bash

BREW_PATH=`which brew`

# Install Homebrew
if [[ -z $BREW_PATH ]]; then
    read -p 'Homebrew not found. Install it? [Y/n] ' response
    if [[ $response =~ ^$|^[Yy]$ ]]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    else
        echo 'Homebrew is required to continue the installation.'
        exit 1
    fi
else
    echo -e 'Found Homebrew: '$BREW_PATH
fi

echo 'Updating homebrew...'
brew update

echo 'Installing dependencies...'
brew install python git liblo libsndfile portaudio portmidi wxpython

echo 'Building Pyo...'
if [ ! -d "./pyo" ]; then
    git clone https://github.com/belangeo/pyo.git
fi
if [ -d "./pyo/build" ]; then
    sudo rm -rf "./pyo/build"
fi
cd pyo
sudo python setup.py install --use-coreaudio --use-double --use-jack
echo
