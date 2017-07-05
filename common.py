from bs4 import BeautifulSoup
import urllib.request
import sys
import re
import pymysql.cursors
import time
from matplotlib import pyplot
import numpy as np
import tensorflow as tf
import pandas as pd


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
