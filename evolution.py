from Mutator import mutate_grayscale, mutate_black_and_white
from score import mlScore, grayScale

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
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate_black_and_white(x) for x in survivors]

	newGen = survivors + mutated
	return newGen