from base_tests.base_test import BaseTest
from tests.pages.all_pages import *


class UITest(BaseTest):

    def test_map_page(self):
        self.home = HomePage(self.driver)
        map_page = self.home.click_map_tab()

    def test_list_page(self):
        self.home = HomePage(self.driver)
        list_page = self.home.click_list_tab()
        list_page.click_share()
        list_page.click_share()
        list_page.add_place('Singapore Zoo')
        list_page.click_place('Singapore Zoo')

    def test_places_page(self):
        self.home = HomePage(self.driver)
        places_page = self.home.click_places_tab()
        places_page.click_ok_btn()
