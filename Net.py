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
		self.y_ = tf.placeholder(tf.float32, shape=[None, 1])
		W = tf.Variable(tf.zeros([784, 1]))
		b = tf.Variable(tf.zeros([1]))

		self.y = tf.matmul(self.x, W) + b
		

		self.sess.run(tf.global_variables_initializer())

	

	def train(self):

		cross_entropy = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(labels=self.y_, logits=self.y))
		train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


		tf.global_variables_initializer().run()

		# Perform training
		for i in range(1000):
			batch_xs, batch_ys = self.data.train.next_batch(100)
			changed_ys = batch_ys[:, [self.num]]

			self.sess.run(train_step, feed_dict={self.x: batch_xs, self.y_: changed_ys})

			#if i % 100 == 0:
			#	print(self.y.eval(feed_dict={self.x:batch_xs}))


	def prepro_edge_detector(self):
		print("  -  Detecting Edges")


	def prepro_round(self):
		print("  -  Maximizing Contrast")
		for n in range(len(self.data.train.images)):
			self.data.train.images[n] = np.round(self.data.train.images[n])



	def score(self, image):
		val = self.y.eval(feed_dict={self.x: image})
		#print(val)
		return val

	def shut(self):
		self.sess.close()
