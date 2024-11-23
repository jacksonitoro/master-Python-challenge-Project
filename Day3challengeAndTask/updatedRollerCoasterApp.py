#Using logical operators
print("Welcome to the Rollercoaster World!!")
guest_height = int(input("Please Enter your Height in cm: "))

bill = 0

if guest_height >= 80:
    print("Yaaah! Time for some fun!!!")
    age = int(input("Please enter your age: "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7

    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want Photo? Type y for Yes and n for No: ")
    if wants_photo == "y":
        #Add $3 to the total bill regardless of age
        bill += 3
    print(f"Your total bill is ${bill}. Thank you for your patronage.")


    print("Go Have Some Fun! Life is a Rollercoaster.")
else:
    print("Sorry, you have to grow more height to roll. Stay safe!!")