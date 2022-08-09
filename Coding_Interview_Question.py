#FIZZBUZZ
for number in range(1,101):
  if number%3==0 and number%5==0:
    number = "FIZZBUZZ"
  elif number%3==0:
    number = "FIZZ"
  elif number%5==0:
    number = "BUZZ"
  print(number)
  
  
