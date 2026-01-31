from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage

class LandingPage(GeneralPage):
    def __init__(self, browser = None):
        super().__init__(browser, 'http://localhost:4200/landing-page')

    def wait_for_pageload(self):
        pass