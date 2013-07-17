#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Events:
  def __init__(self, cod, flag):
    # flags: end
    self.cod = cod
    self.flag = flag

class Show(Events):
  def __init__(self, cod, flag, name, alias, description, target):
    # flags: start, death, exit
    Events.__init__(self, cod, flag)
    self.name = name
    self.alias = alias
    self.description = description
    self.target = target

class Tests(Events):
  def __init__(self, cod, flag, prey, predator, target, aim):
    # flags: test, attrTest, market
    Events.__init__(self, cod, flag)
    self.prey = prey
    self.predator = predator
    self.target = target # dictionary: {'win': evId, 'lose': evId, 'epicWin': evId, 'epicFail': evId}
    self.aim = aim

class Quests(Events):
  def __init__(self, cod, flag, name, status, condition, results):
    # flags: quest
    Events.__init__(self, cod, flag)
    self.name = name
    self.status = status
    self.condition = condition # dictionary: {quest: 0..100}
    self.results = results
