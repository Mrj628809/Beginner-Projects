#TIP CALCULATOR
print("Welcome to the tip calculator!")
cost = input("What is the total bill?\n")

percent = input("How much tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

y = float(percent)/float(100)
x = (float(cost)/int(people)) * float(y)

print(f'Each person should pay:\n' + str(round(x, 2)))
