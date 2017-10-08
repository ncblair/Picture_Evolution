from helpers.evolution import evolve
from helpers.generateImages import genRandom

NUM_IMAGES = 10
IMAGE_WIDTH = 5
def engine():
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 1000:
		images = evolve(images)
		count = count + 1
	for n in range(len(images)):
		images[n].save("./static/images/result_image" + str(n) + ".png")
	return images[0]
