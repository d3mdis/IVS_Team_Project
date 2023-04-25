from .tokenizer import TokenType
from .node_system import *


class TokenException(Exception):
    def __init__(self, message="Syntax error"):
        super(TokenException, self).__init__(message)

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None
        result = self.expr()

        return result

    def expr(self):
        result = self.term()
        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.advance()
                result = AddNode(result, self.term())
            elif token.type == TokenType.MINUS:
                self.advance()
                result = SubtractNode(result, self.term())
        return result

    def term(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.factor())
            elif token.type == TokenType.DIVIDE:
                self.advance()
                result = DivideNode(result, self.factor())
        return result

    def factor(self):
        result = self.power()
        while self.current_token is not None and self.current_token.type == TokenType.ROOT:
            token = self.current_token
            if token.type == TokenType.ROOT:
                self.advance()
                result = RootNode(result, self.factor())
        return result

    def power(self):
        result = self.atom()
        while self.current_token is not None and self.current_token.type == TokenType.POWER:
            token = self.current_token
            if token.type == TokenType.POWER:
                self.advance()
                result = PowerNode(result, self.factor())
        return result

    def atom(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.LEFT_PAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type == TokenType.RIGHT_PAREN:
                self.advance()
                return result
            else:
                raise ValueError
        elif token.type == TokenType.FACTORIAL:
            self.advance()
            return FactorialNode(self.atom())
        elif token.type == TokenType.PLUS:
            self.advance()
            return MultiplyNode(NumberNode(-1), self.atom())
        elif token.type == TokenType.MINUS:
            self.advance()
            return MultiplyNode(NumberNode(-1), self.atom())
        else:
            raise ValueError

