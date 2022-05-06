import ply.lex as lex


literals = {'+','-','/','*','=','(',')'}

t_ignore = " \t\n"

tokens = [ 'VAR','NUMBER'] 


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return('VAR',t.value)

def t_NUMEBR(t):
    r'\d+(\.\d+)?'
    return('NUMBER',t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' , [{t.lexer.lineno}]")
    t.lexer.skip(1)


lexer = lex.lex()
