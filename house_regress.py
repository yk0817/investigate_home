from common import *

with connection.cursor() as cursor:
    sql = "select room_rent,room_area from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    train_y = [np.asarray(row['room_rent']) for row in results]
    train_x = [np.asarray(row['room_area']) for row in results]
    # test = np.asarray(train_x)
    # print(test)