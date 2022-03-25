import ply.lex as lex
import sys
import os
import re


# "LIST_SIZE",
# "LIST_INTERVAL", "LIST_AGREGATION_SIZE", "LIST_AGREGATION_INTERVAL"


tokens = ["SEPARATOR", "DATA", "NEWLINE", "LISTSIZE"]


states = [
    ("header", "exclusive"),
]


def t_header_LISTSIZE(t):
      r'{(?P<min>\d+)(,(?P<max>\d+))?}'
      minSize = int(t.lexer.lexmatch.group("min"))
      maxSizeStr = t.lexer.lexmatch.group("max")

      if maxSizeStr:
          maxSize = int(t.lexer.lexmatch.group("max"))
      else:
          maxSize = minSize

      #lexer.sizesList[lexer.index] = (minSize, maxSize)
      lexer.context.pop(lexer.index)
      lexer.context.append("inicioLista")
      for i in range(maxSize-2):
          lexer.context.append("lista")
      if maxSize > 1:
          lexer.context.append("fimLista")
      return t


# def t_header_LISTSIZE(t):
#      r'{(?P<min>\d+)}'

#      minSize = int(t.lexer.lexmatch.group("min"))
#      print("minsize: ", minSize)
#      lexer.context.pop(lexer.index)
#      lexer.context.append("inicioLista")
#      for i in range(minSize-2):
#          lexer.context.append("lista")
#      if minSize > 1:
#          lexer.context.append("fimLista")
#      return t


def t_header_SEPARATOR(t):
    r','
    lexer.index += 1
    return t


def t_header_DATA(t):
    r'[^,\n{]+'
    lexer.context.append("normal")
    lexer.headers.append(t.value)
    lexer.sizesList.append(None)
    return t


def t_header_NEWLINE(t):
    r'\n'
    t.lexer.begin("INITIAL")
    lexer.jsonFile.write('\t{\n')
    lexer.index = 0

    print(lexer.headers)
    return t


def t_LISTSIZE(t):
    r'{(?P<min>\d+)(,(?P<max>\d+))?}'
    return t


def t_SEPARATOR(t):
    r','
    lexer.index += 1
    return t


def t_DATA(t):
    r'[^,\n]+'
    print("lexer index: ", lexer.index)
    print("lexer context: ", lexer.context)

    if(lexer.index == len(lexer.context) - 1):
        if lexer.context[lexer.index] == "inicioLista":
            lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : [' + str(t.value) + ']\n\t}'
            )
        elif lexer.context[lexer.index] == "fimLista":
            lexer.jsonFile.write(
                str(t.value + "]\n\t}")
            )
        else:
            lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(t.value) + '"\n\t}')

    else:
        if lexer.context[lexer.index] == "inicioLista" and lexer.context[lexer.index + 1] != "normal":
            lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : [' + str(t.value) + ',')
        elif lexer.context[lexer.index] == "inicioLista" and lexer.context[lexer.index + 1] == "normal":
            lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : [' + str(t.value) + '],\n')
        elif lexer.context[lexer.index] == "lista":
            lexer.jsonFile.write(
                str(t.value + ",")
            )
        elif lexer.context[lexer.index] == "fimLista":
            lexer.jsonFile.write(
                str(t.value + "],\n")
            )
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

lexer.context = []
lexer.sizesList = []
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
