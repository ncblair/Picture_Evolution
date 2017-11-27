from PIL import Image

import numpy as np

import random

def mutate_grayscale(image):
	pixelMap = image.load()

	#new 2d array
	newImage = image.copy()

	newImageMap = newImage.load()
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if random.random() > .95:
				a = random.random() * 255
				
				newImageMap[i, j] = int(a)
			else:
				newImageMap[i, j] = pixelMap[i, j]
	return newImage


def mutate_black_and_white(image):
	pixelMap = image.load()

	#new 2d array
	newImage = image.copy()

	newImageMap = newImage.load()
	for i in range(image.size[0]):
		for j in range(image.size[1]):
			if random.random() > .95:
				a = round(random.random()) * 255
				
				newImageMap[i, j] = int(a)
			else:
				newImageMap[i, j] = pixelMap[i, j]
	return newImage


def paintBlackRandomStroke(image):
	imarray = np.asarray(image)
	x, y = imarray.shape
	mask = np.zeros(imarray.shape)
	breshenham(mask)
	imarray_ = np.logical_or(mask, imarray)
	return Image.fromarray(imarray_.astype('uint8'), 'L')


def breshenham(arr):
	x0 = int(random.random()*x * 3 / 4)
	x1 = -1
	while x1 != x0:
		x1 = int(x0 + (random.random() - .5)*x / 2)

	y0 = int(random.random()*y * 3 / 4)
	y1 = -1
	while y0 != y1:
		y1 = int(y0 + (random.random() - .5)*y / 2)
	#compute breshenham
	dx = x1 - x0
	dy = y1 - y0
	err = np.absolute(dy/dx)
	realErr = 0.0
    y = y0
    for x in range(x0, x1 + 1):
    	arr[x][y] = 1
    	while error > 0.5:
    		y = y + np.sign(deltay)
    		error -= 1

