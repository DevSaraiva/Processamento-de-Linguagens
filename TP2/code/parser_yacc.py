import ply.yacc as yacc
from parser_lex import tokens

def p_phrase(p):
    "phrase : lex " #falta yacc

def p_lex(p):
    "lex : LEXMARKER literals ignore tokens functions"
    print(p[1])
    print(p[2])
    print(p[3])
    print(p[4])
    print(p[5])

def p_literals(p):
    "literals : LITERALS EQUAL CHARACTERS comment"
    p[0] = ((p[3]),p[4])
    
def p_literals_empty(p):
    "literals : "
    p[0] = "literals vazio"

def p_comment(p):
    "comment : HASHTAGS words"
    p[0] = p[2]
    

def p_comment_empty(p):
    "comment : "
    

def p_words(p):
    "words : words WORD"
    p[0] = p[1] + ' ' +p[2]

def p_words_stop(p):
    "words : WORD"
    p[0] = p[1]

def p_ignore(p):
    "ignore : IGNORE EQUAL CHARACTERS comment"
    p[0] = (p[3],p[4])

def p_ignore_empty(p):
    "ignore : "

def p_tokens(p):
    "tokens : TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment"
    p[0] = (p[4],p[6])

def p_tokens_empty(p):
    "tokens : "

def p_tokenNames(p):
     "tokenNames : tokenNames COMMA SQM UPPERWORD SQM"
     p[0] = p[1] + ', ' + p[4]

def p_tokenNames_stop(p):
    "tokenNames : SQM UPPERWORD SQM"
    p[0] = p[2]

def p_functions(p):
    "functions : functions function"
    p[0] = p[1] + [p[2]]

def p_functions_empty(p):
    "functions : "
    p[0] = []

def p_function(p):
    "function : RE LEFTBRACKET content RIGHTBRACKET comment "
    p[0] = (p[1],p[3],p[5])
    print(p[1])
    print(p[0])


def p_content_returned(p):
    "content : SQM UPPERWORD SQM COMMA EXPRESSION"
    p[0] = (p[2],p[5])

def p_content_returnedWord(p):
    "content : SQM UPPERWORD SQM COMMA WORD"
    p[0] = (p[2],p[5])

def p_content_string(p):
    "content : STRING COMMA EXPRESSION"
    p[0] = (p[1],p[3])


def p_content_characters(p):
    "content : CHARACTERS COMMA EXPRESSION"
    p[0] = (p[1],p[3])

def p_error(p):
      print(f"Illegal token yacc'{p}'")
        

#YACC


def p_yacc(p):
    "yacc : YACCMARKER precedence vars prods functionsyacc INITYACC parse"
    print(p[1])

def p_precedence(p):
    "precedence : PRECEDENCE EQUAL SLEFTBRACKET precedences SRIGHTBRACKET"
    print(p[1],p[2])

def p_precedence_empty(p):
    "precedence : "

def p_precedences_varios(p):
     "precedences : precedences tokenprecedence"

# def p_precedences_unico(p):
#     "precedences : tokenprecedence COMMA"


def p_precedences_vazio(p):
     "precedences : "

def p_tokenprecedence(p):
     "tokenprecedence : LEFTBRACKET rl COMMA RIGHTBRACKET COMMA" # nametokensprec

def p_tokenprecedence_vazio(p):
     "tokenprecedence : " # nametokensprec


def p_rl_r(p):
      "rl : SQM RIGHT SQM"

def p_rl_l(p):
      "rl : SQM LEFT SQM"




# def p_nametokensprec(p):
#     "nametokensprec : nametokensprec COMMA CHARACTERS"
#     p[0] = f'{p[1]}, {p[3]}'

# def p_nametokensprec_Empty(p):
#     "nametokensprec :"
#     p[0] = ""

# def p_vars(p):
#     "vars : NAMEVAR EQUAL INITVAR"
#     p[0] = f'{p[1]} = {3}'

# def p_prods(p):
#     "prods : NAMEPROD COLON expGram LEFTCOTTER returnedProds RIGHTCOTTER"
#     p[0] = f'def p_{p[0]}(p):\n\t"{p[3]}"\n\t{p[5]}\n'

#     # def p_{p[0]}(p):  \n
#     # \t    "{p[3]}"    \n
#     # \t    {p[5]}      \n

# def p_functionsyacc(p):
#     "functionsyacc : DEF NAMEFUNC LEFTBRACKET CHARACTERS RIGHTBRACKET COLON"
#     p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}'

# def p_functionsyacc_Empty(p):
#     "functionsyacc :"
#     p[0] = ""

# def p_parse(p):
#     "parse : PARSEYACC LEFTBRACKET CHARACTERS RIGHTBRACKET"
#     p[0] = f"y.parse({p[3]})"


# Build the parser
parser = yacc.yacc()


input = '''
%%LEX
%literals = "+-/*=()" ##singlechar
%ignore = " \t\n"
%tokens = [ 'VAR','NUMBER'  ]
[a-zA-Z_][a-zA-Z0-9_]* return('VAR', t.value)
\d+(\.\d+)? return('NUMBER', float(t.value))
.   error(f"Illegal character '{t.value[0]}', [{t.lexer.lineno}]",
t.lexer.skip(1) )
%%YACC 
%precedence = [ 
     ('left',),
     ('left',),
     ('right',),
]'''






parser.parse(input)
