from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators

class SearchPage():
    def __init__(self, driver):
        self.driver = driver
        self.search_box_selctor = Locators.search_box_css_selector

    def search_for_string(self, phrase):
        search = self.driver.find_element(By.CSS_SELECTOR, self.search_box_selctor)
        search.send_keys(phrase + Keys.RETURN)
    
