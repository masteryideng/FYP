from tests.pages.base_pages.base_page import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging


class PlacesPage(BasePage):

    OK = 'OK'
    PLACE = 'new UiSelector().text("%s")'

    def click_ok_btn(self):
        btn = self.driver.find_element_by_accessibility_id(self.OK)
        btn.click()
        sleep(3)
        return PlacesPage(self.driver)
