import functions
import unittest

class TestFunctions(unittest.TestCase):

	def test_mirror(self):
		self.assertEqual(functions.mirror("abcde", 3), "abcddcba")
		self.assertEqual(functions.mirror("abcde", 0), "")
		self.assertEqual(functions.mirror("abcde", 1), "aa")
		self.assertEqual(functions.mirror("abcdefghijklmnopqrstuvwxyz", 25), "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba")
		self.assertEqual(functions.mirror("abcde", -1), "")

if __name__ == '__main__':
	unittest.main()