
# coding: utf-8

# In[5]:

from common import *
rng = np.random

learning_rate = 0.01
# training_epochs = 1000
training_epochs = 10
display_step = 50

with connection.cursor() as cursor:
    sql =  "select room_rent,room_deposit,room_reikinn,admin_expense,room_area,contructed_year,minutes_from_station,building_material      from house_price where toyoko_true_or_not = 0;"
    
    cursor.execute(sql)
    results = cursor.fetchall()
    train_Y = [row['room_rent'] + row['room_deposit'] / 24 + row['room_reikinn'] / 24 + row['admin_expense'] / 10000  for row in results]
    train_X1 = [row['room_area'] for row in results]
    # contructed_year nullは新築記号
    train_X2 = [row['contructed_year'] if row['contructed_year'] else 0 for row in results]
    train_X3 = [row['minutes_from_station'] for row in results]
    # dummy 変数 木造ダミー 木造は1を取る 他は0 
#     train_X4 = [1 if row['building_material'].strip() == "木造" else 0 for row in results]
    
    n_samples = len(train_X1)

    X1 = tf.placeholder("float")
    X2 = tf.placeholder("float")
    X3 = tf.placeholder("float")
#     X4 = tf.placeholder("float")
    Y = tf.placeholder("float")
    # Set model weights
    # 変数を定義    
    W1 = tf.Variable(rng.randn(), name="weight")
    W2 = tf.Variable(rng.randn(), name="weight")
    W3 = tf.Variable(rng.randn(), name="weight")
#     W4 = tf.Variable(rng.randn(), name="weight")
    b = tf.Variable(rng.randn(), name="bias")
    # pred = tf.add(tf.multiply(X, W), b)
    sum_list = [tf.multiply(X1,W1),tf.multiply(X2,W2),tf.multiply(X3,W3)]
    pred = tf.add(tf.add_n(sum_list),b)
    # print(sum_list[0])
    cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        count = 0
        for epoch in range(training_epochs):
            count += 1
            # print(count)
#             for (x1,x2,x3,x4, y) in zip(train_X1,train_X2,train_X3,train_X4,train_Y):
            for (x1,x2,x3, y) in zip(train_X1,train_X2,train_X3,train_Y):
                sess.run(optimizer, feed_dict={X1: x1, X2: x2, X3: x3, Y: y})
#                 sess.run(optimizer, feed_dict={X1: x1, X2: x2, X3: x3, X4: x4, Y: y})

#                 training_cost = sess.run(cost, feed_dict={X1: train_X1, X2: train_X2, X3: train_X3, X4: train_X4, Y: train_Y})
                training_cost = sess.run(cost, feed_dict={X1: train_X1, X2: train_X2, X3: train_X3, Y: train_Y})

#                 print("Training cost=", training_cost, "W1=", sess.run(W1),"W2=", sess.run(W2),"W3=", sess.run(W3),"W4=", sess.run(W4), "b=", sess.run(b), '\n')
                
        print("Optimization Finished!")
#         print("Training cost=", training_cost, "W1=", sess.run(W1),"W2=", sess.run(W2),"W3=", sess.run(W3),"W4=", sess.run(W4), "b=", sess.run(b), '\n')
        W1,W2,W3,b = sess.run(W1),sess.run(W2),sess.run(W3),sess.run(b)
        print("Training cost=", training_cost, "W1=", W1,"W2=", W2,"W3=", W3, "b=", b, '\n')

# connection.close()        


# In[14]:

#決定係数を求める。numpuyで計算
X_1 = W1 * np.array(train_X1)
X_2 = W2* np.array(train_X2)
X_3 = W3* np.array(train_X3)
    for 


# In[ ]:



