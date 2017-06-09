from bs4 import BeautifulSoup
import urllib.request

# webからhtmlを取得する場合
url = 'http://suumo.jp/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

