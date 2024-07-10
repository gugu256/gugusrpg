"""SILK ROAD"""

import os, time, random

### LIB
## VARIABLES
health = 100
location = "Genève"
coins = 0
languages = []
inv = []
day = 0

## CLASSES

## FUNCS
def is_int(s):
    return True if s in "123456789" else False

def show_inv():
    print(inv)

def show_loc(now = False):
    print(f"You are in {location}")

def choose(passages, passages_name):
    i = 1
    for passage in passages_name:
        print(f"{i} : {passage}")
        i += 1
    c = input("> ")
    if is_int(c):
        passages[int(c)-1]()
    elif c == "inv":
        show_inv()
        choose(passages, passages_name)
    elif c == "loc":
        show_loc()
        choose(passages, passages_name)
    elif c == "quit":
        #q()
        quit()
    else:
        choose(passages, passages_name)

## PASSAGES DEFINITIONS


# Maybe we should create character aptitudes and specialties like intelligence, strength

# You can start the game as a venician merchant, a portuguese merchant, a persian merchant, a chinese merchant

### STORY/NOTES
"""Your father recently passed away, and you are his only child left. You have to keep the family business on, and trade spices, silk or ores on the Silk road
You have to learn many skills (and languages) for this, and make decisions (such as where to start the game, get there by boat or by road)
Your goal, is to become profitable and make your family's name remembered. But many obstacles are on the way to silk, and you will need to interact with people if you want it to work!"""

## MECHANICS
# Meeting random people, getting food. Day-by-day game (that way we can have a main loop).
# Some passages end days (for example getting somewhere or trekking), some don't (for example meeting people doesn't make the day end), some end your life and you have to start over!