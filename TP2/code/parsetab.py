
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHAR CHARACTERS COLON COMMA DEF EQUAL EXPGRAM EXPRESSION HASHTAGS IGNORE INITVAR INITYACC LEFT LEFTBRACKET LEFTCOTTER LEXMARKER LITERALS NAMEFUNC NAMEPROD NAMEVAR NEWLINE PARSEYACC PRECEDENCE RE RETURNEDPRODS RIGHT RIGHTBRACKET RIGHTCOTTER SLEFTBRACKET SQM SRIGHTBRACKET STRING TOKENS UPPERWORD WORD YACCMARKERphrase : lex yacclex : LEXMARKER literals ignore tokens functionsliterals : LITERALS EQUAL CHARACTERS commentliterals : comment : HASHTAGS words NEWLINEcomment : words : words WORDwords : WORDignore : IGNORE EQUAL CHARACTERS commentignore : tokens : TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET commenttokens : tokenNames : tokenNames COMMA SQM UPPERWORD SQMtokenNames : SQM UPPERWORD SQMfunctions : functions functionfunctions : function : RE LEFTBRACKET content RIGHTBRACKET comment content : SQM UPPERWORD SQM COMMA EXPRESSIONcontent : SQM UPPERWORD SQM COMMA WORDcontent : STRING COMMA EXPRESSIONcontent : CHARACTERS COMMA EXPRESSIONyacc : YACCMARKER precedence comment varsprecedence : PRECEDENCE EQUAL SLEFTBRACKET precedences SRIGHTBRACKETprecedence : precedences : precedences tokenprecedenceprecedences : tokenprecedence : LEFTBRACKET rl COMMA nametokensprec RIGHTBRACKET COMMAtokenprecedence : rl : SQM RIGHT SQMrl : SQM LEFT SQMnametokensprec :  nametokensprec COMMA SQM UPPERWORD SQMnametokensprec : nametokensprec COMMA SQM CHAR SQMnametokensprec : SQM CHAR SQMnametokensprec : SQM UPPERWORD SQMvars : WORD EQUAL LEFTCOTTER RIGHTCOTTERvars : prods : WORD COLON EXPGRAM LEFTCOTTER RETURNEDPRODS RIGHTCOTTER'
    
