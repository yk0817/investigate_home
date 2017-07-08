from common import *
rng = np.random

learning_rate = 0.03
training_epochs = 1000
# training_epochs = 10
display_step = 50

with connection.cursor() as cursor:
    sql = "select room_rent,room_area from house_price;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # 内包表記で計算してみる
    train_Y = [row['room_rent'] for row in results]
    train_X = [row['room_area'] for row in results]
    n_samples = len(train_X)
    X = tf.placeholder("float")
    Y = tf.placeholder("float")
    # Set model weights
    # 変数を定義    
    W = tf.Variable(rng.randn(), name="weight")
    b = tf.Variable(rng.randn(), name="bias")
    pred = tf.add(tf.multiply(X, W), b)
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
            if count % 10 == 0:
                print("counter:NO",count)
                training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
                print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b))
        print("Optimization Finished!","\n")
        print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b))

connection.close()
