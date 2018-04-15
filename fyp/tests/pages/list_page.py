from tests.pages.base_pages.base_page import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging


class ListPage(BasePage):

    SHARE = 'new UiSelector().textContains("share")'
    PLACE = 'new UiSelector().text("%s")'

    def add_place(self, place):
        location = self.driver.find_element_by_android_uiautomator(self.PLACE % place)
        center = self.get_element_center(location)
        new_center = [center[0]+435, center[1]+24]
        self.driver.tap(new_center, 1)
        sleep(3)
        return ListPage(self.driver)

    def click_place(self, place):
        self.driver.find_element_by_android_uiautomator(self.PLACE % place).click()
        sleep(3)
        return ListPage(self.driver)

    def click_share(self):
        self.driver.find_element_by_android_uiautomator(self.SHARE).click()
        sleep(3)
        return ListPage(self.driver)

    def is_detail_displayed(self, place):
        location = self.driver.find_element_by_android_uiautomator(self.PLACE % place)
        return location.is_displayed()
