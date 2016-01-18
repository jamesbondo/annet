import input_data
import tensorflow as tf
import math


if __name__ == '__main__':
    images_placeholder = tf.placeholder(tf.float32, shape=(batch_size, IMAGE_PIXELS))
    labels_placeholder = tf.placeholder(tf.int32, shape=(batch_size))

    with tf.name_scope('hidden1') as scope:
        weights = tf.Variable(tf.truncated_normal([IMAGE_PIXELS, hidden1_units], stddev=1.0/math.sqrt(float(IMAGE_PIXELS))), name='weights')
        biases = tf.Variable(tf.zeros([hidden1_units]), name='biases')

    hidden1 = tf.nn.relu(tf.matmul(images, weights) + biases)
    hidden2 = tf.nn.relu(tf.matmul(hidden1, weights) + biases)
    logits = tf.matmul(hidden2, weights) + biases
    batch_size = tf.size(labels)
    labels = tf.expand_dims(labels, 1)
    indices = tf.expand_dims(tf.range(0, batch_size, 1), 1)
    concated = tf.concat(1, [indices, labels])
    onehot_labels = tf.sparse_to_dense(concated, tf.pack([batch_size, NUM_CLASSES]), 1.0, 0.0)
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits, onehot_labels, name='xentropy')
    loss = tf.reduce_mean(cross_entropy, name='xentropy_mean')
    tf.scalar_summary(loss.op.name, loss)
