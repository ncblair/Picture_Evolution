from evolution import evolve
from generateImages import genRandom

NUM_IMAGES = 1000;
IMAGE_WIDTH = 100;
def main():
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 1000:
		images = evolve(images)
		count = count + 1

print(main())