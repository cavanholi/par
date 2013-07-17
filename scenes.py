#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Events:
 def __init__(self, cod, flag):
  # flags: end
  self.cod  = cod
  self.flag = flag

class Show(Events):
 def __init__(self, cod, flag, name, alias, desc, target):
  # flags: start, death, exit
  Events.__init__(self, cod, flag)
  self.name   = name
  self.alias  = alias
  self.desc   = desc
  self.target = target

class Tests(Events):
 def __init__(self, cod, flag, alias, prey, pred, target, aim):
  # flags: test, attrTest, market
  Events.__init__(self, cod, flag)
  self.alias  = alias
  self.prey   = prey
  self.pred   = pred
  self.target = target # dict: {'win': evId, 'lose': evId, \
                       #        'epicWin': evId, 'epicFail': evId}
  self.aim    = aim

class Quests(Events):
 def __init__(self, cod, flag, name, status, cond, result):
  # flags: quest
  Events.__init__(self, cod, flag)
  self.name   = name
  self.status = status
  self.cond   = cond # dict: {quest: 0..100}
  self.result = result
