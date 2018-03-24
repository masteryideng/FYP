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


def get_appium_port(min_port, max_port):
    appium_port = "ps axu | grep '/appium' | grep -v grep | grep -v WebDriverAgent | awk -F '-p' '{print $2}' | awk -F '-bp' '{print $1}' "

    temp_list = []
    for i in run_command(appium_port).split('\n'):
        if i:
            temp_list.append(i)

    area_port = [i for i in xrange(min_port, max_port + 1)]
    if temp_list:
        local_port = [int(i.strip()) for i in temp_list]
    else:
        local_port = []

    appium_port = min(list(set(area_port) - set(local_port)))
    print 'local appium port: %s' % str(local_port)
    print 'allow appium port: %s' % appium_port
    return appium_port


def run_command(command):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    retcode = p.wait()
    if retcode:

        def check_unicode(s):
            if isinstance(s, unicode):
                return s.encode('utf-8')
            return s

        command = check_unicode(command)
        stdout = check_unicode(stdout)
        stderr = check_unicode(stderr)
        raise Exception('run command (%s) failed: %d\n%s\n%s' %
                        (command, retcode, stdout, stderr))
    return stdout