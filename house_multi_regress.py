from common import *
rng = np.random

learning_rate = 0.01
training_epochs = 1000
display_step = 50

with connection.cursor() as cursor:
    sql = "select room_rent,room_area from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    train_Y = [row['room_rent'] for row in results]
    train_X1 = [row['room_area'] for row in results]
    train_X2 = [row['contructed_year'] for row in results]
    train_X3 = [row['minutes_from_station'] for row in results]
    # print(train_X)
    # print(train_Y)
    # sys.exit()
    n_samples = len(train_X)
    # print(n_samples)
    # sys.exit()
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
    pred = tf.add(sum_list,b)
    # print(sum_list[0])
    # sys.exit()
    cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        count = 0
        for epoch in range(training_epochs):
            count += 1
            for (x, y) in zip(train_X, train_Y):
                sess.run(optimizer, feed_dict={X: x, Y: y})
            # Display logs per epoch step
            if (epoch+1) % display_step == 0:
                c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
        print("Optimization Finished!")
        training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
        print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')
        