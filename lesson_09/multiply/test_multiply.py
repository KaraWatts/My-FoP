import unittest, math
from multiply import multiply_3_numbers

class TestMultiplyFunction(unittest.TestCase):

    def  test_multiply_integers(self):
        result = multiply_3_numbers(2,3,4)
        self.assertEqual(result, 24)

    def test_multiply_floats(self):
        result = multiply_3_numbers(math.pi, 2, 4.987)
        self.assertEqual(result, 31.334245126904598)

    def  test_negative_integers(self):
        result = multiply_3_numbers(-2,-3,-4)
        self.assertEqual(result, -24)
    
    def  test_negative_floats(self):
        result = multiply_3_numbers(math.pi, -2, -4.987)
        self.assertEqual(result, 31.334245126904598) 

    def test_multiply_integer_2(self):
        result = multiply_3_numbers(34, 78, 199)
        self.assertEqual(result, 527748)

if __name__ == '__main__':
    unittest.main()