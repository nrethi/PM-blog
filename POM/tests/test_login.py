from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.pages.AuthenticationPage import AuthenticationPage
from POM.pages.ProfilePage import ProfilePage
from POM.data.user_testdata import TESTUSER


class TestAuthenticationPage(object):

    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.authentication_page = AuthenticationPage(browser)
        self.profile_page = ProfilePage(browser)

    def teardown_method(self):
        self.authentication_page.quit()

    def test_login(self):
        self.authentication_page.visit()
        self.authentication_page.login(TESTUSER ['email'], TESTUSER['password'])
        self.profile_page.wait_for_pageload()
        assert self.profile_page.get_active_recipes().is_displayed()