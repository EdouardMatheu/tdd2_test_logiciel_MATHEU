import functions
import unittest

class TestFunctions(unittest.TestCase):

	def test_mirror(self):
		self.assertEqual(functions.mirror("abcde", 3), "abcddcba")
		self.assertEqual(functions.mirror("abcde", 0), "aa")
		self.assertEqual(functions.mirror("abcde", 1), "abba")
		self.assertEqual(functions.mirror("abcdefghijklmnopqrstuvwxyz", 25), "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba")
		self.assertEqual(functions.mirror("abcde", -1), "")

	def test_deriv(self):
		self.assertEqual(functions.deriv({0.0, 1.0, 2.0, 3.0, 4.0}), {1.0, 1.0, 1.0, 1.0})
		self.assertEqual(functions.deriv({0.0, 1.0, 4.0, 9.0, 16.0}), {2.0, 4.0, 6.0, 8.0})
		self.assertEqual(functions.deriv({0.0, -1.0, -2.0, -3.0, -4.0}), {-1.0, -1.0, -1.0, -1.0})
		self.assertEqual(functions.deriv({1.0, 1.0, 1.0, 1.0, 1.0}), {0.0, 0.0, 0.0, 0.0})

if __name__ == '__main__':
	unittest.main()