#!/usr/bin/env python
#-*- coding: utf-8

from items import *
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
itemList = []

parser.read('items.info')

for section in parser.sections():
 cod  = int(parser.get(section, 'cod'))
 name = parser.get(section, 'name')
 if section[0:2] == 'it': 
  itemList.append(Items(cod, name)) 
  continue
 if section[0:2] == 'wp' or section[0:2] == 'rw':
  dam  = int(parser.get(section, 'dam'))
  hit  = int(parser.get(section, 'hit'))
  mast = int(parser.get(section, 'mast'))
  if section[0:2] == 'wp': 
   itemList.append(Weapons(cod, name, dam, hit, mast))
   continue
  if section[0:2] == 'rw': 
   dist = int(parser.get(section, 'dist'))
   ammo = parser.get(section, 'ammo')
   itemList.append(RangeWeapons(cod, name, dam, hit, mast, dist, ammo))
   continue
 if section[0:2] == 'am':
  dam  = int(parser.get(section, 'dam'))
  ammo = parser.get(section, 'ammo')
  itemList.append(Ammo(cod, name, dam, hit))
  continue
 if section[0:2] == 'ar':
  defe = int(parser.get(section, 'def'))
  life = int(parser.get(section, 'life'))
  itemList.append(Armor(cod, name, defe, life))
  continue

for item in itemList:
 print 'Name: ', item.name
 print 'Type: ', item.iType
 if item.iType == 'weapon' or item.iType == 'ranged':
  print 'Damage:    ', item.damage
  print 'HitChance: ', item.hitChance
  print 'Mastery:   ', item.mastery
 if item.iType == 'ranged':
  print 'Distance:  ', item.distance
  print 'Ammo Type: ', item.ammoType
 if item.iType == 'ammo':
  print 'Damage Inc: ', item.damInc
  print 'Type:       ', item.ammoType
 if item.iType == 'armor':
  print 'Defense:    ', item.defense
  print 'Durability: ', item.life
 raw_input()
