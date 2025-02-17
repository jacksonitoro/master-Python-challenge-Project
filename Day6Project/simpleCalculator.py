"""
A simple calculator program with infinite loop function
Integrating WHILE Loop and IF statement
"""
from random import choice


def simple_calculator():
    print("Simple Calculator")
    print("==================")

    while True: #Infinite loop
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Enter number (1-5): ")

        if choice == "5":
            print("Exiting the program. Goodbye!")
            break #Exiting the infinite loop

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"The result is: {num1 + num2}")

                elif choice == "2":
                    print(f"The result is: {num1 - num2}")

                elif choice == "3":
                    print(f"The result is: {num1 * num2}")

                elif choice == "4":
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option.")

simple_calculator()