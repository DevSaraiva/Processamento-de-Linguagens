from ast import Return
import ply.lex as lex
import sys
import os
import re


# "LIST_SIZE",
# "LIST_INTERVAL", "LIST_AGREGATION_SIZE", "LIST_AGREGATION_INTERVAL"


tokens = ["SEPARATOR", "DATA", "NEWLINE"]


states = [
    ("header", "exclusive"),
]


def t_header_SEPARATOR(t):
    r','
    return t


def t_header_DATA(t):
    r'[^,\n]+'
    lexer.headers.append(t.value)
    return t


def t_header_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    lexer.jsonFile.write('\t{\n')
    return t


def t_SEPARATOR(t):
    r','
    lexer.index += 1
    return t


def t_DATA(t):
    r'[^,\n]+'
    print(lexer.index)

    if(lexer.index == len(lexer.headers) - 1):
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(t.value) + '"\n\t}')

    else:
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(t.value) + '",\n')

    return t


def t_NEWLINE(t):
    r'\n'
    lexer.index = 0
    lexer.jsonFile.write(',\n\t{\n')
    return t


def t_error(t):
    print("Este token nao e reconhecido", t.value)
    t.lexer.skip(1)


    # Criar instância de lex
lexer = lex.lex()


# state
# verificar se é necessário
filename = os.path.basename("./alunos.csv")

filenameFormatted = re.sub(r'(\w+).csv', r'\1', filename)

final_Filename = filenameFormatted + ".json"

lexer.headers = []
lexer.jsonFile = open(final_Filename, "w", encoding="utf-8")
lexer.index = 0

lexer.begin("header")


# Alimentar o lexer
lexer.jsonFile.write('[\n')

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)


lexer.jsonFile.write('\n]')

print(lexer.headers)
