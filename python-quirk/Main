from Lexer import Lexer_Final
from Parser import Parser_Final

code = (""function x = (y+z) ^s {"+
  "return x"+
    "} var y = 1, var z = 4, var s = 2)")"

tokens = Lexer_Final(code)
parser = Parser_Final(tokens.tokens)
print tokens
print parser
