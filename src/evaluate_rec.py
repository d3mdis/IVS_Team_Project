from math_parser.node_system import *
from math_interface import MathInterface
from math_parser.expression_lexer import Lexer
from math_parser.parser import Parser


class Evaluate:
    def __init__(self, expression, math_interface: MathInterface):
        self.m = math_interface
        translated_expression = Lexer(expression).tokenize()
        self.tree = Parser(translated_expression).parse()

    def evaluate(self):
        if self.tree is None:
            return None
        return self.visit(self.tree)

    def visit(self, node):
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, AddNode):
            return self.m.add(self.visit(node.left), self.visit(node.right))
        elif isinstance(node, SubtractNode):
            return self.m.subtract(self.visit(node.left), self.visit(node.right))
        elif isinstance(node, MultiplyNode):
            return self.m.multiply(self.visit(node.left), self.visit(node.right))
        elif isinstance(node, DivideNode):
            return self.m.divide(self.visit(node.left), self.visit(node.right))
        elif isinstance(node, PowerNode):
            return self.m.power(self.visit(node.left), self.visit(node.right))
        elif isinstance(node, RootNode):
            return self.m.root(self.visit(node.right), self.visit(node.left))
        elif isinstance(node, FactorialNode):
            return self.m.factorial(self.visit(node.value))
