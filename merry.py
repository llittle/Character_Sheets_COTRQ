"""This file describes the heroic adventurer Merry Skipstep.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.0"

name = "Merry Skipstep"
player_name = "Josh"

# Be sure to list Primary class first
classes = ['Rogue', 'Sorceror']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [2, 1]  # ex: [10] or [3, 2]
subclasses = ['', "Wild Magic"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Charlatan"
race = "Lightfoot Halfling"
alignment = "Chaotic Good"

xp = 0
hp_max = 19
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 14
constitution = 10
intelligence = 12
wisdom = 11
charisma = 16

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('acrobatics', 'athletics', 'deception', 'persuasion', 'sleight of hand', 'stealth')

# Named features / feats that aren't part of your classes,
# race, or background. Also include Eldritch Invocations.
# Example:
# features = ('Tavern Brawler',)  # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, Halfling"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Rapier", "Shortsword", "Dagger"] # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
armor = "Elven Chain"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """Fine clothes. Disguise kit. Thieves' tools. Bag of knickknacks. 
Backpack. Bedroll. Mess kit. Tinderbox. 10x torches. 10x rations.
waterskins. 50' rope. 2x daggers."""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Burning Hands", "Expeditious Retreat", "Prestidigitation",
          "Mage Hand", "Poison Spray", "Shocking Grasp")

# Which spells have been prepared (not including cantrips)
spells_prepared = ("Burning Hands", "Expeditious Retreat", "Prestidigitation",
                   "Mage Hand", "Poison Spray", "Shocking Grasp")

# Backstory
# Describe your backstory here
personality_traits = """
Wanderlust, rebel, dedicated, sarcastic.
"""

ideals = """
Life is too short not to enjoy it.

No one tells me what to do.
"""

bonds = """
Isolated from family

Home among friends
"""

flaws = """
Lack of seriousness, tomfoolery.

Difficulty being honest.
"""

features_and_traits = """
*Lucky: reroll 1 on d20

*Brave: Adv. vs. frightened

*Halfling Nimbleness: Move through size+1

*Naturally Stealthy: Hide behind size+1

*False Identity: handful of shallow cons

*Expertise: Acrobatics, Deception

*Sneak Attack: 1d6 if ADV or flanking

*Thieves' Cant

*Cunning Action: free bonus action (Hide, Dash, Disengage)

*Sorcerous Origin: Wild Magic

-Wild Surge (1 on d20)

-Tides of Chaos (1 adv / long rest)

*Personas

-Zoltan, foremost seer of other worlds and planes (ancient tome)

-Hograth, left hand of Tyr (old hat)

-Soleas, animal whisperer (dog carving)

-Axel, Pyros Sorceror Supreme III (fine clothes)

-Harrison Ford, kessel run in 12 pc (magic die)
"""