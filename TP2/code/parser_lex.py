
import ply.lex as lex

tokens = ["LEXMARKER","LITERALS", "EQUAL","CHARACTERS","HASHTAGS", "WORD","NEWLINE",
        "IGNORE", "TOKENS", "SLEFTBRACKET", "RIGHT","LEFT", "PRECTAG", "CHARS","SRIGHTBRACKET", "COMMA", 
        "SQM", "UPPERWORD","LITERAL","RE","LEFTBRACKET", "RIGHTBRACKET", "EXPRESSION","STRING", 
        "YACCMARKER", "INITYACC", "PRECEDENCE", "CHAR","NAMEVAR", "INITVAR", "NAMEPROD", 
        "COLON", "LEFTCOTTER", "EXPGRAM", "RETURNEDPRODS", "RIGHTCOTTER", "DEF", "NAMEFUNC", 
        "PARSEYACC","PERCENTAGE","FUNCTION","BODYFUNCTIONLINE","BODYFUNCTIONFINAL"]


states = [
    ("newlineReader", "inclusive"),
    ("pythonReader" , "exclusive"),
    ("functionReader","exclusive"),
]



#python reader

def t_pythonReader_CHARS(t):
    r'[^{}]+'
    return(t)


def t_pythonReader_RIGHTCOTTER(t):
    r'\}'
    t.lexer.begin('INITIAL')
    return(t)


t_pythonReader_ignore = " \t\n"

def t_pythonReader_error(t):
    r'error'
    return(t)

#NEWLINE READER

def t_newlineReader_NEWLINE(t):
    r'\n'
    t.lexer.begin('INITIAL')
    return(t)



t_newlineReader_ignore = " \t"


#function reader

def t_FUNCTION(t):
    r'def '
    t.lexer.begin('functionReader')
    return(t)

def t_functionReader_BODYFUNCTIONFINAL(t):
    r'.*\n\n'
    t.lexer.begin('INITIAL')
    return(t)

def t_functionReader_BODYFUNCTIONLINE(t):
    r'.*\n'
    return(t)

def t_functionReader_error(t):
    r'error'
    return(t)


t_functionReader_ignore = " \t"

#INITIAL

t_ignore = " \t\n"

def t_INITYACC(t):
    r'y=yacc\(\)'
    return t

def t_PARSEYACC(t):
    r'y.parse'
    return t

def t_STRING(t):
    r'f".*"'
    return(t)



def t_RE(t):
    r'(?:.* return)|.* error'
    return(t)


def t_EXPRESSION(t):
    r'(?:[a-zA-Z.]+\([a-zA-Z.0-9]*\))'
    return(t)

def t_LEXMARKER(t):
    r'\%\%LEX'
    return(t)
    
def t_LITERALS(t):
    r'\%literals'
    return(t)
    
def t_EQUAL(t):
    r'='
    return(t)

def t_CHARACTERS(t):
    r'"[^"]+"'
    return(t)

def t_HASHTAGS(t):
    r'\#\#'
    t.lexer.begin('newlineReader')
    return(t)

def t_UPPERWORD(t):
    r'[A-Z]+'
    return(t)

def t_RIGHT(t):
    r'right'
    return(t)

def t_LEFT(t):
    r'left'
    return(t)     

def t_WORD(t):
    r'[a-zA-Z.:]+'
    return(t)
    
def t_IGNORE(t):
    r'\%ignore'
    return(t)


def t_TOKENS(t):
    r'\%tokens'
    return(t)

def t_SLEFTBRACKET(t):
    r'\['
    return(t)
    
def t_SRIGHTBRACKET(t):
    r'\]'
    return(t)
    
def t_COMMA(t):
    r'\,'
    return(t)

def t_SQM(t):
    r'\''
    return(t)
      
def t_LEFTBRACKET(t):
    r'\('
    return(t)
    
def t_RIGHTBRACKET(t):
    r'\)'
    return(t)

def t_LEFTCOTTER(t):
    r'\{'
    t.lexer.begin('pythonReader')
    return(t)
        
def t_RIGHTCOTTER(t):
    r'\}'
    return(t)




def t_ERROR(t):
    r'error'
    return(t)

# yacc 
def t_YACCMARKER(t):
    r'\%\%YACC'
    return(t)


def t_PRECEDENCE(t):
    r'\%precedence'
    return(t)

def t_PRECTAG(t):
    r'%prec'
    return(t)


def t_PERCENTAGE(t):
    r'%%\n'
    # t.lexer.begin('functionsReader')
    return(t)

def t_CHAR(t):
    r'.'
    return(t)


def t_error(t):
    print(f"Illegal character {t} lexer")
    t.lexer.skip(1)
    return(t)


lexer = lex.lex()
