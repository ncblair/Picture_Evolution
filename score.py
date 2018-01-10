# import random
# from PIL import Image
# import Net
# import numpy as np


def mlScore(image, net):
	normalizedIm = np.reshape( list( image.getdata() ), (1, 784) ) / 255
	score = net.score( normalizedIm )[0][0]
	return score






def grayScale(image):
	# convert to grayscale
	width,height = image.size

	total=0
	for i in range(width):
		for j in range(height):
			total += image.getpixel((i,j))
	return total
