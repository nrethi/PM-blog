import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


def create_preconfigured_chrome_driver():
    options = selenium.webdriver.chrome.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--guest')
    #options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    #browser.set_window_size(1920, 1080)
    return browser


def create_preconfigured_firefox_driver():
    options = selenium.webdriver.firefox.options.Options()
    options.set_preference("detach", True)
    options.add_argument('--guest')
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1920, 1080)
    return browser

'''
def create_preconfigured_safari_driver():
    options = selenium.webdriver.safari.options.Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--guest')
    options.add_argument('--headless')
    browser = webdriver.Safari(options=options)
    browser.set_window_size(1920, 1080)
    return browser

def create_preconfigured_webkit_driver():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--guest')
    options.add_argument('--headless')
    browser = webdriver.WPEWebKit(options=options)
    browser.set_window_size(1920, 1080)
    return browser
    '''




