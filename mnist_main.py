from evolution import *
from generateImages import *
from Net import MNISTnet
from Display import *
from PIL import Image, ImageFilter
from scipy.ndimage import morphology
import numpy as np
from skimage.morphology import skeletonize

# Uncomment if training again
from tensorflow.examples.tutorials.mnist import input_data

IMAGE_WIDTH = 28

def mnist_run(num_images=4, number_to_generate=2, retrain=0, evolution_iters=5000):
	if retrain == "Y":
		print("Loading Input Data")
		# #Load Input
		in_data = input_data.read_data_sets('MNIST_data', one_hot=True)
		
		print("Initializing Net")
		#Initialize Net Object
		mnistNet = MNISTnet(input_data=in_data, number=number_to_generate)


		print("Preprocessing Image Data")
		#Preprocess Image Data
		mnistNet.prepro_round()
		#mnistNet.prepro_edge_detector()
		#mnistNet.prepro_skeletonize()

		print("Training Neural Net")
		#Train Net
		mnistNet.train()

	else:
		print("Initializing Net")
		#Initialize Net Object
		mnistNet = MNISTnet()

		print("Loading Neural Net")
		#Load Net
		mnistNet.load_net()
	

	images = genBlack(num_images, IMAGE_WIDTH)
	x = 1
	print("Running Evolutionary Algorithm")
	#Run Evolutionariy Algorithm
	while x < 11:

		count = 0
		while count < evolution_iters / 10:
			images = evolve_black_and_white_strokes(images, mnistNet)
			count = count + 1


		print(str(x*10) + "% ______________________")
		#Resize, Denoise and Save Images to File
		for n in range(len(images)):
			imarray = np.asarray(images[n])
			imarray = morphology.binary_opening(np.asarray(images[n]), structure=np.ones((3,3)))
			if x == 9:
				imarray = skeletonize(imarray)
			imarray = imarray * 255
			#print(imarray)
			images[n] = Image.fromarray(imarray.astype('uint8'), 'L')
			images[n].save("./images/picturing_a_" + str(number_to_generate) + "_res" + str(n) + ".png")
		if x == 9:
			images[0].show()
		x += 1
	images[0].show()
	
	#Close Neural Net
	mnistNet.shut()

