from tests.pages.base_pages.base_page import BasePage
from .map_page import MapPage
from .places_page import PlacesPage
from .list_page import ListPage
from time import sleep


class HomePage(BasePage):

    MAP = 'tab-t0-0'
    PLACES_TO_VISIT = 'tab-t0-1'
    SELECTED_PLACE = 'tab-t0-2'

    def click_map_tab(self):
        self.driver.find_element_by_id(self.MAP).click()
        sleep(3)
        return MapPage(self.driver)

    def click_list_tab(self):
        self.driver.find_element_by_accessibility_id(self.PLACES_TO_VISIT).click()
        sleep(3)
        return ListPage(self.driver)

    def click_places_tab(self):
        self.driver.find_element_by_accessibility_id(self.SELECTED_PLACE).click()
        sleep(3)
        return PlacesPage(self.driver)
