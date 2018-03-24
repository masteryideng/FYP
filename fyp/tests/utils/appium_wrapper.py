#!/usr/bin/env python
# -*- coding:utf8 -*-

from time import sleep
import subprocess
import os
from fancy_log import fancy_log


def startAppium(port):
    stopAppium(port)
    fancy_log(port=port)
    start_appium = 'nohup appium -p %s > nohup-%s.out &' % (port, port)
    max_retry = 100
    retry = 0
    f = None
    server_log = os.path.abspath('./nohup-%s.out' % port)
    fancy_log(logfile=server_log)
    subprocess.Popen(start_appium, shell=True)
    while retry < max_retry:
        try:
            f = open(server_log, 'r')
            if f.read():
                print 'Appium Server started !'
                break
            else:
                print 'Appium Server Initialing...'
        except IOError:
            print 'Waiting for Appium Server...'
        finally:
            retry += 1
            sleep(3)
            if f:
                f.close()
    sleep(3)


def stopAppium(port, timeout=5):
    fancy_log(port=port)
    kill_appium = "ps axu | grep appium | grep -v grep | grep %s | awk '{print $2}' | xargs kill -9 " % port
    os.popen(kill_appium)
    sleep(timeout)
