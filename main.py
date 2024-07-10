import os, time, random

# -- VARIABLES --

#lives = 3
coins = 0
current_passage = ""
hamPrice = 0
oldmanAlive = True

passages = {
  "1": "start()",
  "2":  "stayInsideHome()",
  "3": "getOutsideHome()",
  "4": "helpOldMan()",
  "5": "dontHelpOldMan()",
  "6": "goHomeOldMan()",
  "7": "askWhoIsBack()",
  "8": "askWhereKyleCity()",
  "9": "RoRoCity()",
  "10": "downtownRoRo()",
  "11": "shopRoRo()",
  "12": "bankRoRo()",
  "13": "leaveRoRo()",
  "14": "NNR()",
  "15": "SNR()",
  "16": "shornayTown()",
  "17": "ShornayTown()",
  "18": "oldWoman()",
  "19": "downtownShornay()"
}

inv = ["", "", ""]

def invEmpty():
  if inv == ["", "", ""] :
    return True
  else:
    return False

chap1map = [
  "                 =-                                  -=:                        ",
  "                  .*                                *.                          ",
  "                   .+-                             +.                           ",
  "                     :+                            *                            ",
  "                       +.           1             -=                            ",
  "                        *.                       =-                             ",
  "                         +.                   :=-                               ",
  "                          ==:.               +:     =10==: 2                      ",
  "                             :=-            +.     +:                             ",
  "                               -=          *     .*.                              ",
  "                                .+.       *.    :+                                ",
  "                                  *      :=    == 3                               ",
  "                                  =:     +    *:                                  ",
  "                                   *   :+   .*.                                   ",
  "                      :.            :--.    4                                     ",
  "                   +#%@@-                  =                                      ",
  "                 .=@@@@@@*                11                                      ",
  "              :*#@@@@@@@@@+              ##                                       ",
  "        9 --> #@@@@@@%@###=             #+:                                       ",
  "             -@@@@@@@@@.@@@@@@          5                                         ",
  "                @@@@@@@@@@@            ##                                          ",
  "                  @@@@@@@              =#                                            ",
  "                    @@@  \\           #=                                          ",
  "                      |   \\:--8----==                                           ",
  "                      |          .===                                           ",
  "                    8 +-       .-6=:                                              ",
  "                      +-    -==-                                                  ",
  "                       \\\\==-.                                                     ",
  "                      7.                                                         ",
  "                                                                                ",
  "LEGEND : ",
  "1 : Shornay Sea\n2 : Glo Cave\n3 : Sea Road\n4 : Shornay Town\n5 : RoRo City\n6 : South National Road\n7 : Kyle City\n8 : Forest Road\n9 : Corrow Forest\n10 : Death Road\n11 : North National Road"
  
]

# --

# -- FONCTIONS UTILES DU TERMINAL --

def clear():
  os.system("clear")
  #os.system("CLS")

def wait(n):
  time.sleep(n)

def load(t):
  clear()
  print("|=         |")
  wait(t)
  clear()
  print("|==        |")
  wait(t)
  clear()
  print("|===       |")
  wait(t)
  clear()
  print("|====      |")
  wait(t)
  clear()
  print("|=====     |")
  wait(t)
  clear()
  print("|======    |")
  wait(t)
  clear()
  print("|=======   |")
  wait(t)
  clear()
  print("|========  |")
  wait(t)
  clear()
  print("|========= |")
  wait(t)
  clear()
  print("|==========|")


def pressenter():
  input("Press enter to continue : ")

# --

# -- FONCTIONS UTILES DE JEU --

def Quit():
  input("Press enter to quit : ")
  quit()

def Help():
  print("How to play")
  print("The game is made of passages.\nAt each passage, you have a choice to make.\nTo make a choice, type 1 or 2 then press Enter.\nAt any moment, you can type 'inv' instead of 1 or 2 to see what's in your inventory\nYou can also type 'quit' instead of 1 or 2 to quit the game,\nand that's it! Nothing more!")
  pressenter()
  main()

def die():
  print("You died !")
  input("Press enter to start over : ")
  main()

def setCoins(t, n): #cette fonction sert a changer l'argent
  global coins
  if t == "+":
    coins += n
    print("You've earned", n, "coins")
    print("You now have", coins, "coins")
    return
  elif t == "-":
    coins -= n
    print("You've lost", n, "coins")
    print("You now have", coins, "coins")
    return
  elif t == "to":
    print("You now have", n, "coins")
    coins = n
    return

def setPassage(p, n): 
  clear()
  global current_passage
  current_passage = n
  print("Password of your current passage :", p)
  t = ""
  for i in range(-1, len("Password of your current passage :"+str(p))):
    t += "-"
  print(t)

