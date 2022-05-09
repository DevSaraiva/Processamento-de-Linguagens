
from ast import Return
import ply.lex as lex

tokens = ["LEXMARKER","LITERALS", "EQUAL","CHARACTERS","HASHTAGS", "WORD", "IGNORE", "TOKENS", "SLEFTBRACKET", "SRIGHTBRACKET", "COMMA", "SQM", "UPPERWORD",
 "RE","RETURN", "LEFTBRACKET", "RIGHTBRACKET", "EXPRESSION","ERROR","TVALUE","STRING"]


t_ignore = " \t\n"

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
    r'".+"'
    return(t)

def t_HASHTAGS(t):
    r'\#\#'
    return(t)

def t_WORD(t):
    r'\w'
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
    
def t_UPPERWORD(t):
    r'[A-Z]+'
    return(t)
     

def t_RETURN(t):
    r'return'
    return(t)
    
def t_LEFTBRACKET(t):
    r'\('
    return(t)
    
def t_RIGHTBRACKET(t):
    r'\)'
    return(t)
    
def t_TVALUE(t):
    r't.value'
    return(t)

def t_STRING(t):
    r'f".+"|".+"'
    return(t)

def t_EXPRESSION(t):
    r'(?:[a-zA-Z.]+\([a-zA-Z.0-9]*\))|[a-zA-Z.]+'
    return(t)
    
def t_ERROR(t):
    r'error'
    return(t)



def t_error(t):
    print(f"Illegal character ")
    t.lexer.skip(1)


lexer = lex.lex()