import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from PIL import Image

class MNISTnet:
	def __init__(self, input_data, number):
		self.data = input_data
		self.num = number

		# Begin session
		self.sess = tf.InteractiveSession()

		

		self.x = tf.placeholder(tf.float32, shape=[None, 784])
		self.y = tf.placeholder(tf.float32, shape=[None, 1])
		W1 = tf.Variable(tf.zeros([784, 30]))
		b1 = tf.Variable(tf.zeros([30]))
		W2 = tf.Variable(tf.zeros([30, 1]))
		b2 = tf.Variable(tf.zeros([1]))

		a2 = tf.sigmoid(tf.matmul(self.x, W1) + b1)
		self.y_hat = tf.sigmoid(tf.matmul(a2, W2) + b2)
		

		self.sess.run(tf.global_variables_initializer())

	

	def train(self):

		cost = tf.reduce_mean((self.y - self.y_hat)**2)
		train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cost)


		tf.global_variables_initializer().run()

		# Perform training
		for i in range(1000):
			batch_xs, batch_ys = self.data.train.next_batch(100)
			changed_ys = batch_ys[:, [self.num]]

			self.sess.run(train_step, feed_dict={self.x: batch_xs, self.y: changed_ys})

			#if i % 100 == 0:
			#	print(self.y.eval(feed_dict={self.x:batch_xs}))


	def prepro_edge_detector(self):
		print("  -  Detecting Edges")


	def prepro_round(self):
		print("  -  Maximizing Contrast")
		for n in range(len(self.data.train.images)):
			self.data.train.images[n] = np.round(self.data.train.images[n])



	def score(self, image):
		val = self.y_hat.eval(feed_dict={self.x: image})
		#print(val)
		return val

	def shut(self):
		self.sess.close()
