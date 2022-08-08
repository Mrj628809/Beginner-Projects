# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 

list1 = random.randrange(len(names))

print(str(names[list1]) + " is going to buy the meal today!")


