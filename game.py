"""SILK ROAD"""

import os, time, random

### LIB
## VARIABLES
health = 1
food = 1 # this variable = the number of days you can last with the amount of food you have
location = "Genève"
coins = 0
languages = []
inv = []
day_n = 0
b = "b"
d = "d"

## CLASSES

## FUNCS

# useful terminal functions
def clear():
    os.system("clear")
    #os.system("CLS")

def wait(n):
    time.sleep(n)

def load(t, l=10, task=""):
    clear()
    i = 0
    while i <=l:
        print(f"[{i*"■"}{(l-i)*" "}]")
        print(task)
        i+=1
        wait(t)
        clear()

def pe():
  input("\nPress Enter to continue/")

def q():
    choose("Are you sure you want to quit?", [quit, pe], ["Yes", "No"])

def is_int(s):
    return True if s in "123456789" else False

# show_ functions
def show_inv():
    print("Inventory")
    print("=========")
    for element in inv:
        print(f"{element[0]} x{element[1]}")
    print("")
    pe()

def show_loc(now = False):
    print(f"You are currently in {location}.")
    pe()

def show_food(now=False, pressenter=True):
    if now:
        if food == 0:
            print("You now have no food!")
        elif food == 1:
            print("You now have enough food to last you 1 day")
        else:
            print(f"You now have enough food to last you {food} days")
    else:
        if food == 0:
            print("You have no food!")
        elif food == 1:
            print("You have enough food to last you 1 day")
        else:
            print(f"You have enough food to last you {food} days")
    if pressenter: pe()

def show_health(now=False, pressenter=True):
    if now == True: print(f"Your health level is now {health}")
    else: print(f"Your health level is currently {health}")
    if pressenter: pe()

def show_day(pressenter=True):
    print(f"Day {day_n}")
    if pressenter: pe()

# other library functions

def choose(msg, passages, passages_name, clearscreen=True):
    if clearscreen: 
        clear()

    print(msg + "\n")
    i = 1
    for passage in passages_name:
        print(f"{i} : {passage}")
        i += 1
    c = input("> ")
    if is_int(c) and int(c) >= 1 and int(c) < i:
        print()
        passages[int(c)-1]()
    elif c == "inv":
        show_inv()
        choose(msg, passages, passages_name)
    elif c == "loc":
        show_loc()
        choose(msg, passages, passages_name)
    elif c == "food":
        show_food()
        choose(msg, passages, passages_name)
    elif c == "quit":
        q()
    else:
        choose(msg, passages, passages_name)

# game functions (not passages)
def die(cause="none"):
    if cause == "none":
        print("You died!")
    elif cause == "hunger":
        print("You starved to death!")
    pe()
    quit()

def checkhealth(cause="none"):
    if health > 0:
        pass
    else:
        die(cause)

def eat(t=b):
    global food
    if food >= 0.5:
        food -= 0.5
        if t == "b":
            print("You eat breakfast, your health stays the same")
            show_food(True, False)
            show_health()
        elif t == "d":
            print("You eat dinner, your health stays the same")
            show_food(True, False)
            show_health()
    else:
        if t == "b": print("You don't have any food! You cannot eat breakfast")
        elif t == "d": print("You don't have any food! You cannot eat dinner")
        skipameal()    

def eat_dinner():
    eat(d)

def skipameal():
    global health
    print("You skip a meal, but your health level decreases by 1...")
    health -= 1
    show_health(True, False)
    checkhealth("hunger")

def day():
    clear()
    global day_n
    day_n += 1
    show_day(False)
    print("The sun rises, and you wake up...")
    # RANDOM EVENT HERE
    choose("Do you want to eat breakfast?", [eat, skipameal], ["Let's eat breakfast!","I can skip a meal..."], False)

def night():
    clear()
    print("The sun sets...")
    choose("Do you want to eat dinner?", [eat_dinner, skipameal], ["Let's eat dinner!", "I can skip a meal..."], False)
    print("\nYou go to sleep...")

# Maybe we should create character aptitudes and specialties like intelligence, strength

# You can start the game as a venician merchant, a portugese merchant, a persian merchant, a chinese merchant

### LORE
"""Your father recently passed away, and you are his only child left. You have to keep the family business on, and trade spices, silk or ores on the Silk road
You have to learn many skills (and languages) for this, and make decisions (such as where to start the game, get there by boat or by road)
Your goal, is to become profitable and make your family's name remembered. But many obstacles are on the way to silk, and you will need to interact with people if you want it to work!"""

## MECHANICS
# Meeting random people, getting food. Day-by-day game (that way we can have a main loop).
# Some passages end days (for example getting somewhere or trekking), some don't (for example meeting people doesn't make the day end), some end your life and you have to start over!

## PASSAGES DEFINITIONS
