import pytest
from Pages.SearchPage import SearchPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class TestEcosiaSearch():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        yield
        driver.close()
        driver.quit()

    def test_ecosia_search(self, test_setup):
        PHRASE = "SEARCH"
        SEARCH_URL = 'https://www.ecosia.org/'
        driver.get(SEARCH_URL)
        search_page = SearchPage(driver)
        search_page.search_for_string(PHRASE)
        # assert x == "ABC"
