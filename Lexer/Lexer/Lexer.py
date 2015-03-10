import re
import sys

class Token:
    def __init__(self, type, val, pos):
        self.val = val
        self.type = type
        self.pos = pos

    def __str__(self):
        return '%s [%s] at pos %s' %(self.val, self.type, self.pos)

class LexExeption(Exception):
    def __init__(self, sign,pos):
        self.pos = pos
        self.sign = sign
    def __str__(self):
        return 'Invalid sign %s at pos %s' % (self.sign , self.pos)    

class Lexer:
    def __init__(self, rules):
        self.rules = [];
        self.tokens = [];
        self.w_space = re.compile('\S')
        for regex, type in rules:
            self.rules.append((re.compile(regex), type))

    def input_insert(self, input):
        self.input = input
        self.pos = 0

    def token(self):
       if self.pos >= len(self.input):
          return None
       else:
           t_tmp = self.w_space.search(self.input[self.pos:])
           if t_tmp:
               self.pos += t_tmp.start()
           else:
               return None
           for t_regex, t_type in self.rules:
               t_tmp = t_regex.match(self.input[self.pos:])   
               if t_tmp:
                  val = self.input[self.pos + t_tmp.start():self.pos + t_tmp.end()]
                  tok = Token(t_type, val, self.pos)
                  self.pos += t_tmp.end()
                  return tok
           raise LexExeption(self.input[self.pos], self.pos)

    def tokenize(self):
        while True:
            tok = self.token()
            if tok is None: break
            yield tok
               
def main(tokens):
    lex = Lexer(tokens)
    lex.input_insert('(2.45^4 + 3) + 3x * 3')
    
    try:
        for tok in lex.tokenize():
            print(tok)
    except LexExeption as err:
        print(err)

if __name__ == '__main__':
    tokens = [    
    (r'[0-9][a-z]' ,          'identifier'),
    (r'\+',                   'plus'),
    (r'\-',                   'minus'),
    (r'\*',                   'multi'),
    (r'\/',                   'div'),
    (r'\^',                   'pow'),
    (r'\(',                   'lp'),
    (r'\)',                   'rp'),   
    (r'[-+]?(\d*[.])?\d+',    'number'),
    ]
    main(tokens)
    