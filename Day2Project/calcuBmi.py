#Body mass Index BMI
#bmi=weight/height^2
weight = int(input("Enter your body weight: "))
height = float((input("Enter your height: ")))
bmi = weight / (height ** 2)

print(f"Your body mass index is: {bmi:.2f}")