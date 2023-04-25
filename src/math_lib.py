from math_interface import MathInterface

## @file math_lib.py
## @author Denis Ragan (xragan82)
## @brief Math Library


## @brief Math library
## that can perform these operations:
## - Addition
## - Subtraction
## - Multiplication
## - Division
## - Exponentation
## - Find nth root
## - Factorial
## - Find reprocical function
class MathLib(MathInterface):

    ## @brief Addition
    ## @throws OverflowError if one of input numbers is bigger that 1e+308
    ## @param a
    ## @param b
    ## @returns a+b
    def add(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        return x+y

    ## @brief Subtraction
    ## @throws OverflowError if one of input numbers in bigger than 1e+308
    ## @param a
    ## @param b
    ## @returns a-b
    def subtract(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        return x-y

    ## @brief Multiplication
    ## @throws OverflowError if parameters are bigger that 1e+308
    ## @throws OverflowError If the final value is bigger than 1e+308
    ## @param a
    ## @param b
    ## @returns a*b
    def multiply(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        if x*y == float('inf'):
            raise OverflowError
        return x*y

    ## @brief Division
    ## @throws OverflowError if parameters are bigger that 1e+308
    ## @throws ZeroDivisionError if second parameter is 0
    ## @param a
    ## @param b
    ## @returns a/b
    def divide(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        if y == 0:
            raise ZeroDivisionError
        return round(x/y, 5)

    ## @brief Exponentation
    ## is designed that it only works on base of natural number.
    ## like this:
    ## x^n
    ## x - natural number
    ## n - any rational number
    ## @throws OverflowError if parameters are bigger that 1e+308
    ## @throws ValueError if x is not natural number number
    ## @param a
    ## @param b
    ## @returns a^b
    def power(self, x: float, n: float) -> float:
        if (x > float(1e+308)) or (n > float(1e+308)):
            raise OverflowError
        if (x <= 0 and isinstance(n, int)) or (x >= 0):
            return x**n
        raise ValueError

    ## @brief Find nth root
    ## Thanks to the rules of mathematics we know that
    ## we cant have negative value under even root
    ## @throws OverflowError if parameters are bigger that 1e+308
    ## @throws ValueError when trying to find nth root of negative number when n is even
    ## @throws ValueError when trying to find nth root of zero
    ## @param x
    ## @param n
    ## @returns  nth root of x
    def root(self, x: float, n: float) -> float:
        if (x > float(1e+308)) or (n > float(1e+308)):
            raise OverflowError
        if x < 0:
            raise ValueError
        if n == 0:
            raise ValueError
        return round(x**(1/n), 5)

    ## @brief Find factorial of int
    ## @throws OverflowError if parameter is bigger that 1e+308
    ## @throws OverflowError if factorial of paramter is bigger 1e+308
    ## @throws ValueError if parameter is negative
    ## @param a is a natural number
    ## @returns !a - factorial of a
    def factorial(self, x: int) -> int:
        try:
            if x > float(1e+308):
                raise OverflowError
            if x < 0:
                raise ValueError
            elif x == 0:
                return 1
            elif x == 1:
                return 1
            return x * self.factorial(x-1)
        except RecursionError as re:
            raise OverflowError

    ## @brief Find reprocical function
    ## @throws OverflowError if parameter is bigger that 1e+308
    ## @throws ValueError if parameter is zero
    ## @param x is any rational number except 0
    ## @returns 1/x - a reprocical function of x
    def reciprocal_func(self, x: float) -> float:
        if x > float(1e+308):
            raise OverflowError
        if x == 0:
            raise ValueError
        return 1/x
