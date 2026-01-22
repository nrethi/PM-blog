from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage
from selenium.webdriver.support.wait import WebDriverWait


class ProfilePage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, 'http://localhost:4200/user-profile')
        self.active_recipes_locator = (By.XPATH, '//span[text()=" Active recipes (0) "]')
        self.button_sign_out_locator = (By.XPATH, '//p[@class="logout"]')


    def wait_for_pageload(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.button_sign_out_locator))


    def get_active_recipes(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.active_recipes_locator))


    def get_button_sign_out(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.button_sign_out_locator))