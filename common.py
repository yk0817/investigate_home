from bs4 import BeautifulSoup
import urllib.request
import sys
import re
import pymysql.cursors
# mysql参考
# http://www.yoheim.net/blog.php?q=20151102

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python_study',
                             charset='utf8mb4',
                             # cursorclassを指定することで
                             # Select結果をtupleではなくdictionaryで受け取れる
                             cursorclass=pymysql.cursors.DictCursor)
                            # )

con = connection.cursor()

# print(con.execute('SELECT * FROM house_price'))
# results = cursor.fetchall()

# {'room_area': '16.32', 'room_floor': '1', 'floor_num': '4', 'admin_expense': '4000', 'minute_station2': '東急田園都市線/三軒茶屋駅 歩25分', 'room_rent': '4.5', 'minute_station1': '東急世田谷線/世田谷駅 歩2分', 'address': '東京都世田谷区世田谷３', 'title_content': 'スカイコート世田谷', 'contructed_year': '34', 'room_plan': 'ワンルーム', 'minute_station3': '東急田園都市線/駒沢大学駅 歩23分'}
# cols = ORFs.keys()
# vals = ORFs.values()

# sqlインサート
# sql = "INSERT INTO {0} ({1}) VALUES({2})".format(table, ",".join(cols), ",".join(vals))