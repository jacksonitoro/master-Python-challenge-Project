#Random selection from list using random function
import random

friends = ["Gideon", "Joshua", "Jackson", "Alice", "Sarah", "Daniel"]
#1 Option
print(random.choice(friends))

#2 Option

random_index = random.randint(0,4)
print(friends[random_index])