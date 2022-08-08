rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
rps = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
rps2 =[rock, paper, scissors]
if rps == str(0):  
  print('You chose Rock' + rps2[0])
elif rps == str(1):
  print('You chose Paper'+ rps2[1])
elif rps == str(2):
  print('You chose Scissors' + rps2[2])
elif rps != str(0) or str(1) or str(2):
  print("Invalid choice you lose!")
  exit()

import random
x = random.choice(rps2)
if x == rock:
  print('The computer chose Rock' + rock)
elif x == paper:
  print('The computer chose Paper' + paper)
elif x == scissors:
  print('The computer chose Scissors' + scissors)

if rps == str(0) and x == scissors:
  print("YOU WIN")
elif rps == str(1) and x == rock:
  print("YOU WIN")
elif rps == str(2) and x == paper:
  print("YOU WIN")
elif rps == str(0) and x == paper:
  print("YOU LOSE")
elif rps == str(1) and x == scissors:
  print("YOU LOSE")
elif rps == str(2) and x == rock:
  print("YOU LOSE")
else:
  print("DRAW")


