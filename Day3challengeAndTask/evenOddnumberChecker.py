#Program to check if an input number is Even or Odd number. Executed using modulo operator

input_number = int(input("Please enter the number to check: "))

if input_number % 2 == 0:
    print(f"{input_number} is Even number")

else:
    print(f"{input_number} is Odd number")