student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]
total_examScore = sum(student_scores)

sum =0

for score in student_scores:
    sum += score

print(sum)
print(total_examScore)

#checking for the maximum score using For loop and If conditional statement
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

#using For Loop with the Range function

for number in range(1, 20):
    print(number)

#skipping 3 numbers
for number in range(1, 21, 3):
    print(number)

#sum of numbers between 1 and 100
total_num = 0
for number in range(1,101):
    total_num += number
print(total_num)