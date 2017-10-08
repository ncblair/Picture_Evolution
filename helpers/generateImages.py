
import numpy

from PIL import Image

#returns an array of randomly generated images
def genRandom(numImages, width):
	images = []
	for n in range(numImages):
		imarray = numpy.random.rand(width, width, 3) * 255
		images.append(Image.fromarray(imarray.astype('uint8')).convert('RGBA'))
	return images

