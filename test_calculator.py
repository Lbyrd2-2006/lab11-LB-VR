# https://github.com/Lbyrd2-2006/lab11-LB-VR
# Partner 1: <YOUR-PARTNER-NAME-HERE>
# Partner 2: <YOUR-NAME-HERE>


import unittest
import math
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-3, 9), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,3),2)
        self.assertEqual(sub(10,3),7)
        self.assertEqual(sub(2,-2), 4)


    ######## Partner 1
     def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)


     def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 3.5), 2.0)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(1000,10),3)
        self.assertEqual(log(16,2),4)
        self.assertEqual(log(1,10),0)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10,1)

    
    ######## Partner 1
     def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(-10, 2)
        with self.assertRaises(ValueError):
            log(10, 1)
        with self.assertRaises(ValueError):
            log(0, 5)

     def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)


     def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()