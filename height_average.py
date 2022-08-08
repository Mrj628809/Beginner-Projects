# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Write your code below this row 👇
total = 0
#sum function
count = 0
#length function
for items in student_heights:
  count += 1
  #it will run the code and count each item entered     in the list
  total += items
  #it will run the code and add each integer item       entered in the list
average = total/count
print(round(average))

#another way to write this and break it up into parts:

#LENGTH FUCNTION AS FOR LOOP
count1 = 0
for length in student_heights:
  count1 += 1
print(count1)

#SUM FUCTION AS A FOR LOOP
total1 = 0
for items1 in student_heights:
  total1 += items1
print(total1)

#COMBINED
average1 = total1/count1
print(round(average1)