#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import unittest
from appium import webdriver
from tests.pages import *
from tests.utils.appium_wrapper import startAppium, stopAppium


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):

        startAppium()
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'CB5A26TG3E'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'
        desired_caps['appPackage'] = 'com.android.calculator2'
        # desired_caps['noReset'] = True
        desired_caps['newCommandTimeout'] = 0
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
        stopAppium()
