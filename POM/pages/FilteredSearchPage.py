from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage

class FilteredSearchPage(GeneralPage):
    def __init__(self, browser = None):
        super().__init__(browser, 'http://localhost:4200/filter-form')

    def wait_for_pageload(self):
        pass

    def get_input_keyword_search(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@type="search"]')))


    def get_button_keyword_search(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,'btn-search')))

    def get_first_displayed_recipe_title(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//h2[@class="recipe-title"]'))).text