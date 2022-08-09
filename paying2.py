#PAYING _RANDOM_2
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random 

list1 = random.randrange(len(names))

print(str(names[list1]) + " is going to buy the meal today!")


