import unittest
from code import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)

if __name__ == "__main__":
    unittest.main()
