import os
from tkinter.messagebox import NO
import typing
import types
import booking.constants as const
from utils import utils
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path: str = r"C:/selinumDrivers", teradown: bool = False):
        self.driver_path = driver_path
        self.teardown = teradown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]],
        exc: typing.Optional[BaseException],
        traceback: typing.Optional[types.TracebackType],
    ):
        if self.teardown:
            self.quit()

    def land_first_page(self) -> None:
        self.get(const.BASE_URL)

    def change_currency(self, currency: str = None) -> None:
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]',
        )
        selected_currency.click()

    def select_place_to_go(self, place_to_go: str) -> None:
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_date(self, check_in_date: str, check_out_date: str) -> None:
        difference = utils.month_difference(check_in_date, check_out_date)

        # TODO: rewrite this block as function
        # same panel
        check_in_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]'
        )

        check_out_element.click()

    # Helper method
    def filter_children(self, count: int) -> None:
        selector = self.find_element(
            By.CSS_SELECTOR,
            'button["aria-label="Increase number of Children"]'
        )
        for _ in range(count):
            selector.click()

    def filter_rooms(self, count: int) -> None:
        selector = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Rooms"]'
        )
        for _ in range(count - 1):
            selector.click()

    def select_filter_adult(self, count_adult: int = 1) -> None:
        selector_element = self.find_element(By.ID, "xp__guests__toggle")
        selector_element.click()

        while True:
            decrease_adult = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adult.click()
            # Break loop when adult number is 1
            number_element = self.find_element(By.ID, "group_adults")
            if int(number_element.get_attribute("value")) == 1:
                break

        increae_adult = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
        )
        for _ in range(count_adult - 1):
            increae_adult.click()

    # TODO: write a wrapper for all the filters
    def pick_filters(adult: bool = True, children: bool = True, rooms: bool = True) -> None:
        pass

    def sumbit_search(self) -> None:
        submit_element = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_element.click()
