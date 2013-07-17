#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Items:
 def __init__(self, cod, name, iType = 'item', amount=1):
  self.cod    = cod
  self.name   = name
  self.iType = iType
  self.amount = amount

class Weapons(Items):
 def __init__(self, cod, name, damage, hitChance, mastery, iType = 'weapon', amount=1):
  Items.__init__(self, cod, name, iType, amount)
  self.damage    = damage
  self.hitChance = hitChance
  self.mastery   = mastery

class RangeWeapons(Weapons):
 def __init__(self, cod, name, damage, hitChance, \
              mastery, distance, ammoType, iType = 'ranged', amount=1):
  Weapons.__init__(self, cod, name, damage, hitChance, mastery, iType, amount)
  self.distance = distance
  self.ammoType = ammoType

class Ammo(Items):
 def __init__(self, cod, name, damInc, ammoType, iType = 'ammo', amount=1):
  Items.__init__(self, cod, name, iType, amount)
  self.damInc   = damInc
  self.ammoType = ammoType

class Armor(Items):
 def __init__(self, cod, name, defense, life, iType = 'armor', amount=1):
  Items.__init__(self, cod, name, iType, amount)
  self.defense = defense
  self.life    = life
