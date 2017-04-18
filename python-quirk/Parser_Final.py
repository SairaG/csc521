import sys
import pprint

pp = pprint.PrettyPrinter(indent=1, depth=10)

tokens = ["VAR", "IDENT:X", "ASSIGN", "NUMBER:4"]
tokens = ["SUB", "IDENT:X", "ADD", "NUMBER:4"]
tokens = ["SUB", "IDENT:X", "EXP", "NUMBER:4", "EOF"]
tokens = ["SUB", "IDENT:X", "EXP", "NUMBER:4", "EXP", "IDENT:X", "EOF"]
tokens = ["NUMBER:9", "DIV", "IDENT:X", "EXP",
          "NUMBER:4", "EXP", "IDENT:X", "EOF"]
tokens = ["NUMBER:9", "ADD", "IDENT:X", "SUB", "NUMBER:4", "EOF"]
tokens = ["NUMBER:9", "ADD", "LPAREN", "IDENT:X",
          "SUB", "NUMBER:4", "RPAREN", "EOF"]
tokens = ["LPAREN", "IDENT:X", "SUB", "NUMBER:4", "RPAREN", "EOF"]
tokens = ["IDENT:FOO", "LPAREN", "RPAREN", "EOF"]
tokens = ["IDENT:FOO", "LPAREN", "RPAREN", "COLON", "NUMBER:0", "EOF"]
tokens = ["SUB", "IDENT:X", "EOF"]

#begin utilities
def is_ident(tok):
    '''Determines if the token is of type IDENT.
    tok - a token
    returns True if IDENT is in the token or False if not.
    '''
    return -1 < tok.find("IDENT")

def is_number(tok):
    '''Determines if the token is of type NUMBER.
    tok - a token
    returns True if NUMBER is in the token or False if not.
    '''
    return -1 < tok.find("NUMBER")
#end utilities

def Expression(token_index):
    if len(self.tokens)-1-token_index>=2:
			if self.tokens[token_index+1] == "ADD":
				self.nest_another(['Expression0',[[], 'ADD', []]], placement)
			if self.tokens[token_index+1] == "SUB":
				self.nest_another(['Expression1',[[], 'SUB', []]], placement)
			self.Term(token_index,0)
			self.Expression(token_index+2,-1)
		else:
			self.nest_another(['Expression2', []], placement)



