# This file is going to include methods that will parse
# The specific data that we need from each one of the deal boxes
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section: WebElement):
        self.boxes_section = boxes_section
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section.find_elements(By.CLASS_NAME, "a826ba81c4")

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            hotel_name = (
                deal_box.find_element(By.CSS_SELECTOR, "div[data-test-id='title']")
                .get_attribute("innerHTML")
                .strip()
            )