def inventory():
  clear()
  print("INVENTORY")
  for i in range(0, len(inv)):
    print("Slot", (i+1),": ", inv[i])
  pressenter()
  eval(current_passage)

def insertInv(item):
  global inv
  if invEmpty():
    inv[0] = item
  elif inv[0] != "":
    if inv[1] == "":
      inv[1] = item
    elif inv[1] != "":
      if inv[2] != "":
        print("Your inventory is full !")
        pressenter()
        eval(current_passage)
      else:
        inv[2] = item

def removeInv(mode, item, verb):
  global inv
  m = mode
  i = item
  v = verb
  inventory()
  if mode == "i":
    slot = int(input("Enter the slot of the object you want to", verb, "\n> ")) - 1
    if inv[slot] == "":
      print("This slot is empty !")
      input("Press enter to select the right slot : ")
      removeInv(m, i, v)
    elif slot not in [0, 1, 2]:
      print("This slot does not exist !")
      input("Press enter to select the right slot : ")
      removeInv(m, i, v)
    elif item not in inv:
      print("You don't have this item in your inventory !")
      pressenter()
      eval(current_passage)
    elif inv[slot] != item:
      print("This slot does not contains the right item !")
      cond("Try again", "Quit", f"removeInv({m}, {i}, {v}", current_passage)
    else:
      inv[slot] = ""
  else:
    slot = int(input("Enter the slot of the object you want to", verb, "\n> ")) - 1
    if inv[slot] == "":
      print("This slot is empty !")
      input("Press enter to select the right slot : ")
      removeInv(m, i, v)
    elif slot not in [0, 1, 2]:
      print("This slot does not exist !")
      input("Press enter to select the right slot : ")
      removeInv(m, i, v)
    else:
      inv[slot] = ""

def cond(c1, c2, f1, f2):
  print("1 :", c1, "\n2 :", c2)
  c = input("> ").lower()
  if c == "1":
    eval(f1)
  elif "q" in c:
    Quit()
  elif "inv" in c:
    inventory()
  else:
    eval(f2)

def cond3(c1, c2, c3, f1, f2, f3):
  print("1 :", c1, "\n2 :", c2, "\n3 :", c3)
  c = input("> ").lower()
  if "q" in c:
    Quit()
  elif "inv" in c:
    inventory()
  elif c == "1":
    eval(f1)
  elif c == "2":
    eval(f2)
  else:
    eval(f3)

def cond5(c1, c2, c3, c4, c5, f1, f2, f3, f4, f5):
  print("1 :", c1, "\n2 :", c2, "\n3 :", c3, "\n4 :", c4, "\n5 :", c5)
  c = input("> ").lower()
  if "q" in c:
    Quit()
  elif "inv" in c:
    inventory()
  elif c == "1":
    eval(f1)
  elif c == "2":
    eval(f2)
  elif c == "3":
    eval(f3)
  elif c == "4":
    eval(f4)
  else:
    eval(f5)

# --

# -- NOTES SUR LE LORE : 
#  - KYLE : 
#     Kyle (juste Kyle) est le mechant du jeu (ou au moins au Chapter 1). C'est un peu un savant fou qui est deteste par tout le monde
#     Il est l'inventeur du DUCK (Destructive Unbelievable Cannon of Kyle), une arme surpuissante
#  - THE OLD MAN :
#      C'est un personnage du debut qui a l'air secondaire, mais qui est en fait un homme de Kyle.
#      Il tue le joueur au debut du jeu si le joueur accepte de l'aider
# --


# -- FONCTIONS DES PASSAGES -- Les nouveaux passages doivent etre rajoutes en HAUT
# - Structure d'un passage : 
#   def nomDuPassage():
#     setPassage(numeroDuPassage, "nomDuPassage()")
#     print("Texte du passage")
#     cond("Premier choix possible", "Deuxieme choix possible", "fonctionDuPremierChoix()", "fonctionDuDeuxiemeChoix()")
# + NE PAS OUBLIER DE RAJOUTER LE PASSWORD DU PASSAGE DANS LE DICT PLUS EN HAUT
# --

# -- KYLE CITY --

def leaveKyleCity():
  pass # a coder

# --

# -- SHORNAY TOWN --

def shornayShop():
  pass

def shornayBank():
  pass

def downtownShornay():
  setPassage(19, "downtownShornay()")
  print("You're in the Shornay Town's Downtown")
  cond3("Go to the Shornay's Shop", "Go to the Shornay's Bank", "shornayShop()", "shornayBank()")

def leaveShornayTown():
  setPassage(16, "shornayTown()")
  print("LOCATION : SHORNAY TOWN\n" + ("-" * len("LOCATION : SHORNAY TOWN")))
  print("You're in the front of the Shornay Town's gate..")
  cond3("Enter Shornay Town", "Walk on the North National Road", "Walk on the sea road", "ShornayTown()", "NNR('shornay')", "seaRoad()")

