PAR = Python Adventure RPG
==========================

A simple text-styled game inspired by the classics adventure fighting fantasy game from Ian Livingstone and many others.<br />
It started when I began writing AZARIA, a simillar project with the story setted in the eponymous city but the project grew so complex in a way that I was unable to add the initial features I've planned for it, let alone implementing anything in the future.<br />
Instead of trying to fix it, it was decided to start from zero, re-using part of the code and re-writing the Objects, in a way that would be more generic and easier to write new stories.


##DONE List
The main structure is still in development but the part which will load the scenes, tests and quests are done. This same area was the source of many problems in the previous incarnation as AZARIA.<br />
Also, the config-style file for loading the events (scenes, quests, tests..) is read to use with a detailed description of the accepted values.
The config-styled files for scens, items and professions are ready. The scenes manipulation in main.py is due to upgrade in order to be dynamic, which will turn data/info.cfg useless.

##YET to come
- <i>The quests handle inside the game is a Work-in-Progress.</i> 0.1301.01

###FAR future
- Fighting
- Non-combat solutions
- Hidden options
- Quest-based options
- Screen, using 'curses'

####WORK in progress
- Fill-up the events.info
- Fill-up items in events.info
- Fill-up professions in profession.info
- Character Generation is working but not completed (0.1307.16)
- Profession Loading (0.1307.16)
- Items Loading (0.1307.16)
- Foe Generation (0.1307.16)

##Files
- main.py	[0.1307.27] : the main game
- characters.py [0.1212.31] : character related classes (NPC, Fighters, Hero)
- items.py	[0.1212.31] : item related classes (Items, Weapons, RangedWeapons, Ammo, Armor)
- scenes.py	[0.1307.24] : events related classes (Scenes, Show, Tests, Quests)
- data
 - events.info	[0.1307.27] : data file with the content for the events
 - info.cfg	[0.1307.22] : configurations used to generate events (number of events per type)
 - items.info   [0.1301.01] : data file with the content for the items
 - profession.info [0.1301.01] : data file with the content for professions
- README.md: this file

##Updates:
- 0.1307.27
 - events.info: removed entries related to 'end' event. Used target = [] instead.
 - main.py: update code to comply with changes in 'events.info'.
- 0.1307.24
 - updating scenes handle. wip.
 - events.info: update 'end' event.
- 0.1307.22
 - corrected errors loading SCENES in 'main.py', 'scenes.py'.
 - updated 'info.cfg'.
 - scenes.py: updated class Events to Scenes.
- 0.1307.16
 - corrected bunch of errors regarding parser and classes in files 'main.py', 'characters.py', 'scenes.py', 'data/profession.info'.
 - main.py: modified behaviour of loadEvents().
- 0.1301.01
 - main.py: finalized foe generation. Updated loading functions. Completed quests test.
 - scenes.py: added 'alias' field to Tests class.
 - data/events.info: start to fill-up.
 - data/profession.info: created file with some content. (wanderer, farmer).
 - data/items.info: created file with some content. (spear, sword, leather armor).
- 0.1212.31
 - main.py: finalized item and profession loading and create hero generation.
 - characters.py: link the Professions bonus to the NPC attributes.
 - items.py: added item type (iType) to all classes.
- 0.1212.30
 - Initial work. All the files were created

##Copywrite
