from evolution import evolve
from generateImages import genRandom
from Mutator import mutate

from PIL import _imaging
from PIL import Image
import unittest


class genRandomTest(unittest.TestCase):

	def testImagesReturned(self):
		randomList = genRandom(1, 1)
		self.assertEqual(str(type(randomList[0])), "<class 'PIL.Image.Image'>")
			
	def testLengthReturn(self):
		randomList = genRandom(10, 1)
		self.assertEqual(len(randomList), 10)

class mutateTest(unittest.TestCase):

	def testImageDifferent(self):
		randomList = genRandom(10, 4)
		for img in randomList:
			self.assertFalse(img == mutate(img))
			
	def testImageNotDestructed(self):
		randomList = genRandom(10, 4)
		oldList = []
		#arrcpy
		for img in randomList:
			oldList.append(img)
			#check no element was destroyed
		for i in range(len(randomList)):
			mutate(randomList[i])
			self.assertEqual(oldList[i], randomList[i])
			
		


if __name__ == '__main__':
    unittest.main()