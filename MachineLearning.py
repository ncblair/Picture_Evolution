import random
from PIL import Image
import Gen2
import numpy as np


def mlScore(image, net):
	score = net.score( np.reshape( list( image.getdata() ), (1, 784) ) )[0][0]
	return score


def grayScale(image):
	# convert to grayscale
	width,height = image.size

	total=0
	for i in range(width):
		for j in range(height):
			total += image.getpixel((i,j))
	return total
