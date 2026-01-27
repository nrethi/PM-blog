from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.pages.AuthenticationPage import AuthenticationPage
from POM.pages.ProfilePage import ProfilePage
from POM.data.user_testdata import TESTUSER
from POM.pages.GeneralPage import GeneralPage
from allure_commons.types import AttachmentType
import allure
import time

class TestAuthenticationPage(object):

    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.authentication_page = AuthenticationPage(browser)
        self.profile_page = ProfilePage(browser)

    def teardown_method(self):
        self.authentication_page.quit()

    @allure.title("DisHub Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")

    def test_login(self):
        self.authentication_page.visit()
        self.authentication_page.login(TESTUSER ['email'], TESTUSER['password'])
        #self.profile_page.wait_for_pageload()
        time.sleep(5)
        assert self.profile_page.get_button_sign_out().is_displayed()



