import mysql.connector
from pprint import pprint

kapcsolat = mysql.connector.connect(user='root',
                                    password='test1234',
                                    host='127.0.0.1',
                                    database='blog - projektmunka')

assert kapcsolat.is_connected()

 lekerdezes = ("SELECT * \n"
              "FROM account \n"
              "WHERE firstname = 'Alfreda' \n"
              "AND lastname = 'Copeland' \n"
              "AND email = 'andersbr@mac.com' \n"
              "AND role = 'ROLE_ADMIN' \n"
              "AND username = 'andersbr@mac.com' \n"
              "AND address = 'Budapest, Baross utca'")

 authentication = ("UPDATE `blog`.`user` SET `enabled` = '1' WHERE (`user_id` = '34')")

kurzor = kapcsolat.cursor(dictionary=True)

kurzor.execute(lekerdezes)

# sor = kurzor.fetchone()
#
# pprint(sor)

# osszes_sor = kurzor.fetchall()
# pprint(len(osszes_sor))

# elso_tiz_sor = kurzor.fetchmany(10)
# pprint(elso_tiz_sor)

# sor = kurzor.fetchone()
# pprint(sor)

eredmenyek = kurzor.fetchall()
assert len(eredmenyek) == 1

kapcsolat.close()