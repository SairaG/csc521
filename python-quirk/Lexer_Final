import re


class Lexer_Final:

	token_syntax = {
	            'var': 'VAR',
	            'function':'FUNCTION',
	            'return': 'RETURN',
	            'print': 'PRINT',
	            '+': 'ADD',
	            '=': 'ASSIGN',
	            '-': 'SUB',
	            '*': 'MULT',
	            '/': 'DIV',
	            '^': 'EXP',
	            '(': 'LPAREN',
	            ')': 'RPAREN',
	            '{': 'LBRACE',
	            '}': 'RBRACE',
	            ',': 'COMMA',
	            ':': 'COLON',
         }


	def __init__(self, code):
		self.input = code
		self.raw_tokens = self.split_code()
		self.token_syntax, self.pair = self.tokenize(self.raw_tokens)

	def split_code(self):
		input_code = self.input
		chars = "+=-*/^(){},:"
		for c in chars:
			if c in input_code:
				input_code = input_code.replace(c, " {} ".format(c))
		input_code = re.sub(' +',' ',input_code)
		input_code = input_code.strip().split(" ")
		return input_code

	def tokenize(self, split_code):
		code_tokened = []
		token_lexeme_pair = []

		for character in split_code:
			if character.lstrip('-').replace('.','',1).isdigit():
				code_tokened.append("NUMBER:{}".format(character))
				token_lexeme_pair.append("NUMBER:{}".format(character))
			elif (bool(re.match("(^([^-_].*[^-_])?$)|(^[a-zA-Z]$)", character))
				and character not in self.token_syntax):
				code_tokened.append("IDENT:{}".format(character))
				token_lexeme_pair.append("IDENT:{}".format(character))
			elif character in self.token_syntax:
				code_tokened.append(self.token_syntax[character])
				token_lexeme_pair.append("{}:{}".format(self.token_syntax[character], character))
			else:
				raise ValueError("Syntax Error")

		return code_tokened, token_lexeme_pair


	def __repr__(self):
			return " ".join(self.token_syntax)


test = lexer(code)
print test.raw_tokens
