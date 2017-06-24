from common import *

pyplot.title('家賃(木造)')
pyplot.xlabel('X-面積(m^2)')
pyplot.ylabel('Y-家賃(+= 管理費 + 礼金/12)')

x = np.linspace(0, 20, 10)
y = np.linspace(0,10,10)

# 家賃データを引っ張ってくる。
with connection.cursor() as cursor:
    sql = "select * from house_price where building_material = %s;"
    cursor.execute(sql,'木造')
    results = cursor.fetchall()
    
    for result in results:
        # あとで修正するかも
        if result['admin_expense'] is None:
            admin_expense = 0
        else:
            admin_expense = result['admin_expense'] / 1000
        
        if result['room_reikinn'] is None:
            room_reikinn = 0
        else:
            room_reikinn = result['room_reikinn'] / 12
            
        
        house_per_price = result['room_rent'] + admin_expense + room_reikinn
        room_area = result['room_area']
        pyplot.plot(room_area, house_per_price, 'ro')


pyplot.show()
pyplot.savefig('hoge.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)
connection.close()
