from common import *

def key_value_for_dicts(key,text):
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
    data_dict["room_floor"] = "'" + args[2].string.replace("階","") + "'"
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


def suumo_url(page_num):
    # kz = 1 2 3 でパラメータ変更
    # 1→鉄筋系
    # 2→鉄骨系
    # 3→木造系
    # 10万以下、
    # 池尻大橋駅、三軒茶屋駅、駒沢大学駅、桜新町駅の賃貸・部屋探し情報　検索結果
    base_url = 'http://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=50&smk=&po1=12&po2=99&kz=1&shkr1=03&shkr2=03&shkr3=03&shkr4=03&rn=0230&ek=023002000&ek=023016720&ek=023015340&ek=023016140&ra=013&ae=02301&cb=0.0&ct=10.0&co=1&et=9999999&mb=0&mt=9999999&cn=9999999&fw2=&pn='
    url = base_url + str(page_num)
    return url

def suumo_make_wrappers(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    scaped_wrappers = soup.find_all("div", class_="cassetteitem")
    return scaped_wrappers
    
def nearest_station_parse(station_text,dict):
    minute_parse_array = station_text.string.split("/")
    nearest_station = re.search(r"(.+)駅",minute_parse_array[1]).group(0)
    minutes_from_station = re.search(r"(\d+)",minute_parse_array[1]).group(0)
    dict.update(key_value_for_dicts("nearest_station",nearest_station))
    dict.update(key_value_for_dicts("minutes_from_station",minutes_from_station))
    return dict
        

def scraped_data_insert_db(scaped_wrappers):
    for scrape in scaped_wrappers:
        dict = {}
        dict['building_material'] = "'" + "木造" + "'"
        dict['address'] = "'" + scrape.find(class_="cassetteitem_detail-col1").string + "'"
        dict['title_content'] = "'" + scrape.find(class_="cassetteitem_content-title").string + "'"
        # 東急世田谷線/若林駅 歩15分←といった情報を配列化
        station_texts = scrape.find_all(class_="cassetteitem_detail-text")
        count = 1
        
        for station_text in station_texts: 
            #東急世田谷線/若林駅 歩15分を 1.若林駅と2.15に分割   
            if count == 1:
                dict = nearest_station_parse(station_text,dict)
            base_key = "minute_station"
            enter_key = base_key + str(count)
            # 結合していく
            dict.update(key_value_for_dicts(enter_key,station_text.string))
            count += 1        
        # 配列後置
        # 築〜年という数字、〜階建て
        # 正規表現でメモリー化させる。
        building_spec = scrape.select(".cassetteitem_detail-col3 > div")
        # sys.exit()
        dict.update(get_building_spec(building_spec))
        # 何個も飽き部屋がある場合ケースは無視（ほとんど同じような条件の部屋しかないため、調査(安い家探し)の目的から外れる)
        room_detail = scrape.select(".cassetteitem_other > tbody > tr")[0].select("td")
        dict.update(get_room_spec(room_detail))
        # print(dict)
        cols = dict.keys()
        vals = dict.values()
        print(vals)
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format("house_price", ",".join(cols), ",".join(vals))
        print(sql)
        con.execute(sql)
        connection.commit()

page_num = 1

while(True):
    try:
        wrappers = suumo_make_wrappers(suumo_url(page_num))
        scraped_data_insert_db(wrappers)
        time.sleep(1)
        page_num += 1
        # print(str(wrappers))
        # ダサい。
        if str(wrappers) == "[]":
            break
    except Exception as e:
        print(e)
        break


connection.close()

