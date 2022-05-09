# phrase -> lex yacc

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

# function -> RE RETURN LEFTBRACKET content RIGHTBRACKET comment 


# content -> SQM UPPERWORD SQM COMMA TVALUE
#          | SQM UPPERWORD SQM COMMA EXPRESSION
#          | STRING COMMA EXPRESSION

#returned -> TVALUE
#            | EXPRESSION


 

import ply.yacc as yacc
from parser_lex import tokens

def p_phrase(p):
    "frase : lex " #falta yacc
    print('ola')

def p_lex(p):
    "lex : LEXMARKER literals ignore tokens functions"

def p_literals(p):
    "literals : LITERALS EQUAL CHARACTERS comment"

def p_literals_empty(p):
    "literals : "

def p_comment(p):
    "comment : HASHTAGS words"

def p_words(p):
    "words : words WORD"

def p_words_stop(p):
    "words : WORD"

def p_ignore(p):
    "ignore : IGNORE EQUAL CHARACTERS comment"

def p_ignore_empty(p):
    "ignore : "

def p_tokens(p):
    "tokens : TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment"

def p_tokens_empty(p):
    "tokens : "

def p_tokenNames(p):
    "tokenNames : tokenNames COMMA SQM UPPERWORD SQM"

def p_tokenNames_stop(p):
    "tokenNames : SQM UPPERWORD SQM"

def p_functions(p):
    "functions : functions function"

def p_functions_stop(p):
    "functions : function"

def p_functions_empty(p):
    "functions : "

def p_function_tvalue(p):
    "function : RE RETURN LEFTBRACKET SQM UPPERWORD COMMA TVALUE SQM RIGHTBRACKET comment"

def p_function_word(p):
    "function : RE RETURN LEFTBRACKET SQM UPPERWORD COMMA WORD LEFTBRACKET TVALUE RIGHTBRACKET SQM RIGHTBRACKET comment"

def p_function_expression(p):
    "function : RE ERROR LEFTBRACKET STRING COMMA EXPRESSION RIGHTBRACKET comment"

def p_error(t):
    print(f"Illegal character '{t}'")
        


# Build the parser
parser = yacc.yacc()


input = '''
%%LEX

'''
#%%LEX
#%literals = "+-/*=()"
# %ignore = " \t\n"
# %tokens = [ ’VAR’,’NUMBER’ ]
# [a-zA-Z_][a-zA-Z0-9_]* return(’VAR’, t.value)    ## a single char
# \d+(\.\d+)? return(’NUMBER’, float(t.value)
# .   error(f"Illegal character ’{t.value[0]}’, [{t.lexer.lineno}]",
# t.lexer.skip(1) )


parser.parse(input)

# # Read line from input and parse it
# import sys
# for linha in sys.stdin:
#     parser.success = True
#     parser.parse(linha)
#     if parser.success:
#         print("Frase válida!")
#     else:
#         print("Frase inválida... Corrija e tente novamente!")