def Term(token_index):
    print self.tokens[token_index]
		if len(self.tokens)-1-token_index>=2:
			if self.tokens[token_index+1] == "MULT":
				self.nest_another(['Term0',[[], 'MULT', []]], placement)
			if self.tokens[token_index+1] == "DIV":
				self.nest_another(['Term1',[[], 'DIV', []]], placement)
			self.Factor(token_index,0)
			self.Term(token_index+2,-1)
		else:
			self.nest_another(['Term2',[]], placement)
			self.Factor(token_index)
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        subtree = ["Term0", returned_subtree]
        if "MULT" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Term(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    # <Factor> DIV <Term>
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        subtree = ["Term1", returned_subtree]
        if "DIV" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Term(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    # <Factor>
    (success, returned_index, returned_subtree) = Factor(token_index)
    if success:
        return [True, returned_index, ["Term2", returned_subtree]]
    return [False, token_index, []]


def Factor(token_index):
    if len(self.tokens)-1-token_index>=2:
			if self.tokens[token_index+1] == "EXP":
				if "LPAREN" in self.tokens[tokens]:
					self.nest_another(['Factor0',[[], 'EXP', []]], placement)
					self.SubExpression(token_index,0)
				else:
					self.nest_another(['Factor3',[[], 'EXP', []]], placement)
					self.Value(token_index,0)
			self.Factor(token_index+2,-1)

    (success, returned_index, returned_subtree) = SubExpression(token_index)
    if success:
        subtree = ["Factor0", returned_subtree]
        if "EXP" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]

    (success, returned_index, returned_subtree) = SubExpression(token_index)
    if success:
        subtree = ["Factor1", returned_subtree]
        return [True, returned_index, subtree]
    #<FunctionCall>
    (success, returned_index, returned_subtree) = FunctionCall(token_index)
    if success:
        return [True, returned_index, ["Factor2", returned_subtree]]
    #<Value> EXP <Factor>
    (success, returned_index, returned_subtree) = Value(token_index)
    if success:
        subtree = ["Factor3", returned_subtree]
        if "EXP" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = Factor(returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                return [True, returned_index, subtree]
    #<Value>
    (success, returned_index, returned_subtree) = Value(token_index)
    if success:
        return [True, returned_index, ["Factor4", returned_subtree]]
    return [False, token_index, []]


def FunctionCall(token_index):
    '''
    <FunctionCall> ->
        <Name> LPAREN <FunctionCallParams> COLON <Number>
        | <Name> LPAREN <FunctionCallParams>
    '''
    # <Name> LPAREN <FunctionCallParams> COLON <Number>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:

        subtree = ["FunctionCall0", returned_subtree]
        if "LPAREN" == tokens[returned_index]:
            subtree.append(tokens[returned_index])
            (success, returned_index, returned_subtree) = FunctionCallParams(
                returned_index + 1)
            if success:
                subtree.append(returned_subtree)
                if "COLON" == tokens[returned_index]:
                    subtree.append(tokens[returned_index])
                    (success, returned_index, returned_subtree) = Number(
                        returned_index + 1)
                    if success:
                        subtree.append(returned_subtree)
                        return [True, returned_index, subtree]

    # <Name> LPAREN <FunctionCallParams>
        (success, returned_index, returned_subtree) = Name(token_index)
        if success:
            subtree = ["FunctionCall1", returned_subtree]
            if "LPAREN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                (success, returned_index, returned_subtree) = FunctionCallParams(
                    returned_index + 1)
                if success:
                    subtree.append(returned_subtree)
                    return [True, returned_index, subtree]
    return [False, token_index, []]


def FunctionCallParams(token_index):
    '''
    <FunctionCallParams> ->
        <ParameterList> RPAREN
        | RPAREN
    '''
    #<ParameterList> RPAREN
    # todo after ParameterList is finished
    # RPAREN
    if "RPAREN" == tokens[token_index]:
        subtree = ["FunctionCallParams1", tokens[token_index]]
        return [True, token_index + 1, subtree]
    return [False, token_index, []]


def SubExpression(token_index):
    '''<SubExpression> ->
        LPAREN <Expression> RPAREN
    '''
    if "LPAREN" == tokens[token_index]:
        subtree = ["SubExpression0", tokens[token_index]]
        (success, returned_index, returned_subtree) = Expression(token_index + 1)
        if success:
            subtree.append(returned_subtree)
            if "RPAREN" == tokens[returned_index]:
                subtree.append(tokens[returned_index])
                return [True, returned_index + 1, subtree]
    return [False, token_index, []]


def Value(token_index):
    if "NUMBER" in "".join(self.tokens[token_index]):
			self.nest_another(['Value0',[]], placement)
			self.Number(token_index)
		if "NAME" in "".join(self.tokens[token_index]):
			self.nest_another(['Value1',[]], placement)
			self.Name(token_index)
		else:
			return self.setter(token_index)

    #<name>
    (success, returned_index, returned_subtree) = Name(token_index)
    if success:
        return [True, returned_index, ["Value0", returned_subtree]]
    #<number>
    (success, returned_index, returned_subtree) = Number(token_index)
    if success:
        return [True, returned_index, ["Value1", returned_subtree]]
    return [False, token_index, []]


def Name(token_index):
    '''<Name> ->
        IDENT
        | SUB IDENT
        | ADD IDENT
    '''
    subtree = []
    if is_ident(tokens[token_index]):
        subtree = ["Name0", tokens[token_index]]
        return [True, token_index + 1, subtree]
    if "SUB" == tokens[token_index]:
        if is_ident(tokens[token_index + 1]):
            subtree = ["Name1", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    if "ADD" == tokens[token_index]:
        if is_ident(tokens[token_index + 1]):
            subtree = ["Name2", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    return [False, token_index, subtree]


def Number(token_index):
    if "SUB" in self.tokens[token_index]:
			self.nest_another(['Number1, SUB, {}'.format(self.tokens[token_index])],1)
		if "ADD" in self.tokens[token_index]:
			self.nest_another(['Number2, ADD, {}'.format(self.tokens[token_index])],1)
		else:
			self.nest_another(['Number0, {}'.format(self.tokens[token_index])],1)

    subtree = []
    if is_number(tokens[token_index]):
        subtree = ["Number0", tokens[token_index]]
        return [True, token_index + 1, subtree]
    if "SUB" == tokens[token_index]:
        if is_number(tokens[token_index + 1]):
            subtree = ["Number1", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    if "ADD" == tokens[token_index]:
        if is_number(tokens[token_index + 1]):
            subtree = ["Number2", tokens[token_index], tokens[token_index + 1]]
            return [True, token_index + 2, subtree]
    return [False, token_index, subtree]

if __name__ == '__main__':
    print("starting __main__")
    pp.pprint(Program(0)[2])
