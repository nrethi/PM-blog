from selenium.webdriver.ie.webdriver import WebDriver

from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.pages.AuthenticationPage import AuthenticationPage
from POM.pages.ProfilePage import ProfilePage
from POM.data.user_testdata import TESTUSER1, TESTUSER2
from allure_commons.types import AttachmentType
import allure
import time
from POM.pages.GeneralPage import GeneralPage
from POM.pages.TokenPage import TokenPage

class TestAuthenticationPage(object):

    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.authentication_page = AuthenticationPage(browser)
        self.profile_page = ProfilePage(browser)
        self.token_page = TokenPage(browser)
        self.authentication_page.signup(TESTUSER2 ['email'], TESTUSER2['name'], TESTUSER2['password'])
        self.token_page.visit()

    def teardown_method(self):
        self.authentication_page.quit()

    @allure.title("DisHub Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")

    def test_login(self):
        #self.token_page.visit()
        #time.sleep(5)
        self.authentication_page.visit()
        self.authentication_page.login(TESTUSER2 ['email'], TESTUSER2['password'])
        self.profile_page.wait_for_pageload()
        #time.sleep(5)
            # self.authentication_page.attach_screenshot_to_allure()
        assert self.profile_page.get_valami_dolog().is_displayed()




