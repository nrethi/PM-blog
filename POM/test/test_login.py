from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.pages.AuthenticationPage import AuthenticationPage
from POM.pages.ProfilePage import ProfilePage
from POM.data.user_testdata import TESTUSER1, TESTUSER2
import allure
from POM.pages.TokenPage import TokenPage
import pytest

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


    @pytest.mark.skip(reason="Pipeline environment doesnt like sql hashes for some reason")
    @allure.title("DisHub Standard Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("login", "positive")

    def test_login(self):
        #self.token_page.visit()
        self.authentication_page.visit()
        self.authentication_page.login(TESTUSER2 ['email'], TESTUSER2['password'])
        self.profile_page.wait_for_pageload()

            # self.authentication_page.attach_screenshot_to_allure()
        assert self.profile_page.get_valami_dolog().is_displayed()




