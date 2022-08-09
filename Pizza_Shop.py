#PIZZA SHOP
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total_price = 0
if size == "S":
  total_price =+ 15
elif size == "M":
  total_price =+ 20
elif size == "L":
  total_price =+ 25

topping1 = 0
if add_pepperoni == "Y" and size == "S":
  topping1 =+ 2
elif add_pepperoni == "Y" and size == "M":
  topping1 =+ 3
elif add_pepperoni == "Y" and size == "L":
  topping =+ 3
elif add_pepperoni == "N":
  topping1 =+ 0

topping2 = 0
if extra_cheese == "Y":
  topping2 =+ 1
elif extra_cheese == "N":
  topping2 =+ 0

total = total_price + topping1 + topping2
print(f"Your final bill is: ${total}.")
