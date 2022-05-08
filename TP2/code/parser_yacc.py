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


import ply.yacc as yacc
from parser_lex import tokens