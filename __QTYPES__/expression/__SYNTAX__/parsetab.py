
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'BBFE57B32B5728E9D5E219A877DAD235'
    
_lr_action_items = {'$end':([4,5,6,8,9,11,12,23,24,25,26,27,28,29,34,35,],[0,-18,-17,-19,-20,-15,-16,-8,-2,-5,-1,-3,-4,-6,-7,-9,]),'LPAREN':([0,1,2,3,5,7,9,13,14,15,16,17,18,19,33,],[1,1,1,1,19,1,-20,1,1,1,1,1,1,1,1,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,29,33,34,35,],[2,2,2,2,13,-18,-17,2,-19,-20,13,-15,-16,2,2,2,2,2,2,2,13,-8,-2,-5,-1,-3,-4,13,2,-7,-9,]),'NAME':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,23,24,25,26,27,28,29,33,34,35,],[3,3,3,3,15,-18,-17,3,-19,-20,15,-15,-16,3,3,3,3,3,3,3,15,-8,-2,-5,-1,-3,-4,15,3,-7,-9,]),'TIMES':([4,5,6,8,9,10,11,12,20,23,24,25,26,27,28,29,34,35,],[16,-18,-17,-19,-20,16,-15,-16,16,-8,16,-5,16,-3,-4,16,-7,-9,]),'DIVIDE':([4,5,6,8,9,10,11,12,20,23,24,25,26,27,28,29,34,35,],[17,-18,-17,-19,-20,17,-15,-16,17,-8,17,-5,17,-3,-4,17,-7,-9,]),'EXP':([4,5,6,8,9,10,11,12,20,23,24,25,26,27,28,29,34,35,],[14,-18,-17,-19,-20,14,-15,-16,14,-8,14,-5,14,14,14,14,-7,-9,]),'COMMA':([5,6,8,9,11,12,20,23,24,25,26,27,28,29,34,35,],[-18,-17,-19,-20,-15,-16,33,-8,-2,-5,-1,-3,-4,-6,-7,-9,]),'LBRACKET':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[7,7,7,7,7,7,7,7,7,7,7,7,7,]),'RBRACKET':([5,6,7,8,9,11,12,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,],[-18,-17,-21,-19,-20,-15,-16,-21,34,-10,-8,-2,-5,-1,-3,-4,-6,-13,-12,-14,-7,-9,-11,]),'RPAREN':([5,6,8,9,10,11,12,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[-18,-17,-19,-20,23,-15,-16,-21,-21,-10,-8,-2,-5,-1,-3,-4,-6,35,-13,-12,-14,-7,-9,-11,]),'NUMBER':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'CARET':([4,5,6,8,9,10,11,12,20,23,24,25,26,27,28,29,34,35,],[18,-18,-17,-19,-20,18,-15,-16,18,-8,-2,-5,-1,-3,-4,18,-7,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'empty':([7,19,20,33,],[22,22,31,22,]),'opt_comma':([20,],[32,]),'name':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'number':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'expression':([0,1,2,3,7,13,14,15,16,17,18,19,33,],[4,10,11,12,20,24,25,26,27,28,29,20,20,]),'list_of_expressions':([7,19,33,],[21,30,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','python.py',58),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','python.py',59),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','python.py',60),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','python.py',61),
  ('expression -> expression EXP expression','expression',3,'p_expression_binop','python.py',62),
  ('expression -> expression CARET expression','expression',3,'p_expression_xor','python.py',70),
  ('expression -> LBRACKET list_of_expressions RBRACKET','expression',3,'p_expression_list','python.py',76),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_grouped','python.py',82),
  ('expression -> name LPAREN list_of_expressions RPAREN','expression',4,'p_expression_call','python.py',88),
  ('list_of_expressions -> empty','list_of_expressions',1,'p_list_of_expressions','python.py',94),
  ('list_of_expressions -> expression COMMA list_of_expressions','list_of_expressions',3,'p_list_of_expressions','python.py',95),
  ('list_of_expressions -> expression opt_comma','list_of_expressions',2,'p_list_of_expressions','python.py',96),
  ('opt_comma -> empty','opt_comma',1,'p_opt_comma','python.py',107),
  ('opt_comma -> COMMA','opt_comma',1,'p_opt_comma','python.py',108),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','python.py',114),
  ('expression -> PLUS expression','expression',2,'p_expression_uplus','python.py',120),
  ('expression -> number','expression',1,'p_expression_atom','python.py',126),
  ('expression -> name','expression',1,'p_expression_atom','python.py',127),
  ('number -> NUMBER','number',1,'p_number','python.py',133),
  ('name -> NAME','name',1,'p_name','python.py',139),
  ('empty -> <empty>','empty',0,'p_empty','python.py',145),
]
