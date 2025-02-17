


def greet(name1):
    print(f"Hello {name1}!")
    print(f"How do you do {name1}?")
    print("Isn't the weather nice?")

greet("Jane")

#functions that allow for inputs

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")

greet_with_name("Jim")

def greet_with(myname, location):
    print(f"Hello {myname}")
    print(f"What is it like in {location}?")

#greet_with("Jack", "New York")
greet_with(myname="Jack", location="New York")

#weeks left for 90yr old

def life_in_weeks(current_age):
    max_age = 90
    week_in_year = 52

    remaining_years = max_age - current_age
    remaining_weeks = remaining_years * week_in_year

    print(f"You have {remaining_weeks} weeks left")


life_in_weeks(40)