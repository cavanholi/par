#!/usr/bin/env python
#-*- coding: utf-8 -*-

from characters import *
from random import randint as rand

raw_input("generatin hero")
dic = {'str': 0, 'dex': 0, 'int': 0, 'exp': 0}
pool = 12
while True:
 print '\n' * 10
 print '=' * 5
 print "[S]trengh     - ", dic['str']
 print "[D]exterity   - ", dic['dex']
 print "[I]nteligence - ", dic['int']
 print "[E]xpression  - ", dic['exp']
 choice = raw_input('_').lower()

 if choice   == 's': pool -= 1; dic['str'] += 1
 elif choice == 'd': pool -= 1; dic['dex'] += 1
 elif choice == 'i': pool -= 1; dic['int'] += 1
 elif choice == 'e': pool -= 1; dic['exp'] += 1

 if pool == 0: break

print '\n' * 10
name = raw_input('name: ')
#attr = {'str': stre, 'dex': dex, 'int': inte, 'exp': exp}
hit = rand(1, 3)+2
backpack = None
purse = 0
profession = None
weapon = None
armor = None
quests = None
hero = Hero(1, name, name, dic, hit, backpack, purse, profession, weapon, armor, quests)

print hero.attr
print type(hero.attr)
raw_input('hero generated')
print "generating foe"
stre = dex = inte = exp = 0
pool = 12
while pool > 0:
  choice = rand(1, 4)
  if choice == 1: pool -= 1; stre += 1
  elif choice == 2: pool -= 1; dex += 1
  elif choice == 3: pool -= 1; inte += 1
  else: pool -= 1; exp += 1

name = 'bugar'
attr = {'str': stre, 'dex': dex, 'int': inte, 'exp': exp}
hit1 = rand(1, 3)+2
foe = Fighters(2, name, name, attr, hit1, backpack, purse, profession, weapon, armor)
raw_input('foe generated')
print '\n' * 10
print '=' * len(hero.name)
print hero.name.upper()
print '-' * len(hero.name)
print 'Strenght    - ', hero.attr['str']
print 'Dexterity   - ', hero.attr['dex']
print 'Inteligence - ', hero.attr['int']
print 'Expression  - ', hero.attr['exp']
print '-' * len(hero.name)
print 'Hit-Rate: ', hero.hitRate

print '\n' * 2
print '=' * len(foe.name)
print foe.name.upper()
print '-' * len(foe.name)
print 'Strenght    - ', foe.attr['str']
print 'Dexterity   - ', foe.attr['dex']
print 'Inteligence - ', foe.attr['int']
print 'Expression  - ', foe.attr['exp']
print '-' * len(foe.name)
print 'Hit-Rate: ', foe.hitRate

raw_input('end')
