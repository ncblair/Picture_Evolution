import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from PIL import Image
import _pickle

sess = tf.InteractiveSession()

# Discriminator and generator weights
dis_W1 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[784, 50]), name='dis_W1')
dis_b1 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[50]), name='dis_b1')
dis_W2 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[50, 50]), name='dis_W2')
dis_b2 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[50]), name='dis_b2')
dis_W3 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[50, 1]), name='dis_W3')
dis_b3 = tf.Variable(tf.random_uniform(minval=-.1,maxval=.1, shape=[1]), name='dis_b3')

gen_W1 = tf.Variable(tf.random_uniform(minval=-.1, maxval=.1, shape=[784, 50]), name="gen_W1")
gen_b1 = tf.Variable(tf.random_uniform(minval=-.1, maxval=.1, shape=[50]), name="gen_b1")
gen_W2 = tf.Variable(tf.random_uniform(minval=-.1, maxval=.1, shape=[50, 784]), name="gen_W2")
gen_b2 = tf.Variable(tf.random_uniform(minval=-.1, maxval=.1, shape=[784]), name="gen_b2")


# returns the feed forward through discriminator
def get_discriminator(input_):
	dis_a2 = tf.sigmoid(tf.matmul(input_, dis_W1) + dis_b1)
	dis_a3 = tf.sigmoid(tf.matmul(dis_a2, dis_W2) + dis_b2)
	# No activation on last layer in order to reduce discriminator saturation
	dis_y_h = tf.matmul(dis_a3, dis_W3) + dis_b3

	return dis_y_h


# returns the feed forward through generator
def get_generator(input_):
	gen_a2 = tf.sigmoid(tf.matmul(input_, gen_W1) + gen_b1)
	gen_y_h = tf.matmul(gen_a2, gen_W2) + gen_b2

	return gen_y_h

def get_images_of_num(num):
	mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
	images = mnist.train.images
	labels = mnist.train.labels
	to_ret = []
	for i in range(len(labels)):
		if np.argmax(labels[i]) == num:
			to_ret.append(images[i])
	return to_ret


batch_size = 100
num_to_train = 2

real_data = get_images_of_num(num_to_train)

# discriminator and generator placeholder inputs
dis_x = tf.placeholder(tf.float32, shape=[batch_size, 784], name='dis_x')
gen_x = tf.placeholder(tf.float32, shape=[batch_size, 784], name='gen_x')

# discriminator y_hats for normal discriminator training and generator training
dis_y_hat = get_discriminator(dis_x)
gen_y_hat = get_generator(gen_x)
dis_from_gen = get_discriminator(gen_y_hat)


sess.run(tf.global_variables_initializer())


# Loss functions
dis_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=dis_y_hat, labels=tf.ones_like(dis_y_hat)))
dis_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=dis_y_hat, labels=tf.zeros_like(dis_y_hat)))

gen_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=dis_from_gen, labels=tf.ones(shape=dis_from_gen.shape)))


# Trainers
# Need to only train the discriminator weights when running dis_loss and the same for the generator so we have
# to separate var_lists
theta = tf.trainable_variables()
dis_vars = [v for v in theta if "dis_" in v.name]
gen_vars = [v for v in theta if "gen_" in v.name]

dis_trainer_real = tf.train.AdamOptimizer(0.005).minimize(dis_loss_real, var_list=dis_vars)
dis_trainer_fake = tf.train.AdamOptimizer(0.005).minimize(dis_loss_real, var_list=dis_vars)
gen_trainer = tf.train.AdamOptimizer(0.001).minimize(gen_loss, var_list=gen_vars)


# Train
for i in range(3000):
	np.random.shuffle(real_data)
	batch = real_data[:batch_size]

	sess.run()

