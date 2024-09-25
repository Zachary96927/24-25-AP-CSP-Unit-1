#   a114_divisible.py
number1 = int(input("What is first number?:"))
number2 = int(input("What is second number?:"))
while number1 % number2 != 0:
    print("Not evenly divisible")
    number1 = int(input("What is first number?:"))
    number2 = int(input("What is second number?:"))

if number1 % number2 == 0:
 print("Evenly divisible")

# get two numbers from user

# loop while the numbers are not divisible (the remainder is not 0)

# inform user of result

# gather user input again

# inform user of result