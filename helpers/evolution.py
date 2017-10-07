from Mutator import mutate
from MachineLearning import mlScore, grayScale
import copy

def evolve(images):
	returnVal = []
	for image in images:
		returnVal.append((image, grayScale(image)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: -1*x[1])]
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate(x) for x in survivors]

	newGen = survivors + mutated
	return newGen