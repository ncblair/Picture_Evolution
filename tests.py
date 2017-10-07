from evolution import evolve
from generateImages import genRandom
from PIL import Image
import unittest


class genRandomTest(unittest.TestCase):

	def testImagesReturned(self):
		randomList = genRandom(1, 1)
		self.assertEqual(str(type(randomList[0])), "<class 'PIL.Image.Image'>")
			
	def testLengthReturn(self):
		randomList = genRandom(10, 1)
		self.assertEqual(len(randomList), 10)


if __name__ == '__main__':
    unittest.main()