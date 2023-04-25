import unittest
from math_lib import MathLib

## @brief Test suite for math_lib
## @file mathlib_suite.py
## @author David Dovala (xdoval01)


## @brief Tests for addition
## Use to test addition capability of MathLib().Add(a: float, b: float) method
class SumTest(unittest.TestCase):

    ## @brief Test basic functionality
    ## Used values: 156+1376=1532
    def test_basic(self):

        result_value: float = MathLib().add(156, 1376)
        expected_value: float = 1532
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative numbers
    ## Used values: -1897+45.78=-1851.22
    def test_negative(self):
        result_value: float = MathLib().add(-1897, 45.78)
        expected_value: float = -1851.22
        self.assertEqual(expected_value, result_value)

    ## @brief Test zero
    ## Used values: 0+0=0
    def test_zero(self):
        result_value: float = MathLib().add(0, 0)
        expected_value: float = 0
        self.assertEqual(expected_value, result_value)

    ## @brief Tests 64 byte input and output
    ## Used values: (9e+307)+(8.976e+307)=(1.7976e+308)
    def test_64byte(self):
        result_value: float = MathLib().add(9e+307, 8.976e+307)
        expected_value = 1.7976e+308
        self.assertEqual(expected_value, result_value)

    ## @brief Test error handling when overflowing arguments are passed to add method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().add(1e+309, -1e+308)

    ## @brief Test error handling when overflowing result is returned by add method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().add(1.79e+308, 1.79e+308)

    ## @brief If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().add("a", "b")


## @breif subtraction test
## Use to test subtraction capability of MathLib().Subtract(a: float, b: float) method
class SubtractionTest(unittest.TestCase):


    ## @breif Test basic functionality
    ## Used values: 156-1376=-1220
    def test_basic(self):
        result_value: float = MathLib().subtract(156, 1376)
        expected_value: float = -1220
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative numbers
    ## Used values: -1897-45.78=-1942.78
    def test_negative(self):
        result_value: float = MathLib().subtract(-1897, 45.78)
        expected_value: float = -1942.78
        self.assertEqual(expected_value, result_value)

    ## @brief Test zero
    ## Used values: 0-0=0
    def test_zero(self):
        result_value: float = MathLib().subtract(0, 0)
        expected_value: float = 0
        self.assertEqual(expected_value, result_value)

    ## @brief Tests 64 byte input and output
    ## Used values: (9e+307)-(8.976e+307)=1e+307
    def test_64byte(self):
        result_value: float = MathLib().subtract(9e+307, 8e+307)
        expected_value = 1e+307
        self.assertAlmostEqual(expected_value, result_value, delta=int(1e+300))

    ## @brief Test error handling when overflowing arguments are passed to subtract method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().subtract(1e+309, 1e+308)

    ## @breif Test error handling when overflowing result is returned by subtract method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().subtract(1.7e+308, -1.7e+308)

    ## @breif If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().subtract("a", "b")


## @brief Use to test multiplication capability of MathLib().Multiply(a: float, b: float) method
class MultiplyTest(unittest.TestCase):


    ## @brief Test basic functionality
    ## Used values: 156*1376=214656
    def test_basic(self):
        result_value: float = MathLib().multiply(156, 1376)
        expected_value: float = 214656
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative numbers
    ## Used values: -17 * -2.5 = 42.5
    def test_negative(self):
        result_value: float = MathLib().multiply(-17, -2.5)
        expected_value: float = 42.5
        self.assertEqual(expected_value, result_value)

    ## @breif Test zero
    ## Used values: 1e+308*0=0
    def test_zero(self):
        result_value: float = MathLib().multiply(1e+308, 0)
        expected_value: float = 0
        self.assertEqual(expected_value, result_value)

    ## @brief Test error handling when overflowing arguments are passed to multiply method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().multiply(1e+309, 0.5)

    ## @ brief Test error handling when overflowing result is returned by multiply method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().multiply(1e+308,1e+100)

    ## @brief If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().multiply("a", "b")

