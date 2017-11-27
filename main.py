from evolution import evolve_grayscale, evolve_black_and_white
from generateImages import genRandom_grayscale, genRandom_black_and_white, genWhiter_grayscale, genWhite
from Net import MNISTnet
from PIL import Image, ImageFilter
from scipy.ndimage import morphology
import numpy as np
from PIL import ImageFilter

# Uncomment if training again
# from tensorflow.examples.tutorials.mnist import input_data

NUM_IMAGES = 4
IMAGE_WIDTH = 28
NUMBER_TO_GENERATE = 2

def main():
	# print("Loading Input Data")
	# #Load Input Data
	# in_data = input_data.read_data_sets('MNIST_data', one_hot=True)

	print("Initializing Net")
	#Initialize Net Object
	mnistNet = MNISTnet(number=NUMBER_TO_GENERATE)

	# print("Preprocessing Image Data")
	#Preprocess Image Data
	# mnistNet.prepro_round()

	# print("Training Neural Net")
	print("Loading Neural Net")
	#Train Net
	mnistNet.load_net()

	print("Running Evolutionary Algorithm")
	#Run Evolutionariy Algorithm
	images =  genRandom_black_and_white(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 10000:
		images = evolve_black_and_white(images, mnistNet)
		count = count + 1
		if count % 10000 == 0:
			images[0].show()


	# images[0] = images[0].filter(ImageFilter.ModeFilter(size=4))
	images[0].show()

	print("Resizing, Denoising, and Saving Images to File")
	#Resize, Denoise and Save Images to File
	for n in range(len(images)):
		images[n] = images[n].resize((28, 28))
		images[n] = Image.fromarray(morphology.grey_opening(np.reshape(list(images[n].getdata()), (28, 28))).astype(np.uint8))
		images[n].save("./images/picturing_a_" + str(NUMBER_TO_GENERATE) + "_res" + str(n) + ".png")
	images[0].show()
	#Close Neural Net
	mnistNet.shut()


print("Running Main")
main()