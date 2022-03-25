import ply.lex as lex
import sys
import os
import re


# "LIST_SIZE",
# "LIST_INTERVAL", "LIST_AGREGATION_SIZE", "LIST_AGREGATION_INTERVAL"


tokens = ["SEPARATOR", "DATA", "NEWLINE", "LISTSIZE", "AGREGATION"]


states = [
    ("header", "exclusive"),
    ("listReader", "inclusive")
]


def t_header_LISTSIZE(t):
    r'{(?P<min>\d+)(,(?P<max>\d+))?}'
    minSize = int(t.lexer.lexmatch.group("min"))
    maxSizeStr = t.lexer.lexmatch.group("max")

    if maxSizeStr:
        maxSize = int(t.lexer.lexmatch.group("max"))
    else:
        maxSize = minSize

    lexer.maxSize = maxSize
    # lexer.sizesList[lexer.index] = (minSize, maxSize)
    lexer.context.pop(lexer.index)
    lexer.context.append("inicioLista")
    for i in range(maxSize-2):          # menos 2 é o inicioLista e fimLista
        lexer.context.append("lista")
    if maxSize > 1:
        lexer.context.append("fimLista")


    for j in range(maxSize-1):
        lexer.headers.append(lexer.headers[lexer.index])
        lexer.agregation.append("no_Agregation")            #TODO: no caso de apanhar a funcao agregation temos que dar popp destes no_Agregation todos 
    return t


def t_header_SEPARATOR(t):
    r','
    lexer.index += 1
    return t


def t_header_DATA(t):
    r'[^:,\n{]+'
    lexer.context.append("normal")
    lexer.agregation.append("no_Agregation")
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



def t_header_AGREGATION(t):
    r'::(?P<func>\w+),'
    
    agreg_func = t.lexer.lexmatch.group("func")

    

    columnName = lexer.headers.pop(lexer.index)


    if agreg_func == 'sum':
        for i in range(lexer.maxSize):
            lexer.agregation.pop(lexer.index)
            lexer.agregation.append("sum")
            lexer.headers.append(columnName + "_" + "sum")
        print(lexer.agregation)
        lexer.maxSize = 0                   # reset the max size variable after filling the agregation array

    elif agreg_func == 'media':
        for j in range(lexer.maxSize):
            lexer.agregation.pop(lexer.index)
            lexer.agregation.append("media")
            lexer.headers.append(columnName + "_" + "media")
        lexer.maxSize = 0                   # reset the max size variable after filling the agregation array
        










def t_listReader_DATA(t):
    r'[^,\n]+'
    print("lexer index: ", lexer.index)
    print("lexer context: ", lexer.context)

    lexer.opList.append(t.value)
    return t


def t_listReader_NEWLINE(t):
    r'\n'

    if lexer.context[lexer.index] == "fimLista"  and lexer.agregation[lexer.index] == "no_Agregation":
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : ['  + lexer.opList[0])
        
        for j in range(len(lexer.opList)-1):
            lexer.jsonFile.write(
                str("," +lexer.opList[j+1]) )             

        lexer.jsonFile.write(
                str("]\n\t}")                             
            )


        t.lexer.opList = []    
        lexer.index = 0
        t.lexer.begin("INITIAL")
        lexer.jsonFile.write(',\n\t{\n')



    elif lexer.context[lexer.index] == "fimLista" and lexer.agregation[lexer.index] != "no_Agregation":
        opValue = 0
        for i in range(len(lexer.opList)):
            if (lexer.agregation[lexer.index] == "sum"):
                opValue += int(lexer.opList[i])
            elif lexer.agregation[lexer.index] == "media":
                opValue += int(lexer.opList[i])
        
        #caso a operação pretendida seja a media, temos que dividir pelo nº total de elementos
        if lexer.agregation[lexer.index] == "media":
            opValue = opValue/len(lexer.opList)

        lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(opValue) + '"\n\t}')

        

        t.lexer.opList = []    
        lexer.index = 0
        t.lexer.begin("INITIAL")
        lexer.jsonFile.write(',\n\t{\n')
    

    lexer.index = 0
    return t


