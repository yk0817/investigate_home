from bs4 import BeautifulSoup
import urllib.request
import sys
import re
# webからhtmlを取得する場合
url = 'http://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&rn=0230&ek=023016720&ek=023015340&cb=0.0&ct=9.0&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=12&pc=50'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

scaped_wrappers = soup.find_all("div", class_="cassetteitem")

# 位置引数から辞書を返す
# 配列→辞書型にしたい。
def minutes_dicts(key,text):
    dict = {}
    dict[key] = text
    return dict






for scrape in scaped_wrappers:
    dict = {}
    address = scrape.find(class_="cassetteitem_detail-col1").string
    title_content = scrape.find(class_="cassetteitem_content-title").string
    # 東急田園都市線/三軒茶屋駅 歩9分
    # 東急世田谷線/西太子堂駅 歩11分
    # 東急世田谷線/若林駅 歩15分←といった情報のため、配列化
    minutes_stations = scrape.find_all(class_="cassetteitem_detail-text")
    count = 1
    # 普通に入れていく。
    for minute in minutes_stations:
        base_key = "minute_station"
        enter_key = base_key + str(count)
        # 結合していく
        dict.update(minutes_dicts(enter_key,minute.string))
        count += 1
    
        
    # 配列後置
    # 築〜年という数字、〜階建て
    # 正規表現でメモリー化させる。
    scrape.find_all(class_="cassetteitem_detail-col3")
    # 家賃農法を配列化
    scrape.select(".cassetteitem_other > tbody")
    
    