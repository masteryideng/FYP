from tests.pages.base_pages.base_page import BasePage


class MapPage(BasePage):

    OFFLINE = 'Internet not detected :('

    def is_offline(self):
        offline = self.driver.find_element_by_accessibility_id(self.OFFLINE)
        return offline.is_displayed()
