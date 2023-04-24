from math_interface import MathInterface


class MathLib(MathInterface):
    def add(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        return x+y

    def subtract(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        return x-y

    def multiply(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        if x*y == float('inf'):
            raise OverflowError
        return x*y

    def divide(self, x: float, y: float) -> float:
        if (x > float(1e+308)) or (y > float(1e+308)):
            raise OverflowError
        if y == 0:
            raise ZeroDivisionError
        return round(x/y, 5)

    def power(self, x: float, n: float) -> float:
        if (x > float(1e+308)) or (n > float(1e+308)):
            raise OverflowError
        if (x <= 0 and isinstance(n, int)) or (x >= 0):
            return x**n
        raise ValueError

    def root(self, x: float, n: float) -> float:
        if (x > float(1e+308)) or (n > float(1e+308)):
            raise OverflowError
        if x < 0:
            raise ValueError
        if n == 0:
            raise ValueError
        return round(x**(1/n), 5)

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

    def reciprocal_func(self, x: float) -> float:
        if x > float(1e+308):
            raise OverflowError
        if x == 0:
            raise ValueError
        return 1/x
