#encoding:UTF-8
import tensorflow as tf
import input_data


def load_data():
    mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
    return mnist


if __name__ == '__main__':
    mnist = load_data()
    sess = tf.InteractiveSession()
    x = tf.placeholder("float", shape=[None, 784])
    y_ = tf.placeholder("float", shape=[None, 10])

    # variables
    w = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))

    # Before Variables can be used within a session, they must be initialized using that session
    sess.run(tf.initialize_all_variables())

    y = tf.nn.softmax(tf.matmul(x, w) + b)
    cross_entropy = - tf.reduce_sum(y_*tf.log(y))

    # training
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    for i in range(1000):
        batch = mnist.train.next_batch(50)
        train_step.run(feed_dict={x: batch[0], y_: batch[1]})

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})