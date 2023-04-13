from abc import ABC, abstractmethod


class MathInterface(ABC):
    """
    Abstract interface containing prototype functions that the calculator will use.
    Its purpose is to simplify testing by decoupling the library from its GUI

    Usage for mathlib: just inherit this and override the functions :clueless:
    """
    @abstractmethod
    def add(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def subtract(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def multiply(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def divide(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def factorial(self, x: int) -> int:
        pass

    @abstractmethod
    def power(self, x: float, n: float) -> float:
        pass

    @abstractmethod
    def root(self, x: float, n: float) -> float:
        pass

    @abstractmethod
    def reciprocal_func(self, x: float) -> float:
        pass
