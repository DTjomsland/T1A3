#!/bin/bash
# Checks to see if python 3 is intalled
# Exits after error so the user is not overwhelmed with errors all at once.
if ! [[ -x "$(command -v python3)" ]];
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' 
  exit 1
fi
# Checks to see if colorama module is intalled
if ! [[ $(pip3 freeze | grep 'colorama') ]];
then
  echo 'Error: 
    This program utilizes the module: colorama, but it looks like colorama is not installed.
    Type "pip3 install colorama" to install module.'
  exit 1
fi
# Checks to see if art module is intalled
if ! [[ $(pip3 freeze | grep 'art') ]];
then
  echo 'Error: 
    This program utilizes the module: art, but it looks like art is not installed.
    Type "pip3 install art" to install module.'
  exit 1
fi
# Checks if the user needs extra help before starting the program
echo -n "Type 'help' for application installation instructions or hit enter to continue to app: "
read var
if [ $# -eq 0 ] && [ "$var" == "help" ]; 
then
  cat help.txt
else
  python3 app.py
fi