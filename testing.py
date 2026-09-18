def add(x,y):
    return x + y

def subtracts(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

import unittest

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
    
    def test_subtracts(self):
        self.assertEqual(subtracts(2, 1), 1)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(4, 0)

if __name__ == '__main__':
    unittest.main()