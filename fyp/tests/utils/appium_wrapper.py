#!/usr/bin/env python
# -*- coding:utf8 -*-

from time import sleep
import subprocess
import os


def startAppium(port=4723):
    stopAppium(port)
    print 'appium_py::utils::appium_wrapper::start_appium(%s)' % port
    start_appium = 'nohup appium -p %s --log-level error &' % port
    subprocess.Popen(start_appium, shell=True)
    sleep(15)


def stopAppium(port=4723, timeout=5):
    print 'appium_py::utils::appium_wrapper::stop_appium(%s)' % port
    kill_appium = "ps axu | grep appium | grep -v grep | grep %s | awk '{print $2}' | xargs kill -9 " % port
    os.popen(kill_appium)
    sleep(timeout)
