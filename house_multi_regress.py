from common import *
rng = np.random

learning_rate = 0.01
training_epochs = 1000
display_step = 50

with connection.cursor() as cursor:
    sql = "select room_rent,room_area,contructed_year,minutes_from_station from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    train_Y = [row['room_rent'] for row in results]
    train_X1 = [row['room_area'] for row in results]
    # contructed_year nullは新築記号
    train_X2 = [row['contructed_year'] if row['contructed_year']  else 0 for row in results]
    train_X3 = [row['minutes_from_station'] for row in results]
    # dummy 変数

    
    
    n_samples = len(train_X1)

    X1 = tf.placeholder("float")
    X2 = tf.placeholder("float")
    X3 = tf.placeholder("float")
    Y = tf.placeholder("float")
    # Set model weights
    # 変数を定義    
    W1 = tf.Variable(rng.randn(), name="weight")
    W2 = tf.Variable(rng.randn(), name="weight")
    W3 = tf.Variable(rng.randn(), name="weight")
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
            for (x1,x2,x3, y) in zip(train_X1,train_X2,train_X3,train_Y):
                sess.run(optimizer, feed_dict={X1: x1, X2: x2, X3: x3, Y: y})
                training_cost = sess.run(cost, feed_dict={X1: train_X1, X2: train_X2, X3: train_X3, Y: train_Y})
                print("Training cost=", training_cost, "W1=", sess.run(W1),"W2=", sess.run(W2),"W3=", sess.run(W3), "b=", sess.run(b), '\n')
                
        print("Optimization Finished!")
        
connection.close()        