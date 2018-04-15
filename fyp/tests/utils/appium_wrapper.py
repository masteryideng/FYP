#!/usr/bin/env python
# -*- coding:utf8 -*-

from time import sleep
import subprocess
import os


def startAppium(port=4723):
    stopAppium(port)
    os.system('appium --port %s --log-level error  &' % port)
    sleep(20)


def stopAppium(port=4723, timeout=5):
    kill_appium = "ps axu | grep appium | grep -v grep | grep %s | awk '{print $2}' | xargs kill -9 " % port
    os.popen(kill_appium)
    sleep(timeout)
