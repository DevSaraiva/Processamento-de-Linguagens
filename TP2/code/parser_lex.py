# frase -> lex yacc

# lex -> LEXMARKER literals ignore tokens functions

# literals -> LITERALS EQUAL CHARACTERS comment
#            | empty

# comment -> HASHTAGS words

# words -> words WORD
#           | WORD

# ignore -> IGNORE EQUAL CHARACTERS  comment
#         | empty

# tokens -> TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment

# tokenNames -> tokenNames COMMA SQM UPPERWORD SQM
#             | SQM UPPERWORD SQM

# functions -> functions function
#             | function

# function -> RE RETURN LEFTBRACKET SQM UPPERWORD COMMA TVALUE SQM RIGHTBRACKET comment 
#           | RE RETURN LEFTBRACKET SQM UPPERWORD COMMA WORD LEFTBRACKET TVALUE RIGHTBRACKET SQM RIGHTBRACKET comment 
#           | RE ERROR LEFTBRACKET STRING COMMA EXPRESSION RIGHTBRACKET comment

import ply.lex as lex

tokens = ["LEXMARKER","LITERALS", "EQUAL", "QM","CHARACTERS","HASHTAGS", "WORD", "IGNORE", "TOKENS", "SLEFTBRACKET", "SRIGHTBRACKET", "COMMA", "SQM", "UPPERWORD",
 "RE","RETURN", "LEFTBRACKET", "RIGHTBRACKET", "EXPRESSION","ERROR","TVALUE"]

def t_LEXMARKER(t):
    r'%% LEX'
    
def t_LITERALS(t):
    r'%literals'
    
def t_EQUAL(t):
    r'='

def t_QM(t):
    r'"'
    
def t_CHARACTERS(t):
    r'".+"'

def t_HASHTAGS(t):
    r'##'

def t_WORD(t):
    r'\w'
    
def t_IGNORE(t):
    r'%ignore'


def t_TOKENS(t):
    r'%tokens'

def t_SLEFTBRACKET(t):
    r'['
    
def t_SRIGHTBRACKET(t):
    r']'
    
def t_COMMA(t):
    r','
    
def t_SQM(t):
    r'\''
    
def t_UPPERWORD(t):
    r'[A-Z]+'
     

def t_RETURN(t):
    r'return'
    
def t_LEFTBRACKET(t):
    r'('
    
def t_RIGHTBRACKET(t):
    r')'
    
def t_TVALUE(t):
    r't.value'

def t_STRING(t):
    r'f".+"|".+"'

def t_EXPRESSION(t):
    r'(?:[a-zA-Z.]+\([a-zA-Z.0-9]*(?R)*[a-zA-Z.0-9]*\)\))|[a-zA-Z.]+\)'
    
def t_ERROR(t):
    r'error'



def t_error(t):
    print(f"Illegal character '{t.value[0]}' , [{t.lexer.lineno}]")
    t.lexer.skip(1)