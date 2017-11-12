from evolution import evolve
from generateImages import genRandom
from Gen2 import Gen2

NUM_IMAGES = 4
IMAGE_WIDTH = 28
def engine():
	net = Gen2()
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 10000:
		images = evolve(images, net)
		count = count + 1
	for n in range(len(images)):
		images[n].save("./images/result_image" + str(n) + ".png")

	net.shut()

engine()