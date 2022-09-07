# This class file include a class with instance methods.
# That will be responsible for interacting with our website
# After we have some results, to apply filtration


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from booking.utils import pop_up
from filters.facilities_fitler import FacilitiesFilter
from filters.meal_filter import MealFilter
from filters.sort_filter import SortFilters
from filters.health_safety_filter import HealthSafetyFilter
from filters.beach_access_filter import BeachAccessFilter
from filters.bed_preference_filter import BedPrefFilter
from filters.review_score_filter import ReviewScoreFilter
from filters.facilities_fitler import FacilitiesFilter
from filters.room_facilities_filter import RoomFacilitiesFilter

# TODO: add a handler to pick the chosen filters
# TODO: add the functionnality of providing multiple filters

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
        if filter.name == HealthSafetyFilter.TRUE:
            health_safety_filter = self.driver.find_element(
                By.CSS_SELECTOR,
                f'input[name="{filter.value}"]'
            )
            health_safety_filter.click()

    def apply_beach_front_filter(self, filter: BeachAccessFilter) -> None:
        if filter.name == BeachAccessFilter.TRUE:
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


    def apply_bed_preference_filter(self, filter: BedPrefFilter) -> None:
        bed_pref_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'input[name="tbd={filter.value}"]'
        )
        bed_pref_filter.click()

    def apply_review_score_filter(self, filter: ReviewScoreFilter) -> None:
        review_score_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'input[name="review_score={filter.value}"]'
        )
        review_score_filter.click()

    def apply_private_bathroom_filter(self, number_of_private_bathroom: int) -> None:
        increment_button = self.driver.find_element(
            By.CLASS_NAME,
            "d64a4ea64d"
        )
        for _ in range(number_of_private_bathroom):
            increment_button.click()
    
    def apply_facilities_filter(self, filter: FacilitiesFilter) -> None:
        facility_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'input[name="hotelfacility={filter.value}"]'
        )
        facility_filter.click()

    def apply_room_facilities_filter(self, filter: RoomFacilitiesFilter) -> None:
        room_facilty_filter = self.driver.find_element(
            By.CSS_SELECTOR,
            f'input[name="roomfacility={filter.name}"]'
        )
        room_facilty_filter.click()
