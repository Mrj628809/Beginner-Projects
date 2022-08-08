print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
fire = str("It's a room full of fire. Game Over.")

treasure = str("You found the treasure! You Win!")

no_door = str("You chose a door that doesn't exist. Game Over.")

trout = str("You get attacked by an angry trout. Game Over.")

hole = str("You fell into a hole. Game Over.")

beast = str("You enter a room of beasts. Game Over.")
crossroads1 = 'left' or 'right'

island1 = 'swim' or 'wait'

red = fire

yellow = treasure

blue = trout

crossroads = input('You\'re at a crossroad. Where do you want to go? Type \"left\" or \"right\" ').lower()
if crossroads == crossroads1 and crossroads1 =="right":
  pass
elif crossroads == crossroads1 and crossroads1 == "left":
  print(hole)
  exit()

elif crossroads == "":
  exit()

  
island = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
if island1 == "wait" and island == "wait":
  pass
elif island1 == "swim" and island.lower() == "swim":
  print(trout)
  exit()
elif island == "":
  exit()

    
door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
if door == "red":
  print(fire)
elif door == "yellow":
  print(treasure)
elif door == "blue":
  print(beast)
else:
  print(no_door)