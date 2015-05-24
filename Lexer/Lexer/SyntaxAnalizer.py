from Lexer import Lexer, LexExeption, Token

class SyntaxExeption(Exception):
    pass

class SyntaxAnalizer:
    def __init__(self):
        self.current_token = None
    


def main(file_path):
    pass

if __name__ == '__main__':
    tokens = [
    (r'^[^\d\W]\w*',                'identifier'),
    (r'\+',                         'plus'),
    (r'\-',                         'minus'),
    (r'\*',                         'multi'),
    (r'\/',                         'div'),
    (r'\^',                         'pow'),
    (r'\(',                         'lp'),
    (r'\)',                         'rp'),
    (r'^\d+([.]|\d+)\d+',           'number')
    ]
    file_path = "file.txt"
    main(file_path)
