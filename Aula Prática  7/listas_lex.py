import ply.lex as lex
 
# [1,2,3,4,5]
# [1,2,3,start,2,3,end,5]

tokens =["DELIM_ABRIR","SEPARATOR","NUM","PAL","DELIM_FECHAR"]

t_DELIM_ABRIR = r'\['
t_SEPARATOR = r','
t_NUM = r'[0-9]+'
t_PAL = r'[a-zA-Z]+'
t_DELIM_FECHAR = r'\]'

t_ignore = ' \t\n'

def t_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()