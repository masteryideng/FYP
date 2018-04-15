from tests.pages.base_pages.base_page import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging


class PlacesPage(BasePage):

    OK = 'new UiSelector().text("OK ")'
    PLACE = 'new UiSelector().text("%s")'

    def click_ok_btn(self):
        self.driver.find_element_by_android_uiautomator(self.OK).click()
        sleep(3)
        return PlacesPage(self.driver)

    def is_place_displayed(self, place):
        location = self.driver.find_element_by_android_uiautomator(self.PLACE % place)
        return location.is_displayed()

    def is_notification_displayed(self):
        notification = self.driver.find_element_by_android_uiautomator(self.OK)
        return notification.is_displayed()
