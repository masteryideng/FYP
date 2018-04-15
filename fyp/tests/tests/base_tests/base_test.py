#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import unittest
from appium import webdriver
from tests.pages import *
from time import sleep
from tests.utils.appium_wrapper import *
import random


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """Basis for all tests."""

    # appium
    MAX_RETRY = 100
    APPIUM_MIN_PORT = 4000
    APPIUM_MAX_PORT = 5000
    # WDA
    WDA_MIN_LOCAL_PORT = 8000
    WDA_MAX_LOCAL_PORT = 9000

    @classmethod
    def setUpClass(cls):
        port = random.randint(cls.APPIUM_MIN_PORT, cls.APPIUM_MAX_PORT)
        server_log = os.path.abspath('./nohup-%s.out' % port)
        if os.path.isfile(server_log):
            os.remove(server_log)
        cls.appium_port = port
        startAppium(cls.appium_port)

    @classmethod
    def tearDownClass(cls):
        stopAppium(cls.appium_port)

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = os.environ['platformVersion']
        desired_caps['deviceName'] = os.environ['deviceName']
        desired_caps['app'] = os.environ['app']

        url = 'http://0.0.0.0:%s/wd/hub' % self.appium_port
        self.driver = webdriver.Remote(url, desired_caps)

        try:
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()

    '''
    port = 4723

    def setUp(self):

        startAppium(self.port)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = os.environ['platformVersion']
        desired_caps['deviceName'] = os.environ['deviceName']
        desired_caps['app'] = os.environ['app']
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, desired_caps)
        sleep(10)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
        stopAppium(self.port)'''
