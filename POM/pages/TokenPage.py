import time
from pprint import pprint
import mysql.connector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM.pages.GeneralPage import GeneralPage
from POM.utils.mysql_db_access import get_user_validation_token

class TokenPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, f'http://localhost:8080/api/auth/confirm-registration?token={get_user_validation_token(self)}')
