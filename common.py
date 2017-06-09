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

print(con.execute('SELECT * FROM house_price'))
results = cursor.fetchall()

cols = ORFs.keys()
vals = ORFs.values()

# sqlインサート
sql = "INSERT INTO %s (%s) VALUES(%s)" % (
    table, ",".join(cols), ",".join(vals))