
# coding: utf-8

# In[18]:

from common import *
rng = np.random


with connection.cursor() as cursor:
    sql = "select room_rent,room_area from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    train_Y = [np.asarray(row['room_rent']) for row in results]
    train_X = [np.asarray(row['room_area']) for row in results]
    n_samples = train_X
    X = tf.placeholder("float")
    Y = tf.placeholder("float")
    # Set model weights
    # 変数を定義    
    W = tf.Variable(rng.randn(), name="weight")
    b = tf.Variable(rng.randn(), name="bias")
    pred = tf.add(tf.multiply(X, W), b)
    cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
    


# In[ ]:



