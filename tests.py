import unittest, calculator


class MyTestCase(unittest.TestCase):
    def test_exp(self):
        self.assertEqual(calculator.exponent(2,2), 4) # test case for exponent feature

    def test_divide(self):
        self.assertEqual(calculator.divide(2,2), 1) # test case for divide feature

    def test_multiply(self):
        self.assertEqual(calculator.multiply(7,8), 56) # test case for multiplication feature
        
if __name__ == '__main__':
    unittest.main()
