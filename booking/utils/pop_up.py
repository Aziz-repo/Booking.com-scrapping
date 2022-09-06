from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def close_map_popup(driver: WebDriver):
    try:
        close_button = driver.find_element(By.CLASS_NAME, "map_full_overlay__close")
        close_button.click()
    except:
        # must be loged
        print("No map Pop-up. Skipping!!")


def close_singin_popup(driver: WebDriver):
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        close_button.click()
    except:
        # must be logged
        print("No sign in Pop-up, Skipping!!")