from Lexer import Lexer, LexExeption, Token

class SyntaxExeption(Exception):
    pass

class SyntaxAnalizer:
    def __init__(self, lex_tokens):
        self.lexer = Lexer(lex_tokens)
        self.expession_tree = {}
        self.current_token = None
    
    def parse (self, file_path):
        file_content = None;
        with open(file_path, 'r') as file:
            file_content = file.read()
        file.close()
        self.lexer.input_insert(file_content)
        self.next_token()
        return self.W()
    
    def next_token(self):
        try:
            self.current_token = self.lexer.token()
            if self.current_token is None:
                self.current_token = Token(None,None,None)
        except LexExeption as e:
            print(e)
    
    def match_grammar_token(self, type):
        try:
            if self.current_token.type == type:
                val = self.current_token.val
                print('value {0} type {1}'.format(self.current_token.val, self.current_token.type))
                self.next_token()
                return val
            else:
                raise ValueError("current token {0} expected {1}".format(self.current_token.type, type))
        except ValueError as e:
            print(e)
    #   W ->  S X
    def W(self):
        self.S()
        self.X()
 
    #   X -> + S X
    #   X -> - S X
    #   X -> eps
    def X(self):
        if self.current_token.type == 'plus' or self.current_token.type == 'minus':
            self.match_grammar_token(self.current_token.type)
            self.S()
            self.X()

    #   S -> C Y
    def S(self):
        self.C()
        self.Y()
    #   Y -> * C Y
    #   Y -> / C Y
    #   Y -> eps
    def Y(self):
       if self.current_token.type == 'multi' or self.current_token.type == 'div':
           self.match_grammar_token(self.current_token.type)
           self.C()
           self.Y()
    #   C -> liczba
    #   C -> identyfikator
    #   C -> ( W )
    def C(self):
        if self.current_token.type == 'number' or self.current_token.type == 'identifier':
            self.match_grammar_token(self.current_token.type)
        elif self.current_token.type == 'lp':
            self.match_grammar_token('lp')
            self.W()
            self.match_grammar_token('rp')

    
def main(file, tok):
    parser = SyntaxAnalizer(tok)
    parser.parse(file)

if __name__ == '__main__':
    tokens = [
    (r'^[^\d\W]\w*',  'identifier'),
    (r'\+',           'plus'),
    (r'\-',           'minus'),
    (r'\*',           'multi'),
    (r'\/',           'div'),
    (r'\(',           'lp'),
    (r'\)',           'rp'),
    (r'^\d+([.]|)',   'number')
    ]

    
    file_path = "file.txt"
    main(file_path, tokens)
