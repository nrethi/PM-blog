'''
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
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from POM.utils.create_driver import create_preconfigured_chrome_driver
from POM.utils.create_driver import create_preconfigured_firefox_driver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def drivers_initialize(request):
    if request.param == "chrome":
        web_driver = create_preconfigured_chrome_driver()
    if request.param == "firefox":
        web_driver = create_preconfigured_firefox_driver()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("drivers_initialize")
class BasicTest:
    pass


class TestSearchInGoogle(BasicTest):

    def test_search_into_two_browser(self):
        self.driver.get('https://google.com/')
        self.driver.maximize_window()

        title = "Google"
        assert title == self.driver.title

        search_line_field = self.driver.find_element(By.NAME, "q")
        search_line_field.clear()

        text_example = "I hope this works!"
        search_line_field.send_keys(text_example)
        time.sleep(1)
        search_line_field.send_keys(Keys.ENTER)
        time.sleep(3)

        new_title = "I hope this works! - Поиск в Google"
        assert new_title == self.driver.title