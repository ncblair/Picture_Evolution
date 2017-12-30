from evolution import *
from generateImages import *
from Net import MNISTnet
from PIL import Image, ImageFilter
from scipy.ndimage import morphology
import numpy as np
from skimage.morphology import skeletonize

# Uncomment if training again
from tensorflow.examples.tutorials.mnist import input_data

NUM_IMAGES = 4
IMAGE_WIDTH = 28
NUMBER_TO_GENERATE = 2

def main():
	# print("Loading Input Data")
	# #Load Input  
	in_data = input_data.read_data_sets('MNIST_data', one_hot=True)

	print("Initializing Net")
	#Initialize Net Object
	mnistNet = MNISTnet(number=NUMBER_TO_GENERATE, input_data=in_data)
	#mnistNet = MNISTnet(number=NUMBER_TO_GENERATE)

	# print("Preprocessing Image Data")
	#Preprocess Image Data
	mnistNet.prepro_round()
	#mnistNet.prepro_edge_detector()
	#mnistNet.prepro_skeletonize()

	# print("Training Neural Net")
	#print("Loading Neural Net")
	#Train Net
	#mnistNet.load_net()
	mnistNet.train()

	print("Running Evolutionary Algorithm")
	#Run Evolutionariy Algorithm
	#images =  genRandom_black_and_white(NUM_IMAGES, IMAGE_WIDTH)
	images = genRandom_black_and_white(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 5000:
		images = evolve_black_and_white(images, mnistNet)
		count = count + 1
		if count % 5000 == 0:
			images[0].show()


	images[0].show()
	print(np.asarray(images[0]))
	print("Resizing, Denoising, and Saving Images to File")
	#Resize, Denoise and Save Images to File
	for n in range(len(images)):
		images[n] = images[n].resize((28, 28))
		imarray = np.asarray(images[n])
		imarray = morphology.binary_opening(np.asarray(images[n]), structure=np.ones((3,3)))
		imarray = 255 * skeletonize(imarray)
		print(imarray)
		images[n] = Image.fromarray(imarray.astype('uint8'), 'L')
		images[n].save("./images/picturing_a_" + str(NUMBER_TO_GENERATE) + "_res" + str(n) + ".png")
	images[0].show()
	#Close Neural Net
	mnistNet.shut()






if __name__ == "__main__":
    import timeit
    setup = "from __main__ import main"
    print("Running Main")
    print(timeit.timeit("main()", setup=setup, number = 1))