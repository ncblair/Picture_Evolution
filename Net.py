from skimage import feature
from skimage.morphology import skeletonize
import tensorflow as tf
import numpy as np
from PIL import Image
import _pickle
from scipy import ndimage

class MNISTnet:
	def __init__(self, input_data=None, number=2):
		self.data = input_data
		self.num = number

		# Begin session
		self.sess = tf.InteractiveSession()

		self.x = tf.placeholder(tf.float32, shape=[None, 784])
		self.y = tf.placeholder(tf.float32, shape=[None, 1])
		self.W1 = tf.Variable(tf.zeros([784, 50]))
		self.b1 = tf.Variable(tf.zeros([50]))
		self.W2 = tf.Variable(tf.zeros([50, 1]))
		self.b2 = tf.Variable(tf.zeros([1]))

		a2 = tf.sigmoid(tf.matmul(self.x, self.W1) + self.b1)
		self.y_hat = tf.sigmoid(tf.matmul(a2, self.W2) + self.b2)

		self.sess.run(tf.global_variables_initializer())

	def train(self):
		cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.y_hat, labels=self.y))
		train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cost)
		correct_prediction = tf.equal(self.y > .5, self.y_hat > .5)
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		tf.global_variables_initializer().run()

		# Perform training
		for i in range(3000):
			batch_xs, batch_ys = self.data.train.next_batch(100)
			changed_ys = batch_ys[:, [self.num]]

			self.sess.run(train_step, feed_dict={self.x: batch_xs, self.y: changed_ys})

			# if i % 100 == 0:
			# 	print(self.y.eval(feed_dict={self.x:batch_xs}))


		print("Accuracy on Test Set:", self.sess.run([accuracy], feed_dict={self.x: self.data.test.images, self.y: self.data.test.labels[:, [self.num]]}))

		dict_rep = {"W1": self.W1.eval(), "b1": self.b1.eval(), "W2": self.W2.eval(), "b2": self.b2.eval()}
		output = open('trainedMNIST.pkl', 'wb')
		_pickle.dump(dict_rep, output)
		output.close()

	def load_net(self):
		dict_ = _pickle.load(open('trainedMNIST.pkl', 'rb'))
		w1_op = self.W1.assign(dict_["W1"])
		b1_op = self.b1.assign(dict_["b1"])
		w2_op = self.W2.assign(dict_["W2"])
		b2_op = self.b2.assign(dict_["b2"])
		self.sess.run(w1_op)
		self.sess.run(b1_op)
		self.sess.run(w2_op)
		self.sess.run(b2_op)


	def prepro_edge_detector(self):
		print("  -  Detecting Edges")
		for n in range(len(self.data.train.images)):
			im = np.reshape(self.data.train.images[n], (28, 28))
			self.data.train.images[n] = np.ndarray.flatten(feature.canny(im))
		#imarray = np.reshape(self.data.train.images[0],(28, 28)) * 255
		#Image.fromarray(imarray.astype('uint8'), 'L').show()



	def prepro_round(self):
		print("  -  Maximizing Contrast")
		for n in range(len(self.data.train.images)):
			self.data.train.images[n] = np.round(self.data.train.images[n])
		#imarray = np.reshape(self.data.train.images[0],(28, 28)) * 255
		#Image.fromarray(imarray.astype('uint8'), 'L').show()

	def prepro_skeletonize(self):
		print("  -  Skeletonizing")
		for n in range(len(self.data.train.images)):
			im = np.reshape(self.data.train.images[n], (28, 28))
			self.data.train.images[n] = np.ndarray.flatten(skeletonize(im))
		#imarray = np.reshape(self.data.train.images[0],(28, 28)) * 255
		#Image.fromarray(imarray.astype('uint8'), 'L').show()


	def score(self, image):
		val = self.y_hat.eval(feed_dict={self.x: image})
		#print(val)
		return val

	def shut(self):
		self.sess.close()
