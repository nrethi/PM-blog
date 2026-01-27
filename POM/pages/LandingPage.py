from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage

class LandingPage(GeneralPage):
    def __init__(self, browser = None):
        super().__init__(browser, 'http://localhost:4200/landing-page')

    def wait_for_pageload(self):
        pass


    def get_carousel_image(self, img_number):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, f'f//div[{img_number}]/img[@class="d-block w-100"]')))


    def get_carousel_caption(self, caption_number):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, f'//div[{caption_number}]/div[@class="carousel-caption d-none d-md-block"]')))


    def get_button_slide(self, slide_number):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, f'//button[@aria-label="{slide_number}"]')))


    def get_carousel_headers(self):
        return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located())

    ''' def scale_browser_size(self, width, height, webelement):
        element_displayed = webelement.is_displayed()
        self.browser.maximize_window()
        self.browser.get_window_size()
        max_window_size = self.browser.get_window_size()
        window_width = int(max_window_size['width'])
        window_height = int(max_window_size['height'])
        max_width_scale = 170
        max_height_scale = 100

        for h in range(max_height_scale):

            if element_displayed:
                if self.browser.get_window_size()['height'] > height:
                    window_height -= 5
                    self.browser.set_window_size(window_width, window_height)
                else:
                    break
                print(self.browser.get_window_size())
            else:
                print('az elem nem található')

        for w in range(max_width_scale):
            element1_displayed = self.browser.find_element(By.XPATH, '//div[1]/div/h5').is_displayed()
            element2_displayed = self.browser.find_element(By.XPATH, '//div[2]/div/h5').is_displayed()
            element3_displayed = self.browser.find_element(By.XPATH, '//div[3]/div/h5').is_displayed()
            if element1_displayed or element2_displayed or element3_displayed:
                if self.browser.get_window_size()['width'] > width:
                    window_width -= 5
                    self.browser.set_window_size(window_width, window_height)
                    print(element_displayed)
                else:
                    break
                print(self.browser.get_window_size())

            else:
                print('nem található')
                break '''


