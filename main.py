#!/usr/bin/env python
#-*- coding: utf-8 -*-

from characters   import *
from scenes       import *
from items        import *
from random       import randint as rand
from ConfigParser import SafeConfigParser

# ========== NEW GAME ========== #
def newGame():
 print '\n' * 100
 eventList = loadEvents()
 eventList = link(eventList)
 itemList  = loadItems()
 profList  = loadProfession()
 hero      = generateHero(itemList, profList)
 foeList   = loadFoeList(itemList, profList)
 start(eventList, hero, foeList, itemList)

# ========== LOAD GAME ========== #

# ========== SETUP ========== #

# ----- loading/events ----- #
def loadEvents():
 cfg = config()
 eventList = []
 showHeader  = cfgHeader('sc', cfg['scenes'])
 testHeader  = cfgHeader('ts', cfg['tests'])
 questHeader = cfgHeader('qs', cfg['quests'])

 parser = SafeConfigParser()
 parser.read('data/events.info')

 for show in showHeader:
  cod     = int(parser.get(show, 'cod'))
  flag    = parser.get(show, 'flag')
  name    = parser.get(show, 'name')
  alias   = parser.get(show, 'alias')
  desc    = parser.get(show, 'desc')
  target  = eval(parser.get(show, 'target'))
  eventList.append(Scenes(cod, flag, name, alias, desc, target))

 for test in testHeader:
  cod    = int(parser.get(test, 'cod'))
  flag   = parser.get(test, 'flag')
  alias  = parser.get(test, 'alias')
  prey   = parser.get(test, 'prey')
  pred   = parser.get(test, 'pred')
  target = eval(parser.get(test, 'target'))
  aim    = parser.get(test, 'aim')
  eventList.append(Tests(cod, flag, alias, prey, pred, target, aim))

 for quest in questHeader:
  cod    = int(parser.get(quest, 'cod'))
  flag   = parser.get(quest, 'flag')
  name   = parser.get(quest, 'name')
  status = eval(parser.get(quest, 'status'))
  cond   = eval(parser.get(quest, 'cond'))
  result = eval(parser.get(quest, 'result'))
  eventList.append(Quests(cod, flag, name, status, cond, result))

 #parser = SafeConfigParser()
 #parser.read('data/events.info')
 eCod  = parser.get('end', 'cod')
 eFlag = parser.get('end', 'flag')
 eventList.append(Events(eCod, eFlag))

 return eventList

# ----- events/link ----- #

def link(eventList):
 for event in eventList:
  if event.flag == 'show' or event.flag == 'start':
   print event.name
   print type(event.target)
   for i in range(len(event.target)):
    for event2 in eventList:
      if event.target[i] == event2.cod and (event2.flag == 'show' or event2.flag == 'start'):
        print i, event.target[i], event2.name
        event.target[i] = event2
   raw_input()

 for event in eventList:
  if event.flag == 'show' or event.flag == 'start':
   print event.name
   print event.target
   for t in event.target:
    print type(t)
    print t.cod, t.name
 raw_input()

# ----- config ----- #
def config():
 parser = SafeConfigParser()
 parser.read('data/info.cfg')
 scenes = int(parser.get('default', 'scenes'))
 tests  = int(parser.get('default', 'tests'))
 quests = int(parser.get('default', 'quests'))
 return {'scenes': scenes, 'tests': tests, 'quests': quests}

def cfgHeader(header, n):
 cfgList = []
 for i in range(n):
  cfgList.append(header+str(i+1))
 return cfgList

