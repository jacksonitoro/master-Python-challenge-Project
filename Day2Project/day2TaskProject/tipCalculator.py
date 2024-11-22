# Day two project : Tip Calculator
print("Welcome to Smart tip calculator!")
total_bill = float(input("Please enter Total Bill: $ "))
tip_percent = int(input("How much tip do you want to give? 10 12 15 : \n"))
number_people_splitBill = int(input("How many people to split the bills?\n"))

tip_as_percent = tip_percent / 100
total_tip_amount = total_bill * tip_as_percent
bill_plus_tip = total_bill + total_tip_amount
bill_per_person = bill_plus_tip / number_people_splitBill
final_amount = round(bill_per_person,2)

print(f"Total bill is: ${bill_plus_tip}")
print(f"Each person should pay: ${final_amount}")



