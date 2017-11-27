import numpy as np

from PIL import Image

#returns an array of randomly generated images
def genRandom_grayscale(numImages, width):
	images = []
	for n in range(numImages):
		imarray = np.random.random((width, width)) * 255
		images.append(Image.fromarray(imarray.astype('uint8'), 'L'))
	return images

def genWhiter_grayscale(numImages, width):
	images = []
	for n in range(numImages):
		imarray = .25*np.random.random((width, width)) * 255
		images.append(Image.fromarray(imarray.astype('uint8'), 'L'))
	return images

def genWhite(numImages, width):
	images = []
	for n in range(numImages):
		imarray = np.full(fill_value=255,shape=((width,width)))
		images.append(Image.fromarray(imarray.astype('uint8'), 'L'))
	return images


def genRandom_black_and_white(numImages, width):
	images = []
	for n in range(numImages):
		imarray = np.round(np.random.random((width, width))) * 255
		images.append(Image.fromarray(imarray.astype('uint8'), 'L'))
	return images

