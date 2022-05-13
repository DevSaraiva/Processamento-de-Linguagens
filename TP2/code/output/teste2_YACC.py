import ply.yacc as yacc
from teste2_LEXER import tokens



def p_lista0(t):
	"lista :  DELIM_ABRIR lista"
	#nothing 

def p_lista1(t):
	"lista :  lcont DELIM_FECHAR"
	#nothing 

def p_lista2(t):
	"lista :  DELIM_FECHAR"
	comp += 1 

def p_lcont3(t):
	"lcont :  NUM lcont"
	comp += 1 

def p_lcont4(t):
	"lcont :  PAL lcont"
	comp += 1; if(p[1] == 'start'): soma += p[2] 

def p_lcont5(t):
	"lcont :  SEPARATOR NUM lcont"
	comp += 1; p[0] = int(p[2]) + p[3] 

def p_lcont6(t):
	"lcont :  SEPARATOR PAL lcont"
	comp += 1; if(p[2] == "start"): soma += p[3]; p[0] = 0 

def p_lcont7(t):
	"lcont : "
	p[0] = 0 

def p_error(p):
	print ("Error:",p)
	erro = True


ya = yacc.yacc()

#comentario inteligente
ya.comp = 0
ya.soma = 0
ya.counting = False
ya.output = 0
ya.operacao = 1       
ya.erro = False       

ya.parse("3+4*7")