def ShornayTown():
  setPassage(17, "ShornayTown()")
  print("You arrive in Shornay Town")
  print("You see a sign saying : \"WELCOME TO SHORNNAY TOWN, THE SEA WONDER\"")
  wait(1)
  print("You see an old, suspicious and weird woman sitting on a bench looking at you straight in the eyes")
  cond("Go Downtown", "Get out of this town", "downtownShornay()", "leaveShornayTown()")

# --

# -- ROUTES --

def seaRoad():
  pass

def NNR(frm):
  global oldmanAlive
  setPassage(14, "NNR()")
  print("LOCATION : NORTH NATIONAL ROAD\n" + ("-" * len("LOCATION : NORTH NATIONAL ROAD")))
  if oldmanAlive:
    print("You walk on the North National Road.\nSuddenly, you see THE old man, he tells you :\n\"Hello young person, Can I see what's in your inventory ?\"\nYou simply answer \"Yes sir\"..")
    wait(1)
    if "Calming Plants" in inv:
      print("The old man tells you  \"FINALLY! I finally found someone who has calming plants !\nI'm so happy !\"")
      print("He INSTANTLY takes your calming plants")
      if inv[0] == "Calming Plants":
        inv[0] = ""
      elif inv[1] == "Calming Plants":
        inv[1] = ""
      elif inv[2] == "Calming Plants":
        inv[2] = ""
      oldmanAlive = False
    elif random.randint(1, 3) == 2:
      print("The old man tells you : \"AHH ! YOU DON'T HAVE CALMING PLANTS ! I'M GONNA KILL YOU !\"")
      wait(2)
      print("Then he pulls out his DUCK (Destructive Unbelievable Cannon of Kyle) and INSTANTLY kills you")
      die()
    else:
      print("The old man tells you : \"AHH ! YOU DON'T HAVE WHAT I WANT... THE NEXT TIME I SEE YOU, I KILL YOU\"")
  input("Press enter to walk : ")
  wait(1.5)
  load(0.5)
  if frm == "roro":
    leaveShornayTown()
  else:
    leaveRoRo()

def SNR(frm):
  global oldmanAlive
  setPassage(15, "SNR()")
  print("LOCATION : SOUTH NATIONAL ROAD\n" + ("-" * len("LOCATION : SOUTH NATIONAL ROAD")))
  if oldmanAlive:
    print("You walk on the South National Road.\nSuddenly, you see THE old man, he tells you :\n\"Hello young person, Can I see what's in your inventory ?\"\nYou simply answer \"Yes sir\"..")
    wait(1)
    if "Calming Plants" in inv:
      print("The old man tells you  \"FINALLY! I finally found someone who has calming plants !\nI'm so happy !\"")
      print("He INSTANTLY takes your calming plants")
      if inv[0] == "Calming Plants":
        inv[0] = ""
      elif inv[1] == "Calming Plants":
        inv[1] = ""
      elif inv[2] == "Calming Plants":
        inv[2] = ""
      oldmanAlive = False
    elif random.randint(1, 3) == 2:
      print("The old man tells you : \"AHH ! YOU DON'T HAVE CALMING PLANTS ! I'M GONNA KILL YOU !\"")
      wait(2)
      print("Then he pulls out his DUCK (Destructive Unbelievable Cannon of Kyle) and INSTANTLY kills you")
      die()
    else:
      print("The old man tells you : \"AHH ! YOU DON'T HAVE WHAT I WANT... THE NEXT TIME I SEE YOU, I KILL YOU\"")
  input("Press enter to walk : ")
  wait(1.5)
  load(0.5)
  if frm == "kyleCity":
    leaveRoRo()
  else:
    leaveKyleCity()

# --

# -- FONCTIONS A RORO CITY --

def buyHam():
  if coins <= 0:
    print("You don't have any money !")
    input("Press enter to leave the shop : ")
    downtownRoRo()
  else:
    print(f"The old lady tells you : \"Each ham costs {hamPrice} coins\"")
    if coins < hamPrice:
      print("But wait a minute, you only have", coins, "\ncoins and it costs", hamPrice, "coins to buy 1 ham") 
      input("Press enter to get out of the shop : ")
      downtownRoRo()
    else:
      print("You've bought RoRo's Ham for", hamPrice, "!")
      setCoins("-", hamPrice)
      insertInv("RoRo's Ham")
      input("Press enter to quit the shop : ")
      downtownRoRo()
  
def mapRoRo():
  clear()
  for i in range(0, len(chap1map)):
    print(chap1map[i])
  input("Press enter to stop looking at the map : ")
  RoRoCity()
  
