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
	imarray = np.asarray(image)
	mask = np.reshape(np.random.choice([0, 255], size=imarray.size, p=[.99, .01]), imarray.shape)
	new_imarray = np.bitwise_or(mask, imarray)
	mask = np.reshape(np.random.choice([0, 255], size=imarray.size, p=[.01, .99]), imarray.shape)
	np.bitwise_and(mask, new_imarray, new_imarray)
	return Image.fromarray(new_imarray.astype('uint8'), 'L')

def mutate_black_and_white_destructive(image):
	imarray = np.asarray(image)
	mask = np.reshape(np.random.choice([0, 255], size=imarray.size, p=[.025, .975]), imarray.shape)
	new_imarray = np.bitwise_and(mask, imarray)
	return Image.fromarray(new_imarray.astype('uint8'), 'L')


def mutate_black_and_white_strokes(image):
	newImage = None
	if random.random() > .4:
		newImage = paintBlackRandomStroke(image)
	else:
		newImage = paintWhiteRandomStroke(image)
	return newImage

def paintWhiteRandomStroke(image):
	imarray = np.asarray(image).astype('uint8')
	mask = np.zeros(imarray.shape).astype('uint8')
	breshenham(mask)
	imarray_ = np.bitwise_or(mask, imarray)
	return Image.fromarray(imarray_.astype('uint8'), 'L')

def paintBlackRandomStroke(image):
	imarray = np.asarray(image).astype('uint8')
	mask = np.zeros(imarray.shape).astype('uint8')
	breshenham(mask)
	invert_BW(mask)
	imarray_ = np.bitwise_and(mask, imarray)
	return Image.fromarray(imarray_.astype('uint8'), 'L')


def invert_BW(arr):
	arr = np.bitwise_xor(arr, 255 * np.ones(arr.shape).astype('uint8'))

def breshenham(arr):
	x0 = int(random.random()*arr.shape[0] * 3 / 4)
	x1 = x0
	while x1 == x0:
		x1 = int(x0 + (random.random() - .5)*arr.shape[0] / 2)

	y0 = int(random.random()*arr.shape[1] * 3 / 4)
	y1 = y0
	while y0 == y1:
		y1 = int(y0 + (random.random() - .5)*arr.shape[1] / 2)
	#compute breshenham
	dx = x1 - x0
	dy = y1 - y0
	error = np.absolute(dy/dx)
	realErr = 0.0
	y = y0
	for x in range(x0, x1 + 1):
		arr[x][y] = 255
		while error > 0.5:
			y = y + np.sign(dy)
			error -= 1

