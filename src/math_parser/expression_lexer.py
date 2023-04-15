from .tokenizer import Token, TokenType
DIGITS = '0123456789'


class Lexer:
    """
    Tokenizes mathematical expressions.
    usage in parser
    """
    def __init__(self, expression: str):
        if "!" in expression:
            self.expression = self.move_factorial(expression)
            self.expression = iter(self.expression)
            self.advance()
        else:
            self.expression = iter(expression)
            self.advance()

    def move_factorial(self, expression):
        for index, value in enumerate(expression):
            if value == "!":
                if expression[index-1] == ")":
                    for i in range(index-1, -1, -1):
                        if expression[i] == "(":
                            expression = expression[:i] + "!" + expression[i:]
                            expression = expression[:index+1] + expression[index+2:]
                            break
                else:
                    if index-1 == 0:
                        expression = "!" + expression
                        expression = expression[:index+1] + expression[index+2:]
                    else:
                        for i in range(index-1, 0, -1):
                            if expression[i] not in DIGITS:
                                expression = expression[:i+1] + "!" + expression[i+1:]
                                expression = expression[:index+1] + expression[index+2:]
                                break
        return expression


    def advance(self):
        try:
            self.current_char = next(self.expression)
        except StopIteration:
            self.current_char = None

    def tokenize(self):
        while self.current_char is not None:
            if self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                yield Token(TokenType.PLUS, '+')
                self.advance()
            elif self.current_char == '-':
                yield Token(TokenType.MINUS, '-')
                self.advance()
            elif self.current_char == '*':
                yield Token(TokenType.MULTIPLY, '*')
                self.advance()
            elif self.current_char == '/':
                yield Token(TokenType.DIVIDE, '/')
                self.advance()
            elif self.current_char == '^':
                yield Token(TokenType.POWER, '^')
                self.advance()
            elif self.current_char == '√':
                yield Token(TokenType.ROOT, '√')
                self.advance()
            elif self.current_char == '(':
                yield Token(TokenType.LEFT_PAREN, '(')
                self.advance()
            elif self.current_char == ')':
                yield Token(TokenType.RIGHT_PAREN, ')')
                self.advance()
            elif self.current_char == '!':
                yield Token(TokenType.FACTORIAL, '!')
                self.advance()

    def generate_number(self):
        decimal_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char in DIGITS or self.current_char == '.'):
            if self.current_char == '.':
                if decimal_count == 1:
                    break
                decimal_count += 1
            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str += '0'
        return Token(TokenType.NUMBER, float(number_str))
