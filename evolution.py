from Mutator import mutate
from MachineLearning import mlScore
import copy

def evolve(images):
	returnVal = []
	for image in images:
		returnVal.append((image, mlScore(image)))
	returnVal = [x[0] for x in sorted(returnVal, key = lambda x: x[1])]
	survivors = returnVal[:len(returnVal)//2]

	mutated = [mutate(x) for x in survivors]

	newGen = survivors + mutated

	return newGen
