from evolution import evolve
from generateImages import genRandom
from Net import Net

from tensorflow.examples.tutorials.mnist import input_data

NUM_IMAGES = 4
IMAGE_WIDTH = 28
def engine():
	print("INPUT")
	print(input_data.read_data_sets('MNIST_data', one_hot=True))
	print("DONE INPUT")
	mnist2Net = Net(input_data.read_data_sets('MNIST_data', one_hot=True))
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 10000:
		images = evolve(images, mnist2Net)
		count = count + 1
	for n in range(len(images)):
		images[n].save("./images/result_image" + str(n) + ".png")

	mnist2Net.shut()

engine()