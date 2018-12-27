"""This file describes the heroic adventurer Korth Jhank.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.9.2"

name = "Korth Jhank"
player_name = "Larissa"

# Be sure to list Primary class first
classes = ['Warlock']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Hexblade Patron"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Urban Bounty Hunter"
race = "Lizardfolk"
alignment = "Chaotic Neutral"

xp = 0
hp_max = 22
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 14
dexterity = 12
constitution = 15
intelligence = 8
wisdom = 11
charisma = 15

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('deception', 'intimidation', 'investigation', 'persuasion', 'stealth', 'survival')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = []

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ["Devil's Sight", "Thief of Five Fates"]

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ('Pact of the Blade',)

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ()

# Proficiencies and languages
languages = """Common, Draconic"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Maul", "Bite"]  # Example: ('shortsword', 'longsword')
magic_items = []  # Example: ('ring of protection',)
armor = "Leather armor"  # Eg "light leather armor"
shield = "None"  # Eg "shield"

equipment = """dagger (stabby dwarf), magic ash, arcane focus (orb),
dungeoneers pack"""

attacks_and_spellcasting = """"""

# List of known spells
# Example: spells = ('magic missile', 'mage armor')
spells = ("Bane", "Chill Touch", "Hellish Rebuke", "Eldritch Blast", "Expeditious Retreat", "Shatter", "Spider Climb")

# Which spells have been prepared (not including cantrips)
spells_prepared = ("Bane", "Chill Touch", "Hellish Rebuke", "Eldritch Blast", "Expeditious Retreat", "Shatter", "Spider Climb")

# Backstory
# Describe your backstory here
personality_traits = """Keep calm.

Don't let emotion control me.

very calculating.
"""

ideals = """
The world is how the world is
"""

bonds = """
Paying off old debt (to patron)
"""

flaws = """
If there is a plan, I forget/ignore it.
"""

features_and_traits = """
"""
