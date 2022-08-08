#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Create a string to store the password
password = ""
#for loop to run through the letters list and pick at random the selected number of letters
for char in range(1, nr_letters + 1):
  random_char = random.choice(letters)
  password += random_char
#for loop to run through the symbols list and pick at random the selected number of symbols
for sym in range(1, nr_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym
#for loop to run through the numbers list and pick at random the selected number of numbers
for num in range(1, nr_numbers + 1):
  random_num = random.choice(numbers)
  password += random_num

print(f"Here is your new password: {password}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#convert the string into a list
password1 = list(password)
#shuffle the characters in the list
random.shuffle(password1)
#convert the list back into a string
shuffled_password = ''.join(password1)
print(f"Here is your new randomized password: {shuffled_password}")
