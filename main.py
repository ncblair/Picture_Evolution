from evolution import evolve
from generateImages import genRandom

NUM_IMAGES = 10;
IMAGE_WIDTH = 10;
def main():
	images =  genRandom(NUM_IMAGES, IMAGE_WIDTH)
	count = 0
	while count < 1000:
		images = evolve(images)
		count = count + 1

	print(len(images))
	for n in range(len(images)):
		print("hello")
		images[n].save("images/result_image" + str(n) + ".png")
	

main()