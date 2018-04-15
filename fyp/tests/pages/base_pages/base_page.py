#!/usr/bin/env python
# -*- coding:utf8 -*-
import time
import os


class BasePage:
    """The basis for all pages."""
    IMPLICIT_WAIT_TIME = 10
    TIMEOUT = 30

    def __init__(self, driver):
        """Base constructor.

        Sets driver, implicit wait, and timeout.
        """
        self.driver = driver
        self.driver.implicitly_wait(self.IMPLICIT_WAIT_TIME)
        self.timeout = self.TIMEOUT
        self.screenshot()

    def screenshot(self):
        file_full_path = 'screenshots/ui/%s_%s.png' % (self.get_name(), str(time.time()))
        self.driver.get_screenshot_as_file(file_full_path)

    def get_name(self):
        return self.__class__.__name__

    def scroll_down(self):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width*0.5, height*0.75, width*0.5, height*0.25, 1000)
        time.sleep(3)
        self.screenshot()

    def get_element_center(self, element):
        """Calculates the center of inputted element and returns it as a tuple (x, y)."""
        element_mid_width = element.size['width'] / 2
        element_mid_height = element.size['height'] / 2
        return element.location['x'] + element_mid_width, element.location['y'] + element_mid_height