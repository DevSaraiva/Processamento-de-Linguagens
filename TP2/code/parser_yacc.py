import os
import ply.yacc as yacc
from parser_lex import tokens
import sys
import re

def p_phrase(p):
    "phrase : lex yacc " #falta yacc

def p_lex(p):
    "lex : LEXMARKER literals ignore tokens functions"
    print(p[5])

    #write imports

    parser.outPutLexer.write('import ply.lex as lex\n\n')

    #write literals

    literals = p[2][0]
    literalsComment = p[2][1]

    parser.outPutLexer.write('literals = [')

    for index,x in enumerate(literals):
        if(x != '"'):
            parser.outPutLexer.write('\'' + x + '\'')
        if(index != len(literals) -1 and index != 0 and index != len(literals) -2):
            parser.outPutLexer.write(',')

    parser.outPutLexer.write(']\t\t' + '#' + literalsComment + '\n\n')

    # write ignore

    ignore = p[3][0]
    ignoreComment = p[3][1]
    parser.outPutLexer.write('ignore = ' + ignore)
    if(ignoreComment):
        parser.outPutLexer.write('#' +'\t\t' + ignoreComment + '\n\n')
    else:
        parser.outPutLexer.write('\n\n')


    # write tokens

    tokens = p[4][0].split(',')
    tokensComment = p[4][1]

    parser.outPutLexer.write('tokens = [')

    for index,token in enumerate(tokens):
    
        parser.outPutLexer.write('\'' + token + '\'')
        if(index != len(tokens) -1):
            parser.outPutLexer.write(',')
    parser.outPutLexer.write(']')

    if(tokensComment):
        parser.outPutLexer.write('#' +'\t\t' + tokensComment + '\n\n')
    else:
        parser.outPutLexer.write('\n\n\n')


    #write functions

    functions = p[5]

    for function in functions:
        comment = function[2]
        functionName = function[1][0] #no caso de ser uma função de erro functionName vai conter o print
        functionRE = function[0].split(' return')
        functionReturnType = function[1][1] #no caso de ser uma função de erro conterá o tratamento

        if(comment):
            parser.outPutLexer.write(f"#{comment}")

        if(len(functionRE) != 2):
            #error case
            functionRE = function[0].split(' error')
            parser.outPutLexer.write('def t_error(t):\n\t')
            parser.outPutLexer.write(f"print({functionName})\n\t")
            parser.outPutLexer.write(f"{functionReturnType}\n")

        else:
            #function case
            
            parser.outPutLexer.write('def t_' + functionName + '(t):\n\t')
            parser.outPutLexer.write(f"r'{functionRE[0]}'\n\t")
            
            #verify return type

            match = re.search(r'([a-zA-Z]+)\([^\)]*\)(\.[^\)]*\))?', functionReturnType)
            
            #modify the return
            
            if match:
                nameModifyFunction = match.group(1)
                parser.outPutLexer.write(f"t.value = {nameModifyFunction}(t.value)\n\t")
                 
            parser.outPutLexer.write('return(t)\n\n')



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
     p[0] = p[1] + ',' + p[4]

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
    "yacc : YACCMARKER precedence " # vars prods functionsyacc INITYACC parse"
    print(p[1])

def p_precedence(p):
    "precedence : PRECEDENCE EQUAL SLEFTBRACKET precedences SRIGHTBRACKET"
    print(p[1],p[2],p[3],p[5])

def p_precedence_empty(p):
    "precedence : "

def p_precedences_varios(p):
     "precedences : precedences tokenprecedence"

# def p_precedences_unico(p):
#     "precedences : tokenprecedence COMMA"


def p_precedences_vazio(p):
     "precedences : "

def p_tokenprecedence(p):
     "tokenprecedence : LEFTBRACKET rl COMMA nametokensprec RIGHTBRACKET COMMA" # nametokensprec

def p_tokenprecedence_vazio(p):
     "tokenprecedence : " # nametokensprec


def p_rl_r(p):
      "rl : SQM RIGHT SQM"

def p_rl_l(p):
      "rl : SQM LEFT SQM"




def p_nametokensprec(p):
    "nametokensprec : nametokensprec COMMA" #  FALTA OS CARACTERS A SEGUIR AO COMMA
    # p[0] = f'{p[1]}, {p[3]}'

def p_nametokensprec_empty(p):
    "nametokensprec :"
    # p[0] = ""

# def p_vars(p): 
#     "vars : NAMEVAR EQUAL EXPRESSION"
#     # p[0] = f'{p[1]} = {3}'

# def p_vars_empty(p):
#     "vars : "
   

# def p_prods(p):
#      "prods : NAMEPROD COLON expGram LEFTCOTTER returnedProds RIGHTCOTTER"
#      p[0] = f'def p_{p[0]}(p):\n\t"{p[3]}"\n\t{p[5]}\n'

#      # def p_{p[0]}(p):  \n
#      # \t    "{p[3]}"    \n
#      # \t    {p[5]}      \n

# def p_functionsyacc(p):
#      "functionsyacc : DEF NAMEFUNC LEFTBRACKET CHARACTERS RIGHTBRACKET COLON"
#      p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}{p[5]}{p[6]}'

# def p_functionsyacc_Empty(p):
#      "functionsyacc :"
#      p[0] = ""

# def p_parse(p):
#      "parse : PARSEYACC LEFTBRACKET CHARACTERS RIGHTBRACKET"
#      p[0] = f"y.parse({p[3]})"


# Build the parser
parser = yacc.yacc()

#Read Input File

filename = sys.argv[1]
inputDir = os.getcwd() + '/input/' + filename
input = open(inputDir, 'r').read()

#Create Output Files
outputDir = os.getcwd() + '/output/' + filename.replace(".txt","")

parser.outPutLexer = open(outputDir + "-LEXER.py", "w")
parser.outPutYacc = open(outputDir + "-YACC.py", "w")






parser.parse(input)
