from common import *
con.execute(sql)
connection.commit()

pyplot.title('家賃(木造)')
pyplot.xlabel('X-面積(m^2)')
pyplot.ylabel('Y-家賃(+= 管理費 + 礼金/12)')

x = np.linspace(0, 20, 10)
y = np.linspace(0,10,10)
pyplot.show()

connection.close()
