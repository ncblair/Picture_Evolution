from evolution import evolve
from generateImages import genRandom

NUM_IMAGES = 10
IMAGE_WIDTH = 5
def main():
    return "http://nathanblair.me/assets/img/nathanCloseUp.JPG"
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 10000:
		images = evolve(images)
		count = count + 1

	for n in range(len(images)):
		images[n].save("../static/images/result_image" + str(n) + ".png")
	return images[0]
main()