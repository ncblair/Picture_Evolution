import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from decimal import Decimal

class Gen2:
	def __init__(self):
		self.mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
		# Begin session
		self.sess = tf.InteractiveSession()

		self.x = tf.placeholder(tf.float32, shape=[None, 784])
		self.y = tf.placeholder(tf.float32, shape=[None, 1])
		W1 = tf.Variable(tf.zeros([784, 1]))
		b1 = tf.Variable(tf.zeros([1]))
		self.y_hat = (tf.matmul(self.x, W1) + b1)

		cross_entropy = tf.reduce_mean(
		    tf.nn.softmax_cross_entropy_with_logits(labels=self.y, logits=self.y_hat))

		train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

		self.sess.run(tf.global_variables_initializer())



		# Perform training
		for i in range(1000):
			batch = self.mnist.train.next_batch(100)
			y_changed = batch[1][:]
			y_changed = y_changed[:,[2]]
			train_step.run(feed_dict={self.x: batch[0], self.y:y_changed})
			if i % 100 == 0:
				print(self.y_hat.eval(feed_dict={self.x:batch[0]}))

		# Converts all test results into 1 or 0
		correct_prediction = tf.equal(tf.greater(self.y,.5), tf.greater(self.y_hat,.5))
		self.accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		self.changed = self.mnist.test.labels[:,[2]]
		print(self.changed)
		print(self.accuracy.eval(feed_dict={self.x: self.mnist.test.images, self.y: self.changed}))


	def score(self, image):
		return self.y_hat.eval(feed_dict={self.x: image})

	def shut(self):
		self.sess.close()
