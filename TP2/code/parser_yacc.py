import ply.yacc as yacc
from parser_lex import tokens

def p_phrase(p):
    "frase : lex yacc" #falta yacc

def p_lex(p):
    "lex : LEXMARKER literals ignore tokens functions"
    print(p[1])
    print(p[2])
    print(p[3])

def p_literals(p):
    "literals : LITERALS EQUAL CHARACTERS comment"
    p[0] = repr(p[3])
    print(p[2])

def p_literals_empty(p):
    "literals : "
    p[0] = "literals vazio"

def p_comment(p):
    "comment : HASHTAGS words"
    print(f"comment {p[2]}")

def p_comment_empty(p):
    "comment : "
    print("sem comentários")

def p_words(p):
    "words : words WORD"
    p[0] = p[1] + ' ' +p[2]

def p_words_stop(p):
    "words : WORD"
    p[0] = p[1]

def p_ignore(p):
    "ignore : IGNORE EQUAL CHARACTERS comment"
    p[0] = repr(p[3])

def p_ignore_empty(p):
    "ignore : "

def p_tokens(p):
    "tokens : TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment"
    print(p[4])


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

def p_functions_empty(p):
    "functions : "

def p_function(p):
    "function : RE LEFTBRACKET content RIGHTBRACKET comment "
    print(p[1])


def p_content_returned(p):
    "content : SQM UPPERWORD SQM COMMA EXPRESSION"
    print(p[2])
    print(p[5])


def p_content_returnedWord(p):
    "content : SQM UPPERWORD SQM COMMA WORD"
    print(p[2])
    print(p[5])

def p_content_string(p):
    "content : STRING COMMA EXPRESSION"
    print(p[1])
    print(p[3])

def p_content_characters(p):
    "content : CHARACTERS COMMA EXPRESSION"
    print(p[1])
    print(p[3])



def p_yacc(p):
    "yacc : YACCMARKER precedence" # vars prods functionsyacc INITYACC parse"
    print(p[1])

def p_precedence(p):
     "precedence : PRECEDENCE EQUAL SLEFTBRACKET tokensprecedences SRIGHTBRACKET"

def p_precedence_empty(p):
     "precedence : "

def p_tokensprecedences(p):
     "tokensprecedences : tokenprecedences COMMA tokensprecedences"

def p_tokensprecedences_unico(p):
     " tokensprecedences : tokenprecedence"

def p_tokenprecedence(p):
     "tokenprecedence : LEFTBRACKET rl COMMA  RIGTHBRACKET" # nametokensprec

def p_rl_r(p):
     "rl : SQM RIGHT SQM"

def p_rl_l(p):
     "rl : SQM LEFT SQM"

def p_error(p):
     print(f"Illegal token yacc'{p}'")
        


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
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
]
'''





parser.parse(input)
