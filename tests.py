import unittest, calculator


class MyTestCase(unittest.TestCase):
    def test_exp(self):
        self.assertEqual(calculator.exponent(2,2), 4); #test case for exponent feature


if __name__ == '__main__':
    unittest.main()
