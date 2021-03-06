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
		self.assertEqual(functions.deriv([0.0, 1.0, 2.0, 3.0, 4.0]), [1.0, 1.0, 1.0, 1.0])
		self.assertEqual(functions.deriv([0.0, 1.0, 4.0, 9.0, 16.0]), [1.0, 3.0, 5.0, 7.0])
		self.assertEqual(functions.deriv([0.0, -1.0, -2.0, -3.0, -4.0]), [-1.0, -1.0, -1.0, -1.0])
		self.assertEqual(functions.deriv([1.0, 1.0, 1.0, 1.0, 1.0]), [0.0, 0.0, 0.0, 0.0])
		self.assertEqual(functions.deriv([1.0]), None)
		self.assertEqual(functions.deriv(['h', 'e', 'l', 'l', 'o']), None)
		self.assertEqual(functions.deriv([1, 2, 3, 4, 5]), None)

	def test_deriv2(self):
		self.assertEqual(functions.deriv2([0.0, 1.0, 2.0, 3.0, 4.0]), [0.0, 0.0, 0.0])
		self.assertEqual(functions.deriv2([0.0, 1.0, 4.0, 9.0, 16.0]), [2.0, 2.0, 2.0])
		self.assertEqual(functions.deriv2([0.0, 1.0, 8.0, 21.0, 64.0]), [6.0, 6.0, 30.0])
		self.assertEqual(functions.deriv2([0.0, -1.0, -2.0, -3.0, -4.0]), [0.0, 0.0, 0.0])
		self.assertEqual(functions.deriv2([1.0, 1.0, 1.0, 1.0, 1.0]), [0.0, 0.0, 0.0])
		self.assertEqual(functions.deriv2([1.0]), None)
		self.assertEqual(functions.deriv2(['h', 'e', 'l', 'l', 'o']), None)
		self.assertEqual(functions.deriv2([1, 2, 3, 4, 5]), None)

	def test_derivapprox(self):
		self.assertEqual(functions.derivapprox(functions.f_x2, 0.0001, 2.379561), 4.7591)
		self.assertEqual(functions.derivapprox(functions.f_x2, 0.1, 2.379561), 4.8)
		self.assertEqual(functions.derivapprox(functions.f_x2, 0.0, 2.379561), 0.0)
		self.assertEqual(functions.derivapprox(functions.f_x2, 0.001, 0.00000001), 0.0)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, 0.0001, 2.379561), -33.9739)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, 0.1, 2.379561), -34.0)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, 0.0, 2.379561), 0.0)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, 0.001, 0.00000001), 0.0)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, 2.0, 0.00000001), None)
		self.assertEqual(functions.derivapprox(functions.f_minus2x3, -0.01, 0.00000001), None)

if __name__ == '__main__':
	unittest.main()