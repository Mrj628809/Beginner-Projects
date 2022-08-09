# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random 

list = len(names)
list_1 = random.randint(0, list - 1)

print(str(names[list_1]) + " is going to buy the meal today!")