# ----- loading/items ----- #
def loadItems():
 itemList      = []
 itemHeader    = []
 weaponHeader  = []
 rangedWHeader = []
 ammoHeader    = []
 armorHeader   = []
 sectionList   = []

 parser = SafeConfigParser()
 parser.read('data/items.info')
 for section in parser.sections():
  sectionList.append(section)

 for item in sectionList:
  if item[0:2] == 'it': itemHeader.append(item)
  elif item[0:2] == 'wp': weaponHeader.append(item)
  elif item[0:2] == 'rw': rangedWHeader.append(item)
  elif item[0:2] == 'am': ammoHeader.append(item)
  elif item[0:2] == 'ar': armorHeader.append(item)
  else: 
   raw_input('error while loading the items.')
   break

 for item in itemHeader:
  cod  = int(parser.get(item, 'cod'))
  name = parser.get(item, 'name')
  itemList.append(Items(cod, name))

 for weapon in weaponHeader:
  cod  = int(parser.get(weapon, 'cod'))
  name = parser.get(weapon, 'name')
  dam  = int(parser.get(weapon, 'dam'))
  hit  = int(parser.get(weapon, 'hit'))
  mast = int(parser.get(weapon, 'mast'))
  itemList.append(Weapons(cod, name, dam, hit, mast))

 for weapon in rangedWHeader:
  cod  = int(parser.get(weapon, 'cod'))
  name = parser.get(weapon, 'name')
  dam  = int(parser.get(weapon, 'dam'))
  hit  = int(parser.get(weapon, 'hit'))
  mast = int(parser.get(weapon, 'mast'))
  dist = int(parser.get(weapon, 'dist'))
  ammo = parser.get(weapon, 'ammo')
  itemList.append(RangeWeapons(cod, name, dam, hit, mast, dist, ammo))

 for ammo in ammoHeader:
  cod  = int(parser.get(ammo, 'cod'))
  name = parser.get(ammo, 'name')
  dam  = int(parser.get(ammo, 'dam'))
  ammo = int(parser.get(ammo, 'ammo'))
  itemList.append(Ammo(cod, name, dam, ammo))

 for armor in armorHeader:
  cod  = int(parser.get(armor, 'cod'))
  name = parser.get(armor, 'name')
  defe = int(parser.get(armor, 'def'))
  life = int(parser.get(armor, 'life'))
  itemList.append(Armor(cod, name, defe, life))

 return itemList

# ----- loading/profession ----- #
def loadProfession():
 profList = []
 parser = SafeConfigParser()
 parser.read('data/profession.info')

 for section in parser.sections():
  cod   = int(parser.get(section, 'cod'))
  name  = parser.get(section, 'name')
  bonus = eval(parser.get(section, 'bonus'))
  requi = eval(parser.get(section, 'requi'))
  profList.append(Professions(cod, name, bonus, requi))

 return profList

# ===== NPC/PC ===== #

# ----- hero ----- #
def generateHero(itemList, profList):
 attr = {'str': 0, 'dex': 0, 'int': 0, 'exp': 0}
 pool = 13
 print '\n' * 100
 print '=' * 14
 print 'GENERATIN HERO'
 print '=' * 14
 name = raw_input('Name: ')

 while pool > 0:
  print '\n' * 100
  print '=' * len(name)
  print name.upper()
  print '=' * len(name)
  print 'Attributes Score'
  print '[S]trenght    - ', attr['str']
  print '[D]exterity   - ', attr['dex']
  print '[I]nteligence - ', attr['int']
  print '[E]xpression  - ', attr['exp']
  print '-' * len(name)
  print 'Score Pool: ', pool
  choice = raw_input('_').lower()

  if choice   == 's': pool -= 1; attr['str'] += 1
  elif choice == 'd': pool -= 1; attr['dex'] += 1
  elif choice == 'i': pool -= 1; attr['int'] += 1
  elif choice == 'e': pool -= 1; attr['exp'] += 1
  else: pass

 print '\n' * 100
 print '=' * len(name)
 print name.upper()
 print '=' * len(name)
 print 'Attributes Score'
 print '[S]trenght    - ', attr['str']
 print '[D]exterity   - ', attr['dex']
 print '[I]nteligence - ', attr['int']
 print '[E]xpression  - ', attr['exp']
 print '-' * len(name)
 raw_input('press ENTER to continue!')

 print 'Choose Your Weapon'
 for item in itemList:
  if item.iType == 'weapon':
   print 'Cod: %i - Name: %s - Damage: 1..%i - Hit-Chance: %i - Mastery: %i'\
          %(item.cod, item.name, item.damage, item.hitChance, item.mastery)
  elif item.iType == 'ranged':
   print 'Cod: %i - Name: %s - Damage: 1..%i - Hit-Chance: %i - Distance: %i\
          - Mastery: %i' %(item.cod, item.name, item.damage, item.hitChance,\
          item.mastery)
 print "Select your weapon by it's COD %s!" %name
 choice = int(raw_input('_'))
 for item in itemList: 
  if item.cod == choice: weapon = item; break

 print '\n' * 10
 for item in itemList:
  if item.iType == 'armor':
   print 'Cod: %i - Name: %s - Defense: %i - Durability: %i' \
          %(item.cod, item.name, item.defense, item.life)
 print "Select your armor by it's COD %s!" %name
 choice = int(raw_input('_'))
 for item in itemList: 
  if item.cod == choice: armor = item; break

 print '\n' * 100
 print '=' * 11
 print 'Professions'
 print '=' * 11
 for prof in profList:
  print '-' * len(prof.name)
  print 'Cod:        ', prof.cod
  print 'Name:       ', prof.name
  print 'Bonus:      ', prof.bonus
  print 'Requisites: ', prof.requisites

 print "Choose your profession by it's COD %s!" %name
 choice = int(raw_input('_'))
 for prof in profList: 
  if prof.cod == choice: profession = prof; break

 hitRate = rand(1, 3) + 2
 purse = rand(0, 80) + 20

 hero = Hero(1, name, name, attr, hitRate, None, purse, profession, weapon, \
             armor, None)

 print '\n' * 100
 print '=' * len(hero.name)
 print hero.name.upper(), ', The ', hero.profession.name
 print '=' * len(hero.name)
 print 'Attributes'
 print '-' * 10
 print 'Strenght:    ', hero.attr['str']
 print 'Dexterity:   ', hero.attr['dex']
 print 'Inteligence: ', hero.attr['int']
 print 'Expression:  ', hero.attr['exp']
 print '-' * 10
 print 'Weapon: %s - Damage: 1..%i - Hit-Chance: %i - Mastery: %i' \
        %(hero.weapon.name, hero.weapon.damage, hero.weapon.hitChance, \
          hero.weapon.mastery)
 print 'Armor: %s - Defense: %i - Durability: %i' %(hero.armor.name, \
        hero.armor.defense, hero.armor.life)
 print '-' * 10
 print 'Purse: %i copper coins' %hero.purse
 raw_input()

 return hero

