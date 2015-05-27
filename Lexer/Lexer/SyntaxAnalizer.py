from Lexer import Lexer, LexExeption, Token

class SyntaxExeption(Exception):
    pass

class SyntaxAnalizer:
    def __init__(self, file_path, grammar):
        self.current_token = None
        self.tokens_tree = dict()
        self.file_path = file_path
        self.lexer = Lexer()
        self.grammar = grammar


    def build_syntax_tree(self):
        file_content = ''
        with open(self.file_path, 'r') as file:
            file_content = file.read()
        file.close()
        self.lexer.input_insert(file_content)
        token_generator = self.lexer.tokenize();

        
    
    def check_grammar_rules(self, token):
        pass
    def is_experssion(self, token);


def main(file_path):
    pass

if __name__ == '__main__':
    tokens = [#(r'^[^\d\W]\w*', 'identifier'),
    (r'\+',                         'plus'),
    (r'\-',                         'minus'),
    (r'\*',                         'multi'),
    (r'\/',                         'div'),
    (r'\^',                         'pow'),
    (r'\(',                         'lp'),
    (r'\)',                         'rp'),
    (r'^\d+([.]|\d+)\d+',           'number')]

    
    file_path = "file.txt"
    main(file_path)
