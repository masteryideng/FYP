from tests.pages.base_pages.base_page import BasePage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import logging


class ListPage(BasePage):

    SHARE = 'closeShare'
    ADD = '//android.view.View[@content-desc="pin%sKm Link"]/android.widget.Button'
    PLACE = 'pin%sKm Link'

    def scroll_to_find(self, place, max_scroll=3):
        PLACE = self.PLACE % place
        place = self.driver.find_element_by_accessibility_id(PLACE)
        for i in xrange(max_scroll):
            if place.is_displayed():
                break
            else:
                self.scroll_down()
                continue

    def add_place(self, place):
        self.scroll_to_find(place)
        self.driver.find_element_by_xpath(self.ADD % place).click()
        sleep(3)
        return ListPage(self.driver)

    def click_place(self, place):
        self.scroll_to_find(place)
        place = self.driver.find_element_by_accessibility_id(self.PLACE % place)
        place.click()
        sleep(3)
        return ListPage(self.driver)

    def click_share(self):
        self.driver.find_element_by_accessibility_id(self.SHARE).click()
        sleep(3)
        return ListPage(self.driver)
