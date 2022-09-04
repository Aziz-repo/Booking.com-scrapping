import os
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

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency: str = None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()

    def select_place_to_go(self, place_to_go: str):
        search_field = self.find_element(
            By.ID,
            'ss'
        )
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR,
            'li[data-i="0"]'
        )
        first_result.click()

    def select_date(self, check_in_date: str, check_out_date: str):
        difference = utils.month_difference(check_in_date, check_out_date)

        # TODO: rewrite this block as function
        # same panel
       
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
                f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()
        

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'td[data-date="{check_out_date}"]'
        )
        
        check_out_element.click()
            