def shopRoRo():
  setPassage(11, "shopRoRo()")
  print("RoRo's Shop")
  print("You enter the RoRo City's shop.\nAt the counter, you see an old lady. She tells you\n\"We only sell RoRo's Ham Here.\"")
  cond("Buy RoRo's Ham", "Leave the shop", "buyHam()", "downtownRoRo()")
  
def bankRoRo():
  setPassage(12, "bankRoRo()")
  print("RoRo's Bank")
  print("You currently have", coins, "coins.")
  print("Your inventory contains : ")
  for i in range(0, len(inv)):
    print("Slot", (i+1),": ", inv[i])
  input("Press enter to leave the bank : ")
  downtownRoRo()
  
def downtownRoRo():
  setPassage(10, "downtownRoRo()")
  print("You arrive in RoRo City's downtown")
  cond3("Go to the shop", "Go to the bank", "Leave RoRo City's downtown", "shopRoRo()", "bankRoRo()", "RoRoCity()")

def leaveRoRo():
  setPassage(13, "leaveRoRo()")
  print("You are in front of the RoRo City's Gate")
  cond3("Enter RoRo City", "Go on the North National Road", "Go on the South National Road", "RoRoCity()", "NNR('roro')", "SNR('roro')")

def RoRoCity():
  setPassage(9, "RoRoCity()")
  print("You see a sign saying \"WELCOME TO RORO CITY, THE BEST CITY EVER\"")
  cond3("Go downtown", "See the public map", "Leave RoRo City", "downtownRoRo()", "mapRoRo()", "leaveRoRo()")
   
def askWhereKyleCity():
  setPassage(8, "askWhereKyleCity()")
  print("The Guy says to you : \"The city for his company is called Kyle City\nTo find it, walk towards the southwest on the South National Road.\nBut I don't think you want to go there anyways !\"")
  input("Press enter to end this conversation and go downtown : ")
  RoRoCity()

def dontCare():
  print("You decide to not care")
  wait(2)
  RoRoCity()

def askWhoIsBack():
  setPassage(7, "askWhoIsBack()")
  print("The guy tells you : \"Kyle is back !\" ")
  cond("Where is this city ?", "Waw. That's insane. I don't give a f*ck actually.",  "askWhereKyleCity()", "dontCare()")

def goHomeOldMan():
  setPassage(6, "goHomeOldMan()")
  print("...")
  wait(2)
  print("YOU IDIOT !\nDUCK stands for Destructive Unbelievable Cannon of Kyle !\nWith this weapon, the old man KILLS YOU !")
  die()

def helpOldMan():
  setPassage(4, "helpOldMan()")
  print("Old Man : \"So uhm, my DUCK has a problem... Can you come to my home to help me ?\"")
  cond("Yes", "Yes", "goHomeOldMan()", "goHomeOldMan()")

def dontHelpOldMan():
  setPassage(5, "dontHelpOldMan()")
  print("You decide to don't help the old man")
  wait(1)
  print("Suddenly, you see a guy RUNNIN' in the streets\nsaying \"He is back !! HE IS BAAAAAAACK ! NOOOOOOOO !\"")
  cond("Ask who is back", "Get out of this town", "askWhoIsBack()", "leaveRoRo()")
  
def stayInsideHome():
  global hamPrice
  setPassage(2, "stayInsideHome()")
  gotCoins = random.randint(2, 15)
  print("You stay inside your home.\nAnd you're lucky! There are", gotCoins, "coins on the table !")
  wait(0.5)
  setCoins("+", gotCoins)
  hamPrice = coins - random.randint(0, 3)
  wait(0.5)
  print("You take it, then realize there's nothing to do in your house")
  input("Press enter to go outside : ")
  getOutsideHome()

def getOutsideHome():
  setPassage(3, "getOutsideHome()")
  print("LOCATION : RoRo City")
  print("--------------------")
  wait(1.5)
  print("In front of your house, you see an old man.")
  wait(1)
  print("Old Man : \"Hello young person... I have problems with my DUCK.\nCould you help ?\"")
  cond("Yes I can help you sir.", "U mad man bro. Get out of my way", "helpOldMan()", "dontHelpOldMan()")

def start():
  setPassage(1, "start()")
  print("You wake up sloooooooowly\nYou decide to")
  cond("Stay inside", "Go outside", "stayInsideHome()", "getOutsideHome()")

# --
  
# -- FONCTION MAIN --

def main():
  clear()
  print("WTF RPG\nCopyright © PancakeDev")
  c = input("1 : Play\n2 : How to play\n> ")
  if c == "1":
    c = input("Enter the password of the\npassage you want to play in\nor enter 1 to start the game at the beginning\n> ")
    try:
      eval(passages[c])
    except KeyError:
      main()
  elif c == "hehe":
    while True:
      c = input(">>> ")
      eval(c)
  else:
    Help()

main()
