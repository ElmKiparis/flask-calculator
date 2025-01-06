import unittest

from functions import *


class TestFunctions(unittest.TestCase):

    def test_add(self):

        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(2, -2), 0)
        self.assertEqual(add(4, 0), 4)

    def test_subtract(self):

        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(2, -2), 4)
        self.assertEqual(subtract(4, 0), 4)

    def test_multiply(self):

        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(2, -2), -4)
        self.assertEqual(multiply(4, 0), 0)

    def test_divide(self):

        self.assertEqual(divide(3, 5), 0.6)
        self.assertEqual(divide(2, -2), -1)
        self.assertEqual(divide(4, 1), 4)

    def test_power(self):

        self.assertEqual(power(3, 5), 243)
        self.assertEqual(power(2, -2), 0.25)
        self.assertEqual(power(4, 0), 1)


if __name__ == '__main__':
    unittest.main()
