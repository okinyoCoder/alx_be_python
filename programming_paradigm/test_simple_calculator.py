import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(7,-8), -1)
        self.assertEqual(self.calc.add(0,4), 4)

    def test_subtract(self):
        self.assertEqual(self.calc.substract(8,-4), 5)
        self.assertEqual(self.calc.substract(5,0), 5)
        self.assertEqual(self.calc.substract(-4,2), -6)
        self.assertEqual(self.calc.substract(-4,-1), 5) 

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-4,-1), 4)
        self.assertEqual(self.calc.multiply(-3,2), 6)
        self.assertEqual(self.calc.multiply(-4,0), 0)
        self.assertEqual(self.calc.multiply(9,-4), 36)

    def test_divide(self):
        self.assertEqual(self.calc.multiply(-4,1), -4)
        self.assertEqual(self.calc.multiply(3,0), 0)
        self.assertEqual(self.calc.multiply(21,1), 7)
        self.assertEqual(self.calc.multiply(9,3), 3)