## @brief Use to test division capability of MathLib().Divide(a: float, b: float) method
class DivisionTest(unittest.TestCase):


    ## @breif Test basic functionality
    ## Used values: 814648.56/452.96=1798.5
    def test_basic(self):
        result_value: float = MathLib().divide(814648.56, 452.96)
        expected_value: float = 1798.5
        self.assertEqual(expected_value, result_value)

    ## @Test negative numbers. Expect flipped sign.
    ## Used values: -48/-12=4
    def test_negative(self):
        result_value: float = MathLib().divide(-48, -12)
        expected_value: float = 4
        self.assertEqual(expected_value, result_value)

    ## @breif Test zero. Expect error.
    ## Used values: 1e+300/0=undefined
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):
            MathLib().divide(1e+300, 0)

    ## @breif Test error handling when overflowing arguments are passed to divide method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().divide(1e+309, 1e+308)

    ## @brief Test error handling when overflowing result is returned by divide method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().divide(1e+309, 0.5)

    ## @brief If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().divide("a", "b")


## @breif Use to test factorial capability of MathLib().Factorial(a: float) method
class FactorialTest(unittest.TestCase):

    ## @brief Test basic functionality
    ## Used values: 5!=120
    def test_basic(self):
        result_value: float = MathLib().factorial(5)
        expected_value: float = 120
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative numbers. Expect error.
    ## Used values: -5!=undefined
    def test_negative(self):
        with self.assertRaises(ValueError):
            MathLib().factorial(-5)

    ## @Test zero. Expect 1.
    ## Used values: 0!=1
    def test_zero(self):
        result_value: float = MathLib().factorial(0)
        expected_value: float = 1
        self.assertEqual(expected_value, result_value)

 
    ## @breif Test error handling when overflowing arguments are passed to factorial method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().factorial(1e+309)

    ## @brief Test error handling when overflowing result is returned by factorial method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().factorial(1e+308)

    ## $breif string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().factorial("a")


## Use to test power capability of MathLib().Power(a: float, b: float) method
class PowerTest(unittest.TestCase):

    ## @brief Test basic functionality
    ## Used values: 5^2=25
    def test_basic(self):
        result_value: float = MathLib().power(5, 2)
        expected_value: float = 25
        self.assertEqual(expected_value, result_value)

    ## @breif Test negative numbers. Expect flipped sign.
    ## Used values: -5^-2=0.04
    def test_negative(self):
        result_value: float = MathLib().power(-5, -2)
        expected_value: float = 0.04
        self.assertEqual(expected_value, result_value)

    ## @breif Test zero. Expect 1.
    ## Used values: -312^0=1
    def test_zero(self):
        result_value: float = MathLib().power(-312, 0)
        expected_value: float = 1
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative square root. Expect error.
    ## Used values: -5^2.5=undefined
    def test_negativeSquareRoot(self):
        with self.assertRaises(ValueError):
            MathLib().power(-5, 0.5)


    ## @breif Test error handling when overflowing arguments are passed to power method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().power(1e+309, 1e+308)

    ## @breif Test error handling when overflowing result is returned by power method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().power(1e+309, 2)

    ## @breif If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().power("a", "b")


## @breif Use to test root capability of MathLib().Root(a: float, b: float) method
class RootTest(unittest.TestCase):

    ## @breif Test basic functionality
    ## Used values: sqrt(25)=5
    def test_basic(self):
        result_value: float = MathLib().root(25, 2)
        expected_value: float = 5
        self.assertEqual(expected_value, result_value)

    ## @brief Test negative root.
    ## Used values: -3rd root of 0.125 = 2
    def test_negative(self):
        result_value: float = MathLib().root(0.125, -3)
        expected_value: float = 2
        self.assertEqual(expected_value, result_value)

    ## @breif Test zero. Expect 0.
    ## Used values: 5^0=0
    def test_zero(self):
        result_value: float = MathLib().root(0, 5)
        expected_value: float = 0
        self.assertEqual(expected_value, result_value)

    ## @breif Test negative even root. Expect error.
    ## Used values: 6th root of -1756 = undefined
    def test_negativeEvenRoot(self):
        with self.assertRaises(ValueError):
            MathLib().root(-1756, 6)

    ## @breif Test error handling when overflowing arguments are passed to root method
    def test_inputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().root(1e+309, 2)

    ## @breif Test error handling when overflowing result is returned by root method
    def test_outputOverflow(self):
        with self.assertRaises(OverflowError):
            MathLib().root(1e+309, 2)

    ## @brief If string is passed to the tested method error should occur
    def test_invalidInput(self):
        with self.assertRaises(TypeError):
            MathLib().root("a", "b")


if __name__ == '__main__':

    unittest.main()