# ----- foe ----- #
def loadFoeList(itemList, profList):
 foeList = []
 attr = {'str': 0, 'dex': 0, 'int': 0, 'exp': 0}
 pool = 12
 while pool > 0:
  choice = rand(1, 4)
  if choice   == 1: pool -= 1; attr['str'] += 1
  elif choice == 2: pool -= 1; attr['dex'] += 1
  elif choice == 3: pool -= 1; attr['int'] += 1
  else: pool  -= 1; attr['exp'] += 1
 name = 'Man'
 hit = rand(1, 3) + 2
 weapon = 0
 while type(weapon) == 'int':
  weapon = rand(1, 5)
  for item in itemList:
   if item.cod == weapon: weapon = item; break
 foeList.append(Fighters(1, name, name, attr, hit, None, None, None, \
                weapon, None))
 return foeList

# ========== GAMING ========== #

# ----- scenes ----- #
def start(eventList, hero, foeList, itemList):
 for event in eventList:
  if event.flag == 'start': break
 while True:
  if event == None: break
  elif event.flag == 'end':    break
  elif event.flag == 'test':   eventId = testing(event, hero, foeList)
  elif event.flag == 'market': eventId = market(event, hero)
  elif event.flag == 'quest':  eventId = quest(event, questList, hero)
  elif event.flag == 'fight':  pass # combat()

  try:
   for event in eventList:
    if event.cod == eventId: break
  except:
   pass

  event = display(event)

# ----- display scenes ----- #
def display(event): 
 print '=' * len(event.alias)
 print event.alias.upper()
 print '=' * len(event.alias)
 print event.desc.replace('#', '\n')
 print '-' * len(event.alias)
 for i in range(len(event.target)):
  print i + 1, '-', event.target[i]#.name
 print '0 - Quit'
 choice = raw_input('_').lower()
 if choice == '0': return None
 else:
  choice = int(choice) - 1
  return event.target[choice]

# ----- tests ----- #
def testing(event, hero, foeList):
 for foe in foeList:
  if event.prey == foe.name:
    event.prey = foe
    event.pred = hero
  elif event.pred == foe.name:
    event.prey = hero
    event.pred = foe

 preyDice = rand(1, 20)
 predDice = rand(1, 20)

 if predDice - preyDice >= 10:   return event.target['epicWin']
 elif preyDice - predDice >= 10: return event.target['epicFail']
 else:
  if event.pred.attr[aim] + predDice >= event.prey.luck + preyDice: 
   return event.target['win']
  else: return event.target['lose']

def market(event, hero):
 if hero.purse >= event.aim:
  hero.purse -= event.aim
  return event.target['win']
 else: return event.target['lose']

# ----- quests ----- #
def quests(event, questList, hero):
 condition = event.cond.keys()[0]
 for quest in questList:
  if quest.name == cond and quest.status == event.cond[cond]:
   return event.result['yes']
 return result['no']

# ========== MAIN ========== #

def main():
 while True:
  print '\n' * 100
  print '=' * 11
  print 'MAIN MENU'
  print '=' * 11
  print '[N] - New Game'
  print '[L] - Load Game'
  print '[Q] - Quit'
  print '-' * 11
  choice = raw_input('_').lower()
  if choice   == 'n': newGame()
  elif choice == 'l': pass
  elif choice == 'q': break
  else: pass

if __name__ == '__main__': main()
