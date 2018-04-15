from base_tests.base_test import BaseTest
from tests.pages.all_pages import *
from selenium.common.exceptions import NoSuchElementException


class UITest(BaseTest):

    def test_add_place(self):
        self.home = HomePage(self.driver)
        try:
            self.home.click_allow_button()
        except NoSuchElementException:
            pass
        list_page = self.home.click_list_tab()
        list_page.add_place('Botanic Garden')
        places_page = self.home.click_places_tab()
        self.assertTrue(places_page.is_place_displayed('Botanic Garden'))

    def test_place_detail(self):
        self.home = HomePage(self.driver)
        try:
            self.home.click_allow_button()
        except NoSuchElementException:
            pass
        list_page = self.home.click_list_tab()
        list_page.click_place('Botanic Garden')
        self.assertTrue(list_page.is_detail_displayed('Botanic Garden'))

    def test_share(self):
        self.home = HomePage(self.driver)
        try:
            self.home.click_allow_button()
        except NoSuchElementException:
            pass
        list_page = self.home.click_list_tab()
        list_page.click_share()
        self.assertTrue(list_page.is_facebook_displayed())

    def test_empty_places(self):
        self.home = HomePage(self.driver)
        try:
            self.home.click_allow_button()
        except NoSuchElementException:
            pass
        places_page = self.home.click_places_tab()
        self.assertTrue(places_page.is_notification_displayed())
