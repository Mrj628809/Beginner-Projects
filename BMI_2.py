#BMI
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = float(weight)/(float(height)**2)
bmi_2 = round(bmi)

if bmi < 18.5:
  print("Your BMI is " + str(bmi_2) + ", you are underweight.")

elif bmi < 25:
  print("Your BMI is " + str(bmi_2) + ", you have a normal weight.")

elif bmi < 30:
  print("Your BMI is " + str(bmi_2) + ", you are slightly overweight.")

elif bmi < 35:
  print("Your BMI is " + str(bmi_2) + ", you are obese.")

else:
  print("Your BMI is " + str(bmi_2) + ", you are clinically obese.")
