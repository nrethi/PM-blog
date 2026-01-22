from POM.utils.create_driver import create_preconfigured_chrome_driver
from selenium.webdriver.common.by import By

browser = create_preconfigured_chrome_driver()


def scale_browser_size(width, height, webelement):
    element_displayed = webelement.is_displayed()
    browser.maximize_window()
    browser.get_window_size()
    max_window_size = browser.get_window_size()
    window_width = int(max_window_size['width'])
    window_height = int(max_window_size['height'])
    max_width_scale = 170
    max_height_scale = 100

    for h in range(max_height_scale):

        if element_displayed:
            if browser.get_window_size()['height'] > height:
                window_height -= 5
                browser.set_window_size(window_width, window_height)
            else: break
            print(browser.get_window_size())
        else: print('az elem nem található')


    for w in range(max_width_scale):
        element1_displayed = browser.find_element(By.XPATH, '//div[1]/div/h5').is_displayed()
        element2_displayed = browser.find_element(By.XPATH, '//div[2]/div/h5').is_displayed()
        element3_displayed = browser.find_element(By.XPATH, '//div[3]/div/h5').is_displayed()
        if element1_displayed or element2_displayed or element3_displayed:
            if browser.get_window_size()['width'] > width:
                window_width -= 5
                browser.set_window_size(window_width, window_height)
                print(element_displayed)
            else: break
            print(browser.get_window_size())

        else:
            print('nem található')
            break
