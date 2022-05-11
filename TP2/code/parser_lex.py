
from ast import Return
import ply.lex as lex

tokens = ["LEXMARKER","LITERALS", "EQUAL","CHARACTERS","HASHTAGS", "WORD", "IGNORE", "TOKENS", "SLEFTBRACKET", "SRIGHTBRACKET", "COMMA", "SQM", "UPPERWORD",
 "RE","LEFTBRACKET", "RIGHTBRACKET", "EXPRESSION","STRING", "SPACE","NEWLINE", "DOUBLENEWLINE"]


states = [
    ("spacesReader", "inclusive"), #read spaces in this state
]


#function Reader


#spacesReader

t_spacesReader_ignore = "ª"

def t_spacesReader_CHARACTERS(t):
    r'"[^"]+"'
    print("de volta")
    t.lexer.begin("INITIAL")
    t.lexer.activateSpaces = False
    return(t)


def t_spacesReader_SPACE(t):
    r'\s'
    return(t)

#INITIAL

t_ignore = " \t"

def t_NEWLINE(t):
    r'\n'
    return(t)

def t_DOUBLENEWLINE(t):
    r'\n\n'
    return(t)

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
    lexer.activateSpaces = True
    return(t)
    
def t_EQUAL(t):
    r'='
    if(t.lexer.activateSpaces == True): 
        lexer.begin('spacesReader')
        print('comecei')
    return(t)

def t_CHARACTERS(t):
    r'"[^"]+"'
    return(t)

def t_HASHTAGS(t):
    r'\#\#'
    return(t)

def t_UPPERWORD(t):
    r'[A-Z]+'
    return(t)
     
def t_WORD(t):
    r'[a-zA-Z.]+'
    return(t)
    
def t_IGNORE(t):
    r'\%ignore'
    lexer.activateSpaces = True
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
    




    
def t_ERROR(t):
    r'error'
    return(t)




def t_error(t):
    print(f"Illegal character {t} lexer")
    t.lexer.skip(1)
    return(t)


lexer = lex.lex()
lexer.activateSpaces = False