from PIL import Image

import numpy

import random

def mutate(image):
	pixelMap = image.load()

	#new 2d array
	newImage = image.copy()

	newImageMap = newImage.load()
	#newImageArr = [[0 for x in range(image.size[0])] for y in range(image.size[1])] 
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if random.random() > .3:
				newImageMap[i, j] = (int(random.random()*255), int(random.random()*255), int(random.random()*255//1))
			else:
				newImageMap[i, j] = pixelMap[i, j]
	return newImage


