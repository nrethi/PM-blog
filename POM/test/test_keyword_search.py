from POM.utils.create_driver import create_preconfigured_chrome_driver
import allure
from POM.pages.FilteredSearchPage import FilteredSearchPage

class TestAuthenticationPage(object):

    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.filtered_search_page = FilteredSearchPage(browser)

    def teardown_method(self):
        self.filtered_search_page.quit()

    @allure.title("DisHub Keyword search")
    @allure.description("Kulcsszó alapján való keresés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("keyword", "search")

    def test_search_keyword(self):
        self.filtered_search_page.visit()
        self.filtered_search_page.get_input_keyword_search().send_keys('lobster')
        self.filtered_search_page.get_button_keyword_search().click()
        print(self.filtered_search_page.get_first_displayed_recipe_title())
        assert "Lobster" or "lobster" in self.filtered_search_page.get_first_displayed_recipe_title()

    def test_search_capital_keyword(self):
        self.filtered_search_page.visit()
        self.filtered_search_page.get_input_keyword_search().send_keys('Lobster')
        self.filtered_search_page.get_button_keyword_search().click()
        print(self.filtered_search_page.get_first_displayed_recipe_title())
        assert "Lobster" or "lobster" in self.filtered_search_page.get_first_displayed_recipe_title()