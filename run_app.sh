#!/bin/bash
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' 
  exit 1
fi

if ! [[ $(pip3 freeze | grep 'colorama') ]]; 
then
  echo 'Error: 
    This program utilizes the module: colorama, but it looks like colorama is not installed.
    Type "pip3 install colorama" to install module.'
  exit 1
fi

if ! [[ $(pip3 freeze | grep 'art') ]]; 
then
  echo 'Error: 
    This program utilizes the module: art, but it looks like art is not installed.
    Type "pip3 install art" to install module.'
  exit 1
fi

python3 app.py