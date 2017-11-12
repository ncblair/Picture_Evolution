import numpy as np

from PIL import Image

#returns an array of randomly generated images
def genRandom(numImages, width):
	images = []
	for n in range(numImages):
		imarray = np.random.random((width, width)) * 255
		images.append(Image.fromarray(imarray.astype('uint8'), 'L'))
	return images

