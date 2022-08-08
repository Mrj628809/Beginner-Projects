# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random 
list = len(names)
list1 = random.randint(0, list - 1)
print(str(names[list1]) + " is going to buy the meal today!")


