import unittest
from Task0 import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(-3, -7), -10)
        self.assertEqual(add(1000000, 1), 1000001)
        self.assertAlmostEqual(add(-1.1, -2.2), -3.3, places=7)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(add(-100, 100), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertEqual(subtract(10, 0), 10)
        self.assertEqual(subtract(-5, 5), -10)
        self.assertEqual(subtract(1.5, 0.5), 1.0)
        self.assertEqual(subtract(-10, -5), -5)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=7)
        self.assertEqual(subtract(1000000, 1), 999999)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-1, 3), -3)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(-2, -8), 16)
        self.assertEqual(multiply(1.5, -2), -3.0)
        self.assertAlmostEqual(multiply(1000, 0.001), 1.0, places=7)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(-1, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, -1), -5)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(5, 0), "Error: Division by zero")
        self.assertEqual(divide(-8, 2), -4)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-9, -3), 3)
        self.assertEqual(divide(0, -5), 0)
        self.assertEqual(divide(1.5, 0.5), 3.0)
        self.assertEqual(divide(0, 100), 0)
        self.assertEqual(divide(100, 0), "Error: Division by zero")
        self.assertAlmostEqual(divide(1, 3), 1/3, places=7)


if __name__ == "__main__":
    unittest.main()
        