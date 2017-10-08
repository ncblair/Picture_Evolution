import random

from PIL import Image


def mlScore(image):
	return int(random.random()*100)


def grayScale(image):
	# convert to grayscale
	width,height = image.size

	total=0
	for i in range(0,width):
		for j in range(0,height):
			total += image.getpixel((i,j))[0]
			total += image.getpixel((i,j))[1]
			total += image.getpixel((i,j))[2]

	print(total)
	return total
