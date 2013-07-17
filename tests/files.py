#!/usr/bin/env python
#-*- coding: utf-8 -*-

from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
from scenes import *

eventList = []
scenesList = []
testList = []
scCab = ['sc1', 'sc2']
tsCab = ['ts1']

parser.read('info')

for sc in scCab:
 cod = parser.get(sc, 'cod')
 flag = parser.get(sc, 'flag')
 name = parser.get(sc, 'name')
 alias = parser.get(sc, 'alias')
 description = parser.get(sc, 'description')
 target = eval(parser.get(sc, 'target'))
 scenesList.append(Show(cod, flag, name, alias, description, target))

for ts in tsCab:
 cod = parser.get(ts, 'cod')
 flag = parser.get(ts, 'flag')
 prey = parser.get(ts, 'prey')
 predator = parser.get(ts, 'predator')
 target = eval(parser.get(ts, 'target'))
 aim = parser.get(ts, 'aim')
 testList.append(Tests(cod, flag, prey, predator, target, aim))

cod = parser.get('end', 'cod')
flag = parser.get('end', 'flag')
event = Events(cod, flag)

raw_input('terminado de ler o arquivo info')
print 'segue a lista de eventos/cenas:'
for scene in scenesList:
  print '---'
  print 'name: ', scene.name
  print 'flag: ', scene.flag
  print 'desc: ', scene.description
  print 'targ: ', scene.target
  print 'tartType: ', type(scene.target)

raw_input('-----')
print 'segue a lista de eventos/test:'
for test in testList:
  print '---'
  print 'prey: ', test.prey
  print 'pred: ', test.predator
  print 'aim: ', test.aim
  print 'targ: ', test.target
  print 'targType: ', type(test.target)

raw_input('-----')
print 'finalizador: '
print 'cod: ', event.cod
print 'flag: ', event.flag

raw_input('Se chegamos até aqui é porque tudo correu bem! Duvido.')
