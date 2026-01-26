from selenium.webdriver.chrome.options import Options
from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.safari.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.webkitgtk.options import Options

import pytest
URL = 'https://duckduckgo.com'

class MultiBrowserResponsiveness(object):

    @pytest.fixture
    def browser_chrome(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    @pytest.fixture
    def browser_firefox(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    @pytest.fixture
    def browser_safari(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--guest')
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

def test_multiple_browsers(browser_chrome):
    assert WebDriverWait()