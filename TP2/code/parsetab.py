
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CHARACTERS COMMA EQUAL EXPRESSION HASHTAGS IGNORE LEFTBRACKET LEXMARKER LITERALS PRECEDENCE RE RIGHTBRACKET SLEFTBRACKET SPACE SQM SRIGHTBRACKET STRING TOKENS UPPERWORD WORD YACCMARKERphrase : lex lex : LEXMARKER literals ignore tokens functionsliterals : LITERALS EQUAL CHARACTERS commentliterals : comment : HASHTAGS wordscomment : words : words WORDwords : WORDignore : IGNORE EQUAL CHARACTERS commentignore : tokens : TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET commenttokens : tokenNames : tokenNames COMMA SQM UPPERWORD SQMtokenNames : SQM UPPERWORD SQMfunctions : functions functionfunctions : function : RE LEFTBRACKET content RIGHTBRACKET comment content : SQM UPPERWORD SQM COMMA EXPRESSIONcontent : SQM UPPERWORD SQM COMMA WORDcontent : STRING COMMA EXPRESSIONcontent : CHARACTERS COMMA EXPRESSION'
    
_lr_action_items = {'LEXMARKER':([0,],[3,]),'$end':([1,2,3,4,6,9,12,13,15,16,18,21,22,23,27,32,35,39,42,],[0,-1,-4,-10,-12,-16,-6,-2,-6,-3,-15,-9,-5,-8,-7,-6,-6,-11,-17,]),'LITERALS':([3,],[5,]),'IGNORE':([3,4,12,16,22,23,27,],[-4,7,-6,-3,-5,-8,-7,]),'TOKENS':([3,4,6,12,15,16,21,22,23,27,],[-4,-10,10,-6,-6,-3,-9,-5,-8,-7,]),'RE':([3,4,6,9,12,13,15,16,18,21,22,23,27,32,35,39,42,],[-4,-10,-12,-16,-6,19,-6,-3,-15,-9,-5,-8,-7,-6,-6,-11,-17,]),'EQUAL':([5,7,10,],[8,11,14,]),'CHARACTERS':([8,11,24,],[12,15,31,]),'HASHTAGS':([12,15,32,35,],[17,17,17,17,]),'SLEFTBRACKET':([14,],[20,]),'WORD':([17,22,23,27,47,],[23,27,-8,-7,50,]),'LEFTBRACKET':([19,],[24,]),'SQM':([20,24,33,34,36,46,],[26,29,40,41,43,48,]),'STRING':([24,],[30,]),'SRIGHTBRACKET':([25,41,48,],[32,-14,-13,]),'COMMA':([25,30,31,41,43,48,],[33,37,38,-14,47,-13,]),'UPPERWORD':([26,29,40,],[34,36,46,]),'RIGHTBRACKET':([28,44,45,49,50,],[35,-20,-21,-18,-19,]),'EXPRESSION':([37,38,47,],[44,45,49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'phrase':([0,],[1,]),'lex':([0,],[2,]),'literals':([3,],[4,]),'ignore':([4,],[6,]),'tokens':([6,],[9,]),'functions':([9,],[13,]),'comment':([12,15,32,35,],[16,21,39,42,]),'function':([13,],[18,]),'words':([17,],[22,]),'tokenNames':([20,],[25,]),'content':([24,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> phrase","S'",1,None,None,None),
  ('phrase -> lex','phrase',1,'p_phrase','parser_yacc.py',5),
  ('lex -> LEXMARKER literals ignore tokens functions','lex',5,'p_lex','parser_yacc.py',8),
  ('literals -> LITERALS EQUAL CHARACTERS comment','literals',4,'p_literals','parser_yacc.py',16),
  ('literals -> <empty>','literals',0,'p_literals_empty','parser_yacc.py',20),
  ('comment -> HASHTAGS words','comment',2,'p_comment','parser_yacc.py',24),
  ('comment -> <empty>','comment',0,'p_comment_empty','parser_yacc.py',29),
  ('words -> words WORD','words',2,'p_words','parser_yacc.py',33),
  ('words -> WORD','words',1,'p_words_stop','parser_yacc.py',37),
  ('ignore -> IGNORE EQUAL CHARACTERS comment','ignore',4,'p_ignore','parser_yacc.py',41),
  ('ignore -> <empty>','ignore',0,'p_ignore_empty','parser_yacc.py',45),
  ('tokens -> TOKENS EQUAL SLEFTBRACKET tokenNames SRIGHTBRACKET comment','tokens',6,'p_tokens','parser_yacc.py',48),
  ('tokens -> <empty>','tokens',0,'p_tokens_empty','parser_yacc.py',52),
  ('tokenNames -> tokenNames COMMA SQM UPPERWORD SQM','tokenNames',5,'p_tokenNames','parser_yacc.py',55),
  ('tokenNames -> SQM UPPERWORD SQM','tokenNames',3,'p_tokenNames_stop','parser_yacc.py',59),
  ('functions -> functions function','functions',2,'p_functions','parser_yacc.py',63),
  ('functions -> <empty>','functions',0,'p_functions_empty','parser_yacc.py',67),
  ('function -> RE LEFTBRACKET content RIGHTBRACKET comment','function',5,'p_function','parser_yacc.py',71),
  ('content -> SQM UPPERWORD SQM COMMA EXPRESSION','content',5,'p_content_returned','parser_yacc.py',78),
  ('content -> SQM UPPERWORD SQM COMMA WORD','content',5,'p_content_returnedWord','parser_yacc.py',82),
  ('content -> STRING COMMA EXPRESSION','content',3,'p_content_string','parser_yacc.py',86),
  ('content -> CHARACTERS COMMA EXPRESSION','content',3,'p_content_characters','parser_yacc.py',91),
]