from evolution import evolve
from generateImages import genRandom

NUM_IMAGES = 12
IMAGE_WIDTH = 5
def main():
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 100:
		images = evolve(images)
		count = count + 1

	for n in range(len(images)):
		images[n].save("../images/result_image" + str(n) + ".png")
	

main()