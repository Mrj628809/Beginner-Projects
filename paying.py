#PAYING_RANDOM
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random 

list1 = random.choice(names)
print(list1+" is going to buy the meal today!")


