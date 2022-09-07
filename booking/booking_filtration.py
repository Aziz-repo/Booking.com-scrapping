# This class file include a class with instance methods.
# That will be responsible for interacting with our website
# After we have some results, to apply filtration


from pickle import TRUE
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from booking.utils import pop_up
from filters.meal_filter import MealFilter
from filters.sort_filter import SortFilters
from filters.health_safety_filter import HealthSafetyFilter
from filters.beach_access_filter import BeachAccessFilter


# TODO: add a handler to pick the chosen filters
class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values: int) -> None:
        # close sign in pop up
        pop_up.close_singin_popup(self.driver)

        filtration_box = self.driver.find_element(
            By.CSS_SELECTOR, 'div[data-filters-group="class"]'
        )
        star_child_element = filtration_box.find_elements(By.CSS_SELECTOR, "*")
        for star_value in star_values:
            for star_element in star_child_element:
                if (
                    str(star_element.get_attribute("innerHTML")).strip()
                    == f"{star_value} stars"
                ):
                    star_element.click()

    def apply_sort_filters(self, filter: SortFilters) -> None:

        filtration_button = self.driver.find_element(By.CLASS_NAME, "e57ffa4eb5")
        filtration_button.click()

        # close map pop-up
        pop_up.close_map_popup(self.driver)

        sorter_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-selected-sorter="popularity"]'
        )
        sorter_element.click()
        
        selection = self.driver.find_element(
            By.CSS_SELECTOR, f'button[data-id="{filter.value}"]'
        )
        selection.click()

    def apply_health_safety_filter(self, filter: HealthSafetyFilter) -> None:
        if filter.name == TRUE:
            health_safety_filter = self.driver.find_element(
                By.CSS_SELECTOR,
                f'input[name="{filter.value}"]'
            )
            health_safety_filter.click()

    def apply_beach_front_filter(self, filter: BeachAccessFilter) -> None:
        if filter.name == TRUE:
            beach_access_filter = self.driver.find_element(
                By.CSS_SELECTOR,
                f'input[name="{filter.value}"]'
            )
            beach_access_filter.click()

    def apply_meal_filter(self, filter: MealFilter) -> None:
        meal_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'input[name="mealplan={filter.value}"]'
        )
        meal_filter.click()


    