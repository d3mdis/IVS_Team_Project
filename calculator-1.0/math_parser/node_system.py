from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f'{self.value}'


@dataclass
class AddNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} + {self.right})'


@dataclass
class SubtractNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} - {self.right})'


@dataclass
class MultiplyNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} * {self.right})'


@dataclass
class DivideNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} / {self.right})'


@dataclass
class PowerNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} ^ {self.right})'


@dataclass
class RootNode:
    left: object
    right: object

    def __repr__(self):
        return f'({self.left} √ {self.right})'


@dataclass
class FactorialNode:
    value: object

    def __repr__(self):
        return f'({self.value}!)'

