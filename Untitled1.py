
# coding: utf-8

# In[2]:

from common import *
pyplot.rcParams['font.family'] = 'Osaka'

get_ipython().magic('matplotlib inline')

pyplot.title('N=2820 東急田園都市 池尻大橋〜桜新町 ソース：suumo',fontsize=15)
pyplot.xlabel('X-面積(m^2)',fontsize=15)
pyplot.ylabel('Y-家賃 万円/月(含 管理費 + 礼金/24)',fontsize=15)

x = np.linspace(0, 20, 10)
y = np.linspace(0, 10, 10)

# 家賃データを引っ張ってくる。
with connection.cursor() as cursor:
#     sql = "select count(*) from house_price where building_material = %s;"
#     sql = "select count(*) from house_price;"
    # cursor.execute(sql,'木造')
#     cursor.execute(sql)
#     n_count = cursor.fetchall()[0]['count(*)']
    # print(count[0]['count(*)'])
    # sql = "select * from house_price where building_material = %s;"
    sql = "select * from house_price;"
    # cursor.execute(sql,'木造')
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for result in results:
        # あとで修正するかも
        if result['admin_expense'] is None:
            admin_expense = 0
        else:
            admin_expense = result['admin_expense'] / (10 ** 4)
        
        if result['room_reikinn'] is None:
            room_reikinn = 0
        else:
            room_reikinn = result['room_reikinn'] / 24
            
        
        house_per_price = result['room_rent'] + admin_expense + room_reikinn
        room_area = result['room_area']
        building_material = result['building_material']
        if building_material == '木造':
            pyplot.plot(room_area, house_per_price, 'ro', label='木造')
        elif building_material == '鉄筋系':            
            pyplot.plot(room_area, house_per_price, 'bo', label='鉄筋系')
        else:
            pyplot.plot(room_area, house_per_price, 'yo', label='鉄骨系')


pyplot.tick_params(labelsize = 20)
pyplot.tight_layout()
pyplot.text(30, 4, '木造=赤色,鉄筋系=青色,鉄骨系=黄色', fontsize = 15)
pyplot.show()
# pyplot.savefig('mokuzo.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)
connection.close()






# In[ ]:



