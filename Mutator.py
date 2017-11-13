from PIL import Image

import numpy

import random

def mutate(image):
	pixelMap = image.load()

	#new 2d array
	newImage = image.copy()

	newImageMap = newImage.load()
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if random.random() > .95:
				a = random.random()*255
				
				newImageMap[i, j] = int(a)
			else:
				newImageMap[i, j] = pixelMap[i, j]
	return newImage


