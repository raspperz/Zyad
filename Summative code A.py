

#  Asking the user for their name
name = input("Enter your name: ")

#  Gets the current time of day to greet the user later on


from datetime import datetime
time = datetime.now().hour




#  Greet the user based on the time of day, if its between 5am to 12pm its a good morning
#if its between 12pm and 5pm its a good afternoon anything else is a good night.
if 5 <= time < 12:
    print("Good Morning!,", name)
elif 12 <= time < 17:
    print("Good Afternoon!,", name)
else:
    print("Good Nigh!,", name)

# Asks the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

#  Calculates the sum of the three numbers by addition
sum_numbers = num1 + num2 + num3
print("The sum of the numbers is:", sum_numbers)

#  Calculates the average of the three numbers bu getting the sum from the prev  function then divides by 3
average = sum_numbers / 3
print("The average of the numbers is:", average)

#  Calculates the difference between each pair of numbers then prints the results 
diff1 = num1 - num2
diff2 = num2 - num3
diff3 = num3 - num1
print("The differences between the numbers are:", diff1, diff2, diff3)

#  Finds the greatest number using conditions
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
print("The greatest number is:", greatest)

#  Checks if the greatest number is odd or even by getting the remainder,
#if the remainder is 0 once divided by 2 then that means its even other wise its odd/
if greatest % 2 == 0: 
    print("The greatest number is even")

else:
    print("The greatest number is odd")


