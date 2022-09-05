import os
import typing
import types
import booking.constants as const
from utils import utils
from utils import actions
from typing import List, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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

    ## Helper methods for filtering the input
    def __filter_children(self, count: int, age: List[int]) -> None:
        if (actions.check_args(count, age) and actions.check_age(age)):
            selector = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]'
            )
            for i in range(count):
                selector.click()
                child_age = Select(
                    self.find_element(
                        By.CSS_SELECTOR, f'select[data-group-child-age="{i}"]'
                    )
                )
                child_age.select_by_value(f"{age[i]}")
        

    def __filter_rooms(self, count: int) -> None:
        selector = self.find_element(
            By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]'
        )
        for i in range(count - 1):
            selector.click()
            # work with drop box

    def __filter_adult(self, count_adult: int = 1) -> None:
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

    def pick_filters(
        self,
        adult: bool = True,
        rooms: bool = True,
        count: List[int] = [2, 0, 1],
        children_age: Optional[List[int]] = None,
    ) -> None:
        if adult:
            self.__filter_adult(count[0])
        if rooms:
            self.__filter_rooms(count[2])
        if children_age != None:
            self.__filter_children(count[1], children_age)
        

    def sumbit_search(self) -> None:
        submit_element = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_element.click()