_lr_action_items = {'LEXMARKER':([0,],[3,]),'$end':([1,4,5,8,13,20,30,38,44,],[0,-1,-24,-6,-36,-22,-5,-23,-35,]),'YACCMARKER':([2,3,6,10,16,19,25,27,28,30,33,36,51,57,61,68,],[5,-4,-10,-12,-16,-6,-2,-6,-3,-5,-15,-9,-6,-6,-11,-17,]),'LITERALS':([3,],[7,]),'IGNORE':([3,6,19,28,30,],[-4,11,-6,-3,-5,]),'TOKENS':([3,6,10,19,27,28,30,36,],[-4,-10,17,-6,-6,-3,-5,-9,]),'RE':([3,6,10,16,19,25,27,28,30,33,36,51,57,61,68,],[-4,-10,-12,-16,-6,34,-6,-3,-5,-15,-9,-6,-6,-11,-17,]),'PRECEDENCE':([5,],[9,]),'HASHTAGS':([5,8,19,27,38,51,57,],[-24,14,14,14,-23,14,14,]),'WORD':([5,8,13,14,22,23,30,31,38,77,],[-24,-6,21,23,31,-8,-5,-7,-23,84,]),'EQUAL':([7,9,11,17,21,],[12,15,18,26,29,]),'CHARACTERS':([12,18,41,],[19,27,50,]),'SLEFTBRACKET':([15,26,],[24,35,]),'NEWLINE':([22,23,31,],[30,-8,-7,]),'SRIGHTBRACKET':([24,32,39,42,63,78,80,],[-26,38,-25,51,-14,-13,-27,]),'LEFTBRACKET':([24,32,34,39,80,],[-26,40,41,-25,-27,]),'LEFTCOTTER':([29,],[37,]),'SQM':([35,40,41,52,53,54,55,56,58,72,73,75,76,85,86,],[43,46,48,62,63,65,66,67,69,78,79,81,82,87,88,]),'RIGHTCOTTER':([37,],[44,]),'STRING':([41,],[49,]),'COMMA':([42,45,49,50,63,64,66,67,69,74,78,81,82,87,88,],[52,54,59,60,-14,73,-29,-30,77,80,-13,-33,-34,-31,-32,]),'UPPERWORD':([43,48,62,65,79,],[53,58,72,76,85,]),'RIGHT':([46,],[55,]),'LEFT':([46,],[56,]),'RIGHTBRACKET':([47,64,70,71,81,82,83,84,87,88,],[57,74,-20,-21,-33,-34,-18,-19,-31,-32,]),'EXPRESSION':([59,60,77,],[70,71,83,]),'CHAR':([65,79,],[75,86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'phrase':([0,],[1,]),'lex':([0,],[2,]),'yacc':([2,],[4,]),'literals':([3,],[6,]),'precedence':([5,],[8,]),'ignore':([6,],[10,]),'comment':([8,19,27,51,57,],[13,28,36,61,68,]),'tokens':([10,],[16,]),'vars':([13,],[20,]),'words':([14,],[22,]),'functions':([16,],[25,]),'precedences':([24,],[32,]),'function':([25,],[33,]),'tokenprecedence':([32,],[39,]),'tokenNames':([35,],[42,]),'rl':([40,],[45,]),'content':([41,],[47,]),'nametokensprec':([54,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> phrase","S'",1,None,None,None),
  ('phrase -> lex yacc','phrase',2,'p_phrase','parser_yacc.py',8),
  ('lex -> LEXMARKER literals ignore tokens functions','lex',5,'p_lex','parser_yacc.py',11),
  ('literals -> LITERALS EQUAL CHARACTERS comment','literals',4,'p_literals','parser_yacc.py',104),
  ('literals -> <empty>','literals',0,'p_literals_empty','parser_yacc.py',108),
  ('comment -> HASHTAGS words NEWLINE','comment',3,'p_comment','parser_yacc.py',112),
  ('comment -> <empty>','comment',0,'p_comment_empty','parser_yacc.py',117),
  ('words -> words WORD','words',2,'p_words','parser_yacc.py',121),
  ('words -> WORD','words',1,'p_words_stop','parser_yacc.py',125),
  ('ignore -> IGNORE EQUAL CHARACTERS comment','ignore',4,'p_ignore','parser_yacc.py',129),
  ('ignore -> <empty>','ignore',0,'p_ignore_empty','parser_yacc.py',133),
  ('tokens -> TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment','tokens',6,'p_tokens','parser_yacc.py',136),
  ('tokens -> <empty>','tokens',0,'p_tokens_empty','parser_yacc.py',140),
  ('tokenNames -> tokenNames COMMA SQM UPPERWORD SQM','tokenNames',5,'p_tokenNames','parser_yacc.py',143),
  ('tokenNames -> SQM UPPERWORD SQM','tokenNames',3,'p_tokenNames_stop','parser_yacc.py',147),
  ('functions -> functions function','functions',2,'p_functions','parser_yacc.py',151),
  ('functions -> <empty>','functions',0,'p_functions_empty','parser_yacc.py',155),
  ('function -> RE LEFTBRACKET content RIGHTBRACKET comment','function',5,'p_function','parser_yacc.py',159),
  ('content -> SQM UPPERWORD SQM COMMA EXPRESSION','content',5,'p_content_returned','parser_yacc.py',164),
  ('content -> SQM UPPERWORD SQM COMMA WORD','content',5,'p_content_returnedWord','parser_yacc.py',168),
  ('content -> STRING COMMA EXPRESSION','content',3,'p_content_string','parser_yacc.py',172),
  ('content -> CHARACTERS COMMA EXPRESSION','content',3,'p_content_characters','parser_yacc.py',177),
  ('yacc -> YACCMARKER precedence comment vars','yacc',4,'p_yacc','parser_yacc.py',188),
  ('precedence -> PRECEDENCE EQUAL SLEFTBRACKET precedences SRIGHTBRACKET','precedence',5,'p_precedence','parser_yacc.py',193),
  ('precedence -> <empty>','precedence',0,'p_precedence_empty','parser_yacc.py',197),
  ('precedences -> precedences tokenprecedence','precedences',2,'p_precedences_varios','parser_yacc.py',202),
  ('precedences -> <empty>','precedences',0,'p_precedences_vazio','parser_yacc.py',205),
  ('tokenprecedence -> LEFTBRACKET rl COMMA nametokensprec RIGHTBRACKET COMMA','tokenprecedence',6,'p_tokenprecedence','parser_yacc.py',208),
  ('tokenprecedence -> <empty>','tokenprecedence',0,'p_tokenprecedence_vazio','parser_yacc.py',213),
  ('rl -> SQM RIGHT SQM','rl',3,'p_rl_r','parser_yacc.py',218),
  ('rl -> SQM LEFT SQM','rl',3,'p_rl_l','parser_yacc.py',221),
  ('nametokensprec -> nametokensprec COMMA SQM UPPERWORD SQM','nametokensprec',5,'p_nametokensprec','parser_yacc.py',225),
  ('nametokensprec -> nametokensprec COMMA SQM CHAR SQM','nametokensprec',5,'p_nametokensprec_char','parser_yacc.py',229),
  ('nametokensprec -> SQM CHAR SQM','nametokensprec',3,'p_nametokensprec_char_single','parser_yacc.py',233),
  ('nametokensprec -> SQM UPPERWORD SQM','nametokensprec',3,'p_nametokensprec_upperword_single','parser_yacc.py',238),
  ('vars -> WORD EQUAL LEFTCOTTER RIGHTCOTTER','vars',4,'p_vars','parser_yacc.py',245),
  ('vars -> <empty>','vars',0,'p_vars_empty','parser_yacc.py',250),
  ('prods -> WORD COLON EXPGRAM LEFTCOTTER RETURNEDPRODS RIGHTCOTTER','prods',6,'p_prods','parser_yacc.py',254),
]
