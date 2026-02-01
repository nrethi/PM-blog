from pprint import pprint
import mysql.connector





def enable_user(email):
    kapcsolat = mysql.connector.connect(user='root',
                                        password='test1234',
                                        host='127.0.0.1',
                                        database='blog')

    assert kapcsolat.is_connected()

    get_user_id = ("SELECT user_id \n"
                   "FROM blog.user \n"
                   f"WHERE email = '{email}' ")
    user_id = 1

    authorize = ("UPDATE blog.user \n"
                 "SET enabled = 1 \n"
                 f"WHERE (user_id = {user_id})")


    kurzor = kapcsolat.cursor(dictionary=True)

    kurzor.execute(get_user_id)
    user_id = kurzor.fetchone()
    pprint(user_id)
    kurzor.execute(authorize)

enable_user('garirij791@okexbit.com')
