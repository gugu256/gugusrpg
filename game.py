"""SILK ROAD"""

import os, time, random

### LIB
## VARIABLES
health = 100
food = 1 # this variable = the number of days you can last with the amount of food you have
location = "Venice"
coins = 0
languages = []
inv = []
day_n = 0
b = "b" # b and d are useful for the beakfast and dinner funcs
d = "d"
ate_least_meal = False

## CLASSES

## FUNCS

def do_nothing():
    pass

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

def pe(msg=""):
    if msg=="":
        input("\nPress Enter to continue/")
    else:
        input(f"\nPress Enter {msg}/")

def q():
    quit()
    
def is_int(s):
    return True if s in "123456789" and s != "" else False

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
    if now == True: print(f"Your health level is now {health}/100")
    else: print(f"Your health level is currently {health}/100")
    if pressenter: pe()

def show_day(pressenter=True):
    print(f"Day {day_n}")
    if pressenter: pe()

# other library functions

help_message =     """
This game is a text-based game made of passages.
You have to make a choice at every passage.
At any moment, you can type one of these commands instead of inputting your choice:

inv: see what's inside your inventory
loc: see your current location
food: see how much food you have left
help: see this message again
quit: quit the game

That's it! Nothing more
    """

def h_title():
    clear()
    print("How to play")
    print("===========\n")
    print(help_message)
    pe("if you got it")
    title()

def h():
    clear()
    print("How to play")
    print("===========\n")
    print(help_message)
    pe("if you got it")

def choose(msg, passages, passages_name, clearscreen=True, passage_title=""):
    if clearscreen: 
        clear()

    if passage_title != "":
        print(passage_title)
        print("="*len(passage_title) + "\n")
    
    print(msg + "\n") if msg != "" else do_nothing()
    i = 1
    for passage in passages_name:
        print(f"{i} : {passage}")
        i += 1
    c = input("> ")
    if is_int(c) and int(c) >= 1 and int(c) < i:
        print()
        passages[int(c)-1]()
    elif c == "inv":
        clear()
        show_inv()
        choose(msg, passages, passages_name, True, passage_title)
    elif c == "loc":
        clear()
        show_loc()
        choose(msg, passages, passages_name, True, passage_title)
    elif c == "food":
        clear()
        show_food()
        choose(msg, passages, passages_name, True, passage_title)
    elif c == "help":
        h()
        choose(msg, passages, passages_name, True, passage_title)
    elif c == "quit":
        q()
    else:
        choose(msg, passages, passages_name, clearscreen, passage_title)
   
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
    global ate_last_meal
    if food >= 0.5:
        food -= 0.5
        ate_last_meal = True
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
    global ate_last_meal
    print("You skip a meal, but your health level decreases by 1...")
    health -= 1
    ate_last_meal = False
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
def first_day():
    day()

def title():
    choose("", [first_day, h_title, q], ["Start Game", "How to play",  "Quit"], True,  "SILK ROAD: THE GAME")
    
title()
