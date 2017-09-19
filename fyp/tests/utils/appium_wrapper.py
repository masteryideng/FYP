#!/usr/bin/env python
# -*- coding:utf8 -*-

from os import system
from time import sleep
import subprocess


def startAppium(port=4723):
    system('appium --port %s &' % str(port))
    sleep(15)


def stopAppium():
    system('pkill -f "node /usr/local/bin/appium"')
