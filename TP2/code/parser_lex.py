
import ply.lex as lex

tokens = ["LEXMARKER","LITERALS", "EQUAL","CHARACTERS","HASHTAGS", "WORD", 
        "IGNORE", "TOKENS", "SLEFTBRACKET", "RIGHT","LEFT", "SRIGHTBRACKET", "COMMA", 
        "SQM", "UPPERWORD", "RE","LEFTBRACKET", "RIGHTBRACKET", "EXPRESSION","STRING", 
        "SPACE","YACCMARKER", "INITYACC", "PRECEDENCE", "NAMEVAR", "INITVAR", "NAMEPROD", 
        "COLON", "LEFTCOTTER", "EXPGRAM", "RETURNEDPRODS", "RIGHTCOTTER", "DEF", "NAMEFUNC", 
        "PARSEYACC"]


#INITIAL

t_ignore = " \t\n"

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
    return(t)

def t_CHARACTERS(t):
    r'"[^"]+"'
    return(t)

# def t_ONLYCHARACTERS(t):
#     r'\'[^\']+\''
#     return(t)    

def t_HASHTAGS(t):
    r'\#\#'
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
    r'[a-zA-Z.]+'
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
    

def t_ERROR(t):
    r'error'
    return(t)

# yacc 
def t_YACCMARKER(t):
    r'\%\%YACC'
    return(t)

def t_INITYACC(t):
    r'y=yacc()'
    return t

def t_PRECEDENCE(t):
    r'\%precedence'
    return(t)



def t_error(t):
    print(f"Illegal character {t} lexer")
    t.lexer.skip(1)
    return(t)


lexer = lex.lex()
