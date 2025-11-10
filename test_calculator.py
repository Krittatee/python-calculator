import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 3), 4)

    # Add the following test methods to the TestCalculator class:

    def test_add3(self):
        self.assertEqual(self.calc.add(5, -3), 2)
    def test_add2(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-7, 2), -9)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-5, 2), -10)
    
    def test_divide1(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(4, 2), 0)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(8, 2), 0)

    

if __name__ == '__main__':
    unittest.main()