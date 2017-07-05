from common import *
import logging


sql = "SELECT * FROM house_price"
logging.basicConfig(level=logging.DEBUG)
logging.debug('デバッグ')

test = con.execute(sql)
connection.commit()
# print(test)

connection.close()