def t_listReader_SEPARATOR(t):
    r','

    if lexer.context[lexer.index] == "fimLista" and lexer.context[lexer.index+1] != "fimLista" and lexer.agregation[lexer.index] == "no_Agregation":
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : ['  + lexer.opList[0])
        
        for j in range(len(lexer.opList)-1):
            lexer.jsonFile.write(
                str("," +lexer.opList[j+1]) )             #TODO: ultimo elemento da lista vai ter uma virgula a mais

        lexer.jsonFile.write(
                str("],\n")                             #TODO: temos que verificar se precisa da virgula (pq nao e o ultumo)
            )
        t.lexer.opList = []    
        t.lexer.begin("INITIAL")



    elif lexer.context[lexer.index] == "fimLista" and lexer.context[lexer.index+1] != "fimLista" and lexer.agregation[lexer.index] != "no_Agregation":
    # elif (lexer.context[lexer.index] == "fimLista" and lexer.agregation[lexer.index] != "no_Agregation" and ((lexer.index == len(lexer.agregation) -1) or lexer.agregation[lexer.index+1] == "no_Agregation")):
        opValue = 0
        for i in range(len(lexer.opList)):
            if (lexer.agregation[lexer.index] == "sum"):
                opValue += int(lexer.opList[i])
            elif lexer.agregation[lexer.index] == "media":
                opValue += int(lexer.opList[i])
        
        #caso a operação pretendida seja a media, temos que dividir pelo nº total de elementos
        if lexer.agregation[lexer.index] == "media":
            opValue = opValue/len(lexer.opList)

        lexer.jsonFile.write(
                '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(opValue) + '",\n')

        
        t.lexer.opList = []    
        t.lexer.begin("INITIAL")
    
    lexer.index += 1
    return t


def t_LISTSIZE(t):
    r'{(?P<min>\d+)(,(?P<max>\d+))?}'
    return t


def t_SEPARATOR(t):
    r','

    if(lexer.context[lexer.index+1] == "inicioLista"):
        lexer.begin("listReader")

    

    lexer.index += 1
    return t


def t_DATA(t):
    r'[^,\n]+'

    if(lexer.index == len(lexer.headers) - 1):
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(t.value) + '"\n\t}')

    else:
        lexer.jsonFile.write(
            '\t\t"' + lexer.headers[lexer.index] + '" : "' + str(t.value) + '",\n')

    return t


def t_NEWLINE(t):
    r'\n'

    # if(lexer.context[lexer.index] == "fimLista" and lexer.agregation[lexer.index] != "no_Agregation"):
    #     opValue = 0
    #     for i in range(len(lexer.opList)):
    #         if (lexer.agregation[lexer.index] == "sum"):
    #             opValue += int(lexer.opList[i])
    #         elif lexer.agregation[lexer.index] == "media":
    #             opValue += int(lexer.opList[i])
        
    #     #caso a operação pretendida seja a media, temos que dividir pelo nº total de elementos
    #     if lexer.agregation[lexer.index] == "media":
    #         opValue = opValue/len(lexer.opList)

    #     lexer.jsonFile.write(
    #             '\t\t"' + lexer.headers[lexer.index-4] + '" : "' + str(opValue) + '",\n')


    lexer.index = 0
    t.lexer.begin("INITIAL")
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
lexer.maxSize = 0
lexer.agregation = []   # em cada index indica se é para aplicar ou nao uma operacao de agregação
lexer.opList = []   # lista na qual se vai aplicar os operadores
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

# print("headers:" + lexer.headers)
# print("agregation:" + lexer.agregation)
# print("context:" + lexer.context)

print(lexer.opList)
