import mysql.connector
from pprint import pprint
import time
from POM.pages.GeneralPage import GeneralPage
from POM.utils.create_driver import create_preconfigured_chrome_driver



def get_user_validation_token(self, userid=39):
    kapcsolat = mysql.connector.connect(user='root',
                                        password='test1234',
                                        host='127.0.0.1',
                                        database='blog')

    assert kapcsolat.is_connected()
    confirmation = (f"SELECT token \n"
                    "FROM blog.confirmation \n"
                    f"WHERE user_id = {userid}")
    kurzor = kapcsolat.cursor(dictionary=True)

    kurzor.execute(confirmation)
    validation_token = kurzor.fetchone()
    validation_token = validation_token['token']
    pprint(validation_token)
    return validation_token