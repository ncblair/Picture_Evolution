from mutator import *
from score import *

import copy

def evolve_grayscale(images, net):
	returnVal = []
	for image in images:
		returnVal.append((image, mlScore(image, net)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: -1*x[1])]
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate_grayscale(x) for x in survivors]

	newGen = survivors + mutated
	return newGen

def evolve_black_and_white(images, net):
	returnVal = []
	for image in images:
		returnVal.append((image, mlScore(image, net)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: -1*x[1])]
	#print("_____________")
	#for im in returnVal:
		#print(mlScore(im, net))
	survivors = returnVal[:len(returnVal)//2]
	#print("_____________")
	#for im in survivors:
		#print(mlScore(im, net))

	mutated = [mutate_black_and_white(x) for x in survivors]

	newGen = survivors + mutated
	#print("_______x_____")
	#for im in newGen:
		#print(mlScore(im, net))
	return newGen

def evolve_black_and_white_strokes(images, net):
	returnVal = []
	for image in images:
		returnVal.append((image, mlScore(image, net)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: -1*x[1])]
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate_black_and_white_strokes(x) for x in survivors]

	newGen = survivors + mutated
	return newGen

def evolve_black_and_white_destructive(images, net):
	returnVal = []
	for image in images:
		returnVal.append((image, mlScore(image, net)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: -1*x[1])]
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate_black_and_white_destructive(x) for x in survivors]

	newGen = survivors + mutated
	return newGen