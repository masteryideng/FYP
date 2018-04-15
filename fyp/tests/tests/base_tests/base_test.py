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

    port = 4723

    @classmethod
    def setUpClass(cls):
        startAppium(cls.port)

    @classmethod
    def tearDownClass(cls):
        stopAppium(cls.port)

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = os.environ['platformVersion']
        desired_caps['deviceName'] = os.environ['deviceName']
        desired_caps['app'] = os.environ['app']

        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, desired_caps)

        try:
            self.driver.switch_to.alert.accept()
        except Exception:
            pass

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
