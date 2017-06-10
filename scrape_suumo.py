from common import *
# webからhtmlを取得する場合
url = 'http://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&rn=0230&ek=023016720&ek=023015340&cb=0.0&ct=9.0&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=12&pc=50'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, "lxml")

scaped_wrappers = soup.find_all("div", class_="cassetteitem")

def minutes_dicts(key,text):
    dict = {}
    if text is not None:
        dict[key] = "'" + text + "'"
    return dict
    
def get_building_spec(args):
    data_dict = {}
    for arg in args:
        arg = arg.string
        data = re.search(r"(\d+)",str(arg))
        if re.match(r"築",arg):
            data_dict["contructed_year"] = data.group(0)
        elif re.search(r"\d+階",arg):
            data_dict["floor_num"] = data.group(0)
    return data_dict
    
def get_room_spec(args):
    data_dict = {}
    data_dict["room_floor"] = args[2].string.replace("階","")
    data_dict["room_rent"] = args[3].string.replace("万円","")
    if re.search(r"円",args[4].string):
        data_dict["admin_expense"] = args[4].string.replace("円","")
    room_other_price = args[5].string.split("/")
    if re.match(r"\d+万円",room_other_price[0]):
        data_dict["room_deposit"] = room_other_price[0].replace("万円","")
    if re.match(r"\d+万円",room_other_price[1]):
        data_dict["room_reikinn"] = room_other_price[1].replace("万円","")
    data_dict["room_plan"] = "'" + args[6].string + "'"
    data_dict["room_area"] = args[7].contents[0].replace("m","")
    return data_dict

for scrape in scaped_wrappers:
    dict = {}
    dict['address'] = "'" + scrape.find(class_="cassetteitem_detail-col1").string + "'"
    dict['title_content'] = "'" + scrape.find(class_="cassetteitem_content-title").string + "'"
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
    building_spec = scrape.select(".cassetteitem_detail-col3 > div")
    # sys.exit()
    dict.update(get_building_spec(building_spec))
    # 何個も飽き部屋がある場合があるが今回は
    room_detail = scrape.select(".cassetteitem_other > tbody > tr")[0].select("td")
    dict.update(get_room_spec(room_detail))
    # print(dict)
    cols = dict.keys()
    vals = dict.values()
    sql = "INSERT INTO {0} ({1}) VALUES ({2})".format("house_price", ",".join(cols), ",".join(vals))
    print(sql)
    con.execute(sql)
    connection.commit()

connection.close()



