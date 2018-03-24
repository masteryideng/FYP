#!/usr/bin/env python
# -*- coding:utf8 -*-

import os
import unittest
from appium import webdriver
from tests.pages import *
from time import sleep
from tests.utils.appium_wrapper import *
from selenium.common.exceptions import NoSuchElementException


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    APPIUM_MIN_PORT = 4450
    APPIUM_MAX_PORT = 4499
    appium_port = get_appium_port(APPIUM_MIN_PORT, APPIUM_MAX_PORT)

    def setUp(self):

        stopAppium(self.appium_port)
        startAppium(self.appium_port)
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = os.environ['platformVersion']
        desired_caps['deviceName'] = os.environ['deviceName']
        desired_caps['app'] = os.environ['app']
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.appium_port, desired_caps)
        sleep(10)

        try:
            self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        except NoSuchElementException:
            pass

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
        stopAppium(self.appium_port)
