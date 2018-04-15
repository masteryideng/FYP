from base_tests.base_test import BaseTest
from tests.pages.all_pages import *
from selenium.common.exceptions import NoSuchElementException


class UITest(BaseTest):

    allow_button = 'com.android.packageinstaller:id/permission_allow_button'

    def test_add_place(self):
        try:
            self.driver.find_element_by_id(self.allow_button).click()
        except NoSuchElementException:
            pass

        self.home = HomePage(self.driver)
        list_page = self.home.click_list_tab()
        list_page.add_place('Singapore Zoo')
        places_page = self.home.click_places_tab()
        self.assertTrue(places_page.is_place_displayed('Singapore Zoo'))

    def test_place_detail(self):
        try:
            self.driver.find_element_by_id(self.allow_button).click()
        except NoSuchElementException:
            pass

        self.home = HomePage(self.driver)
        list_page = self.home.click_list_tab()
        list_page.click_place('Singapore Zoo')
        self.assertTrue(list_page.is_place_displayed('Singapore Zoo'))
