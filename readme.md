# TMSI development enviroment
---
A docker based enviroment for developing applications for online signal analysis for the tMSI amplifier.

## Prerequisite
Installed Docker

* OS X: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/
* Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/

after having docker installed pull the base image

`docker pull registry.gitlab.com/pierzchlewicz/tmsi-usb-docker`

## UNIX-likes
* running `./setup.sh`
* building `./start.sh`

## Windows
##### UNTESTED
* running `setup.bat`
* building `start.bat`

## Development
Under `./src/` one will find `app.py`, where the function `app()` lives. The function is an interface to the amplifier, allowing to work with the samples gathered.

The dev enviroment is set to use a dummy amplifier, which provides some basic functions like sin etc.

Available Functions:
* Sine
* Cosine
* Random
* Modulo




