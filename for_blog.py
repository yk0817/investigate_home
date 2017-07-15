
# coding: utf-8

# In[37]:

pyplot.plot(room_area, house_per_price, 'bo', label='plot')



pyplot.tick_params(labelsize = 20)
pyplot.tight_layout()
pyplot.text(30, 4, 'label', fontsize = 15)
pyplot.show()


# In[36]:

from common import *

get_ipython().magic('matplotlib inline')

pyplot.title('N=2820 source:suumo',fontsize=15)
pyplot.xlabel('X-room_area(m^2)',fontsize=15)
pyplot.ylabel('Y-room_rent/month)',fontsize=15)

x = np.linspace(0, 20, 10)
y = np.linspace(0, 10, 10)

# 家賃データを引っ張ってくる。
with connection.cursor() as cursor:
    sql = "select * from house_price where toyoko_true_or_not = 0;"
    # cursor.execute(sql,'木造')
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for result in results:
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
        pyplot.plot(room_area, house_per_price, 'bo', label='plot')



pyplot.tick_params(labelsize = 20)
pyplot.tight_layout()
pyplot.text(30, 4, 'label', fontsize = 15)
pyplot.show()
# pyplot.savefig('mokuzo.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)
# connection.close()


# In[31]:

pyplot.title('N=2820 source:suumo',fontsize=15)
pyplot.xlabel('X-contructed_year(year)',fontsize=15)
pyplot.ylabel('Y-room_rent/month)',fontsize=15)

x = np.linspace(0, 50, 10)
y = np.linspace(0, 10, 10)

for result in results:
    house_per_price = result['room_rent'] + admin_expense + room_reikinn
    if result['contructed_year'] is None:
        contructed_year = 0
    else:
        contructed_year = result['contructed_year']
    pyplot.plot(contructed_year, house_per_price, 'bo', label='test')
    


# In[ ]:

pyplot.title('N=2820 source:suumo',fontsize=15)
pyplot.xlabel('X-minute_from_station(m)',fontsize=15)
pyplot.ylabel('Y-roo
              m_rent/month)',fontsize=15)

x = np.linspace(0, 20, 10)
y = np.linspace(0, 10, 10)

for result in results:
    house_per_price = result['room_rent'] + admin_expense + room_reikinn
    minutes_from_station = result['minutes_from_station']
    pyplot.plot(minutes_from_station, house_per_price, 'bo', label='plot')

# コネクションクローズ
connection.close()

