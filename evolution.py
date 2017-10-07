from Mutator import mutate


def evolve(images) :
	return[]
	evolvedImages = []

	for image in images:
		evolvedImages.append((image, mlScore(image)))

	#sort it, get the first value
	evolvedImages = sorted(evolvedImages, key=lambda x: x[1])
	evolvedImages = [x[0] for x in evolvedImages[:len(evolvedImages)//2]]

	mutatedImages = []

	for image in evolvedImages:
		mutatedImages.append((image, mutate(image)))

	images.extend(mutatedImages)
	return images
