

# load data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


import tensorflow as tf

# launch interactive session
sess = tf.InteractiveSession()

# placeholders for inputs & outputs
# filled with vals when we ask tf to run a computation
# first dimension of None means batch size can be of any size
# shape param is optional but lets tf do type checking (ish) on tensors
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])


# variables are values that live inside tf computation graph
#  can be used/changed by computaiton
# better than placeholders (inputs) for weights because mutable
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# assign values to *all* variables
sess.run(tf.initialize_all_variables())


# predict class
y = tf.matmul(x, W) + b
# loss (cross entropy)
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))


# metaop: adds new ops to graph: compute gradients, compute param updates, apply param updates
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# train model
for i in range(1000):
    # minibatch of 100
    batch = mnist.train.next_batch(100)
    # feed dict fills/replaces placeholderswith given values
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})



correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})
# 92%





#####################################################
#####################################################
#####################################################


#init weights from gaussian
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

# init biaese with constants
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# stride len of 1
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding="SAME")

# pool over 2x2 blocks
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1,2,2,1], padding='SAME')

# LAYER 1: 28x28x1 input to 28x28x32
# convolve over 5x5 patches, 1 input channel, 32 output channels
W_conv1 = weight_variable([5,5,1,32])
b_conv1 = bias_variable([32])

# dim 4 = num color channels
x_image = tf.reshape(x, [-1,28,28,1])

# convolve over x_image w W_conv1, add bias, apply relu, max pool
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


# LAYER 2: 28x28x32 input to 28x28x64 (they say 7x7x64???)
W_conv2 = weight_variable([5,5,32,64])
b_conv2 = bias_variable([64])
# takes output of last layer (h_pool1) as input
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)


# LAYER 3: fully connected: 7x7x64 to 1024
W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)


# dropout for regularization
# use prob of keeping as variable so that we can toggle it on/off
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)


# LAYER 4: fully connected: 1024 to 10
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2


#########
#### MODEL TRAINING
###########


cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
sess.run(tf.initialize_all_variables())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g"%(i, train_accuracy))
    # pass dropout rate through feed_dict
    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))
