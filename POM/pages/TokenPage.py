from POM.pages.GeneralPage import GeneralPage
from POM.utils.mysql_db_access import get_user_validation_token

class TokenPage(GeneralPage):
    def __init__(self, browser=None):
        super().__init__(browser, f'http://localhost:8080/api/auth/confirm-registration?token={get_user_validation_token(self)}')
