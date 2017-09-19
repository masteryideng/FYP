#!/usr/bin/env python
# -*- coding:utf8 -*-

from tests.pages.base_pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
import logging


class HomePage(BasePage):

    RESULT = 'com.android.calculator2:id/result'

    def click_btn(self, BTN):
        try:
            btn = self.driver.find_element_by_id(BTN)
            btn.click()
        except NoSuchElementException as e:
            logging.warning('HomePage::click_btn::%' % e.msg)

    def is_result_correct(self, ans):
        result = self.driver.find_element_by_id(self.RESULT).get_attribute('text')
        return int(result) == ans
