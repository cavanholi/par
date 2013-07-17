#!/usr/bin/env python
#-*- coding: utf-8 -*-

class NPC:
 def __init__(self, cod, name, attr, hitRate, backpack, purse, profession, \
	      luck=7, charLevel=1):
  self.cod        = cod
  self.name       = name
  self.attr       = attr # dict {'str': #, 'dex': #, 'int': #, 'exp': #}
  self.hitRate    = hitRate
  self.luck       = luck
  self.backpack   = backpack
  self.purse      = purse
  self.profession = profession
  self.charLevel  = charLevel

 def bonus():
  for a in self.attr:
   for t in self.profession.bonus:
    if a == t: self.attr[a] += self.profession.bonus[t]

class Fighters(NPC):
 def __init__(self, cod, name, nickname, attr, hitRate, backpack, purse, \
              profession, weapon, armor, luck=7, charLevel=1):
  NPC.__init__(self, cod, name, attr, hitRate, backpack, \
               purse, profession, luck, charLevel)
  self.nickname = nickname
  self.weapon   = weapon
  self.armor    = armor

class Hero(Fighters):
 def __init__(self, cod, name, nickname, attr, hitRate, backpack, purse, \
              profession, weapon, armor, quests, luck=7, charLevel=1):
  Fighters.__init__(self, cod, name, name, attr, hitRate, backpack, purse, \
                    profession, weapon, armor, luck, charLevel)
  self.quests = quests

class Professions:
 def __init__(self, cod, name, bonus, requisites, level=0):
  self.cod        = cod
  self.name       = name
  self.bonus      = bonus
  self.requisites = requisites
  self.level      = level
