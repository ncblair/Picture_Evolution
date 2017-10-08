
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
			if random.random() > .95:
				"""
				randMult = random.random()
				a = randMult*newImageMap[i, j][0] + (1 - randMult)*random.random()*255
				randMult = random.random()
				b = randMult*newImageMap[i, j][0] + (1 - randMult)*random.random()*255
				randMult = random.random()
				c = randMult*newImageMap[i, j][0] + (1 - randMult)*random.random()*255
				"""
				a = random.random()*255
				b = random.random()*255
				c = random.random()*255
				
				newImageMap[i, j] = (int(a), int(b), int(c))
			else:
				newImageMap[i, j] = pixelMap[i, j]
	return newImage


