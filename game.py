"""SILK ROAD"""

import os, time, random

### LIB
## VARIABLES
health = 100
coins = 0
languages = []
inv = []
day = 0
# Maybe we should create character aptitudes and specialties like intelligence, strength

# You can start the game as a venician merchant, a portuguese merchant, a persian merchant, a chinese merchant

### STORY/NOTES
"""Your father recently passed away, and you are his only child left. You have to keep the family business on, and trade spices, silk or ores on the Silk road
You have to learn many skills (and languages) for this, and make decisions (such as where to start the game, get there by boat or by road)
Your goal, is to become profitable and make your family's name remembered. But many obstacles are on the way to silk, and you will need to interact with people if you want it to work!"""

## MECHANICS
# Meeting random people, getting food. Day-by-day game (that way we can have a main loop).
# Some passages end days (for example getting somewhere or trekking), some don't (for example meeting people doesn't make the day end), some end your life and you have to start over!