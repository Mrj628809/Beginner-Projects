# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name11 = name1.lower()
name22 = name2.lower()
total  =name11.count('t') + name22.count('t')
total1 =name11.count('r') + name22.count('r')
total2 =name11.count('u') + name22.count('u')
total3 =name11.count('e') + name22.count('e')
total4 =name11.count('l') + name22.count('l')
total5 =name11.count('o') + name22.count('o')
total6 =name11.count('v') + name22.count('v')
total7 =name11.count('e') + name22.count('e')
new_total = total + total1 + total2 + total3 
new_total2 = total4 + total5 + total6 + total7
new_score = str(new_total)+str(new_total2)
new_score1 = int(new_score)
if new_score1 < 10 or new_score1 > 90:
  print("Your score is " + new_score + ", you go together like coke and mentos.")
elif new_score1 > 40 and new_score1 < 50:
  print("Your score is " + new_score + ", you are alright together.")
else:
  print("Your score is " + new_score + ".")
