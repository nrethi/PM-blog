from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage

class AuthenticationPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, 'http://localhost:4200/authentication')
        self.button_signup_locator = (By.XPATH, '//button[text()="Sign Up"]')
        self.button_login_locator = (By.XPATH, '//button[text()="Login"]')
        self.button_submit_locator = (By.XPATH, '//button[text()="Submit]')

    def wait_for_pageload(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.button_signup_locator))


    def get_input_email(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'email')))


    def get_input_password(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'password')))


    def get_input_name(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'name')))


    def get_button_login(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.button_login_locator))


    def get_button_signup(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.button_signup_locator))


    def get_button_submit(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(self.button_submit_locator))


    def get_error_message(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'is-invalid text-danger ng-star-inserted')))


    def get_header_login(self):
        return WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//h1[text()="Login"]')))


    def get_header_create_account(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Create Account"]')))


    def get_button_facebook(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//button/i[@class="fab fa-facebook-f"]')))


    def get_button_instagram(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//button/i[@class="fab fa-google-plus-g"]')))


    def get_toggler_navbar(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-controls="navbarNav"]')))



    def login(self, email, password):
        self.get_input_email().send_keys(email)
        self.get_input_password().send_keys(password)
        self.get_button_login().click()

    def attach_screenshot_to_allure(self):
        attach_screenshot(self.browser, "CI_test.png")
