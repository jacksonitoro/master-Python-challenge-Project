#Application for Pizza Order. Includes multiple size selection with corresponding prices.
#Small size (S):$15
#Medium size (M):$20
#Large size (L):$25

#With special request such as;
#add pepperoni for small pizza (Y or N): $2
#add pepperoni for large pizza (Y or N): $3
#add extra cheese to any size of pizza (Y or N): $1

#Task execution
print("Welcome to JayPizzeria!!")

bill = 0
#extra_pepperoni_s = 0
#extra_pepperoni_m_l = 0
#extra_cheese = 0

#Select desired size
select_size = input("Kindly select your preferred size. s for small, m for medium, l for large: ")

if select_size == "S":
    bill += 15
    print(f"Small size is ${bill}.")

elif select_size == "M":
    bill += 20
    print(f"Medium size is ${bill}.")

elif select_size == "L":
    bill += 25
    print(f"Large size is ${bill}.")
else:
    print("You typed the wrong inputs.")

#To calculate how to add the charge for extra cheese and pepperoni to the bill

#To calculate amount for adding pepperoni
pepperoni = input("Do want pepperoni? Y for yes and N for no: ")
if pepperoni == "Y":
    if select_size == "S":
        bill += 2
    else:
        bill += 3

#To calculate total amount based on if extra cheese was requested
extra_cheese = input("Do you want extra cheese? Y for yes and N for no:")
if extra_cheese == "Y":
    bill += 1
#Total bill
print(f"Your Total Bill is ${bill}")



