import ply.yacc as yacc
from listas_lex import tokens



#[1,2,3,4,5]
#[1,2,3,start,2,3,end,5]



def p_Lista(p):
    "Lista : DELIM_ABRIR Lista2"

def p_Lista2(p):
    "Lista2 : LCont DELIM_FECHAR"

def p_lista2_vazia(p):
    "Lista2 : DELIM_FECHAR"

def p_LCont(p):
    "LCont : NUM LCont2"
    parser.comp +=1

def p_LCont_pal(p):
    "LCont : PAL LCont2"
    parser.comp +=1
    if(p[1] == "start"):
        parser.soma+= p[2]

def p_LCont2(p):
    "LCont2 : SEPARATOR NUM LCont2"
    parser.comp +=1
    p[0] = int(p[2]) + p[3]

def p_LCont2_pal(p):
    "LCont2 : SEPARATOR PAL LCont2"
    parser.comp +=1
    if(p[2] == "start"):
        parser.soma+= p[3]
    p[0] = 0
    

def p_LCont2_vazio(p):
    "LCont2 : "
    p[0] = 0


def p_error(p):
    print ("Error:",p)
    parser.erro = True
parser = yacc.yacc()





import sys
for linha in sys.stdin:
    parser.comp = 0
    parser.soma = 0
    parser.counting = False
    parser.output = 0
    parser.operacao = 1 # 1-soma, 2- subtração
    parser.erro = False # Controlar os erros
    parser.parse(linha) # Chamar o parse linha a linha
    if not parser.erro:
        print("Frase válida!")
        print(parser.output)
        print("A frase possui ",parser.comp)
        print("A soma é de ",parser.soma)
    else:
        print("Frase inválida... Corrija e tente novamente!")





