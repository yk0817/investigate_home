from common import *

with connection.cursor() as cursor:
    sql = "select room_rent from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    # print(results)
    # for row in results:
    #     print(row)
    train_x = [row.values() for row in results]
    test = np.asarray(train_x)
    print(test)