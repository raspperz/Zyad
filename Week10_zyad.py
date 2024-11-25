
# #Get input from user 
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# #Variable  to hold the equation and carry out the maths
# bmi = weight / (height ** 2)

# #condition statements
# if bmi < 18.5:
#     print(f"Your BMI is {bmi:.2f}. Category: Underweight")
# elif 18.5 <= bmi < 24.9:
#     print(f"Your BMI is {bmi:.2f}. Category: Normal weight")
# elif 25 <= bmi < 29.9:
#     print(f"Your BMI is {bmi:.2f}. Category: Overweight")
# else:
#     print(f"Your BMI is {bmi:.2f}. Category: Obesity")

#2 im not really sure i dont know how to make a tax calculator 


# Temperature Converter

print("Temperature Converter")
print("1: Convert Celsius to Fahrenheit")
print("2: Convert Fahrenheit to Celsius")

choice = input("Choose an option (1/2): ")
#got method from google 
if choice == "1":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
else:
    print("Invalid choice. Please select 1 or 2.")

    # Input a number
number = int(input("Enter a number: "))

# Input a number
number = int(input("Enter a number: "))

# Checks conditions
positive = number > 0
negative = number < 0
even = number % 2 == 0
divisible_by_3 = number % 3 == 0

# Displays the results
print("Positive:", positive)
print("Negative:", negative)

if positive:
    print("Even:", even)
    print("Odd:", not even)
elif negative:
    print("no", divisible_by_3)


# Input employee details
years_of_service = int(input("Enter years of service: "))
salary = float(input("Enter salary: "))

# Bonus calculation found on google
has_bonus = years_of_service > 5
bonus_percentage = 0.10 if salary > 50000 else 0.15
bonus = salary * bonus_percentage if has_bonus else 0

# Displays bonus
print("The Is Bonus:", bonus)

