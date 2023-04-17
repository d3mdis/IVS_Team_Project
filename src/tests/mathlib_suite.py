import unittest
from ..math_interface import MathInterface, IMathLib # <--- Q: sys.path.append('?')


class SumTest(unittest.TestCase):
    """
        Use to test addition capability of MathLibrary.Add(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 156+1376=1532
        """
        resultValue: float = self.mathLib.add(156, 1376)
        expectedValue: float = 1532
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers
            Used values: -1897+45.78=1220
        """
        resultValue: float = self.mathLib.add(-1897,45.78)
        expectedValue: float = 1851.22
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero
            Used values: 0+0=0
        """
        resultValue: float = self.mathLib.add(0, 0)
        expectedValue: float = 0
        self.assertEquals(expectedValue, resultValue)

    def test_64byte(self):
        """
            Tests 64 byte input and output
            Used values: (9e+307)+(8.976e+307)=(1.7976e+308)
        """
        resultValue: float = self.mathLib.add(9e+307, 8.976e+307)
        expectedValue = 1.7976e+308
        self.assertEqual(expectedValue, resultValue)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to add method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.add(1e+309, -1e+308)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by add method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.add(1.79e+308, 1.79e+308)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.add("a", "b")

class SubtractionTest(unittest.TestCase):
    """
        Use to test subtraction capability of MathLibrary.Subtract(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 156-1376=-1220
        """
        resultValue: float = self.mathLib.subtract(156, 1376)
        expectedValue: float = -1220
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers
            Used values: -1897-45.78=-1942.78
        """
        resultValue: float = self.mathLib.subtract(-1897, 45.78)
        expectedValue: float = -1942.78
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero
            Used values: 0-0=0
        """
        resultValue: float = self.mathLib.subtract(0, 0)
        expectedValue: float = 0
        self.assertEquals(expectedValue, resultValue)

    def test_64byte(self):
        """
            Tests 64 byte input and output
            Used values: (9e+307)-(8.976e+307)=2.4e+6
        """
        resultValue: float = self.mathLib.subtract(9e+307, 8.976e+307)
        expectedValue = 2.4e+6
        self.assertEqual(expectedValue, resultValue)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to subtract method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.subtract(1e+309, 1e+308)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by subtract method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.subtract(1.7e+308, -1.7e+308)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.subtract("a", "b")

class MultiplyTest(unittest.TestCase):

    """
        Use to test multiplication capability of MathLibrary.Multiply(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 156*1376=214656
        """
        resultValue: float = self.mathLib.multiply(156, 1376)
        expectedValue: float = 214656
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers
            Used values: -1897*-45.78=87050.86
        """
        resultValue: float = self.mathLib.multiply(-1897, -45.78)
        expectedValue: float = 87050.86
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero
            Used values: 1e+308*0=0
        """
        resultValue: float = self.mathLib.multiply(1e+308, 0)
        expectedValue: float = 0
        self.assertEquals(expectedValue, resultValue)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to multiply method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.multiply(1e+309, 0.5)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by multiply method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.multiply(1e+308,1e+100)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.multiply("a", "b")

class DivisionTest(unittest.TestCase):
    """
        Use to test division capability of MathLibrary.Divide(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 814648.56/452.96=1798.5
        """
        resultValue: float = self.mathLib.divide(814648.56, 452.96)
        expectedValue: float = 1798.5
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers. Expect flipped sign.
            Used values: 1897/-45.78=-41.286
        """
        resultValue: float = self.mathLib.divide(-1897, -45.78)
        expectedValue: float = 41.286
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero. Expect error.
            Used values: 1e+300/0=undefined
        """
        with self.assertRaises(ZeroDivisionError):
            self.mathLib.divide(1e+300, 0)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to divide method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.divide(1e+309, 1e+308)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by divide method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.divide(1e+309, 0.5)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.divide("a", "b")

class FactorialTest(unittest.TestCase):
    """
        Use to test factorial capability of MathLibrary.Factorial(a: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 5!=120
        """
        resultValue: float = self.mathLib.factorial(5)
        expectedValue: float = 120
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers. Expect error.
            Used values: -5!=undefined
        """
        with self.assertRaises(ValueError):
            self.mathLib.factorial(-5)

    def test_zero(self):
        """
            Test zero. Expect 1.
            Used values: 0!=1
        """
        resultValue: float = self.mathLib.factorial(0)
        expectedValue: float = 1
        self.assertEquals(expectedValue, resultValue)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to factorial method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.factorial(1e+309)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by factorial method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.factorial(1e+308)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.factorial("a")

class PowerTest(unittest.TestCase):
    """
        Use to test power capability of MathLibrary.Power(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: 5^2=25
        """
        resultValue: float = self.mathLib.power(5, 2)
        expectedValue: float = 25
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers. Expect flipped sign.
            Used values: -5^-2=0.04
        """
        resultValue: float = self.mathLib.power(-5, -2)
        expectedValue: float = 0.04
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero. Expect 1.
            Used values: -312^0=1
        """
        resultValue: float = self.mathLib.power(-312, 0)
        expectedValue: float = 1
        self.assertEquals(expectedValue, resultValue)

    def test_negativeSquareRoot(self):
        """
            Test negative square root. Expect error.
            Used values: -5^2.5=undefined
        """
        with self.assertRaises(ValueError):
            self.mathLib.power(-5, 0.5)


    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to power method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.power(1e+309, 1e+308)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by power method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.power(1e+309, 2)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.power("a", "b")

class RootTest(unittest.TestCase):
    """
        Use to test root capability of MathLibrary.Root(a: float, b: float) method
    """
    mathLib: IMathLib

    def test_basic(self):
        """
            Test basic functionality
            Used values: sqrt(25)=5
        """
        resultValue: float = self.mathLib.root(25, 2)
        expectedValue: float = 5
        self.assertEquals(expectedValue, resultValue)

    def test_negative(self):
        """
            Test negative numbers. Expect error.
            Used values: -3rd root of 0.25 = 2
        """
        resultValue: float = self.mathLib.root(0.25, -3)
        expectedValue: float = 2
        self.assertEquals(expectedValue, resultValue)

    def test_zero(self):
        """
            Test zero. Expect 0.
            Used values: 5^0=0
        """
        resultValue: float = self.mathLib.root(0, 5)
        expectedValue: float = 0
        self.assertEquals(expectedValue, resultValue)

    def test_negativeEvenRoot(self):
        """
            Test negative even root. Expect error.
            Used values: 6th root of -1756 = undefined
        """
        with self.assertRaises(ValueError):
            self.mathLib.root(-1756, 6)

    def test_inputOverflow(self):
        """
            Test error handling when overflowing arguments are passed to root method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.root(1e+309, 2)

    def test_outputOverflow(self):
        """
            Test error handling when overflowing result is returned by root method
        """
        with self.assertRaises(OverflowError):
            self.mathLib.root(1e+309, 2)

    def test_invalidInput(self):
        """
            If string is passed to the tested method error should occur
        """
        with self.assertRaises(TypeError):
            self.mathLib.root("a", "b")

if __name__ == '__main__':
    unittest.main()