from base_tests.base_test import BaseTest
import time
from PIL import Image, ImageDraw
import os


visited = []
pages = {}
clickable_number = {}
maximum_iteration_time = int(os.environ['traversal_time'])


class TraversalTest(BaseTest):

    def test_all_page(self):
        start_time = time.time()
        clickables, clickables_name, current_page = self.get_clickables()
        accessibility_id, index = self.click_current_page(current_page)
        result = self.check_after_click(current_page, index, start_time)
        if result is True:
            self.tearDown()

    def click_current_page(self, current_page):
        accessibility_id, index = self.find_not_repeated(current_page)
        if accessibility_id is None:
            return None, None
        else:
            element = self.draw_rectangle(accessibility_id, current_page)
            element.click()
            visited.append(accessibility_id)
            current_page['if_clicked'][index] = True
            return accessibility_id, index

    def check_after_click(self, previous_page, index, start_time):
        new_clickables, new_clickables_name, new_page = self.get_clickables()
        previous_page['if_all_clicked'][index] = True
        for i in range(len(new_page['if_clicked'])):
            if new_page['if_clicked'][i] is False:
                previous_page['if_all_clicked'][index] = False
        accessibility_id, index = self.click_current_page(new_page)
        time_passed = time.time() - start_time
        if accessibility_id is None or time_passed >= maximum_iteration_time:
            return True
        else:
            self.check_after_click(new_page, index, start_time)

    def get_clickables(self):
        current_page = {}
        all_page_clickables = []
        all_elements = self.driver.find_elements_by_xpath("//*")
        clickables = [item for item in all_elements if item.get_attribute('clickable') == 'true']
        clickables_name = [item.get_attribute('text') for item in clickables]
        clickables_name = [item for item in clickables_name if item != '']

        for item in pages.values():
            all_page_clickables.append(item['clickables'])
        if clickables_name not in all_page_clickables:
            self.screenshot(len(pages))
            current_page['clickables'] = clickables_name
            current_page['if_clicked'] = self.false_array(clickables_name)
            current_page['if_all_clicked'] = self.false_array(clickables_name)
            pages['page%d' % len(pages)] = current_page
        else:
            for item in pages.values():
                if item['clickables'] == clickables_name:
                    current_page = item
        return clickables, clickables_name, current_page

    def false_array(self, array):
        false_array = []
        for i in range(len(array)):
            false_array.append(False)
        return false_array

    def find_not_repeated(self, current_page):
        for i in range(len(current_page['if_clicked'])):
            if current_page['if_clicked'][i] is False:
                return current_page['clickables'][i], i
        for i in range(len(current_page['if_all_clicked'])):
            if current_page['if_all_clicked'][i] is False:
                return current_page['clickables'][i], i
        return None, None

    def screenshot(self, name):
        file_full_path = 'screenshots/traversal/page%d.png' % name
        self.driver.get_screenshot_as_file(file_full_path)

    def draw_rectangle(self, name, current_page):
        key = [k for k, v in pages.items() if v == current_page]
        page = key[0]
        path = 'screenshots/traversal/%s.png' % page
        element = self.driver.find_element_by_android_uiautomator('new UiSelector().text("%s")' % name)
        x1 = element.location['x']
        y1 = element.location['y']
        x2 = x1 + element.size['width']
        y2 = y1 + element.size['height']

        im = Image.open(path)
        draw = ImageDraw.Draw(im)
        for i in range(1, 6):
            draw.rectangle((x1 + i, y1 + i, x2 - i, y2 - i), outline='green')
        im.save(path)
        return element
