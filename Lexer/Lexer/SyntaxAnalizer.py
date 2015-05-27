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
        return self.expression_tree_build()
    
    def next_token(self):
        try:
            self.current_token = self.lexer.token()
            if self.current_token is None:
                self.current_token = Token(None,None,None)
        except LexExeption as e:
            print(e)
    
    def match_grammar(self, type):
        if self.current_token.type == type:
            val = self.current_token.val
            self.next_token()
            return val
    
    def expression_tree_build(self):
        if self.current_token.type is None:
            return ''
        else:
            return self.match_expession()

    def match_expession(self):
        lval = self.match_term()

        if self.current_token.type == 'plus':
            self.match_grammar('plus')
            op = lambda a, b : a + b
        elif self.current_token.type == 'minus':
            self.match_grammar('minus')
            op = lambda a, b: a - b
        else:
            print ('returning lval = {0} '.format(lval))
            return lval
         
        rval = self.match_expession()
        print ('lval = {0}, rval = {1}, res = {2}'.format( lval, rval, op(lval, rval)))
        return op(lval, rval)   
    
    def match_term(self):
        lval = self.match_factor()
        if self.current_token.type == 'multi':
            self.match_grammar('multi')
            op = lambda a, b: a * b
        elif self.current_token.type == 'div':
            self.match_grammar('div')
            op = lambda a, b: a / b
        else:
            return lval
        
        rval = self.match_term()
        return op(lval, rval)

    def match_factor(self):
        if self.current_token.type == 'lp':
            self.match_grammar('lp')
            val = self.match_expession()
            self.match_grammar('rp')
            return val
        elif self.current_token.type == 'number':
            return int(self.match_grammar('number'))
 
def main(file, tok):
    parser = SyntaxAnalizer(tok)
    parser.parse(file)

if __name__ == '__main__':
    tokens = [
    (r'\+',                         'plus'),
    (r'\-',                         'minus'),
    (r'\*',                         'multi'),
    (r'\/',                         'div'),
    (r'\(',                         'lp'),
    (r'\)',                         'rp'),
    (r'^\d+([.]|)',           'number')]

    
    file_path = "file.txt"
    main(file_path, tokens)
