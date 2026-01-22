from hmac import digest_size

from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.pages.ProfilePage import ProfilePage
from POM.pages.AuthenticationPage import AuthenticationPage
from POM.pages.LandingPage import LandingPage
#from POM.pages.RecipesPage import RecipePage
from selenium.webdriver.common.by import By

class TestResponsibility(object):

    def setup_method(self):
        browser = create_preconfigured_chrome_driver()
        self.authentication_page = AuthenticationPage(browser)
        self.profile_page = ProfilePage(browser)
        self.landing_page = LandingPage(browser)

    def teardown_method(self):
        self.authentication_page.quit()

    '''def test_landing_responsiveness(self):
        self.landing_page.scale_browser_size(700, 700, self.landing_page.get_carousel_headers())
        assert self.landing_page.get_carousel_headers().is_displayed()'''
#comment
