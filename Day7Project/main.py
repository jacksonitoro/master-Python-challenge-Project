"""
The Hangman game project
"""

word_list = ["aardvark", "baboon", "camel"]

#Task 1: Randomly choose a word from the word-list and assign it to a variable called chosen_word. Then print it.
import random

#create a variable called 'lives' to keep track of the number of lives or attempt left
#set lives to equal to 6

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)
#Improvement1: create a placeholder with the same number of the chosen_word

placeHolder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeHolder += "_"
print(placeHolder)

#Update: use while loop to let the user guess again
game_over = False
correct_letter = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
#Task2: Ask the user to guess a letter and assign their answer to variable called guess. Make the guess lowercase.


    print(guess)



#Task3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
#Improvement2: create a display that put the guess letter in the right position


    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)

        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print(display)
    """
    TODO: if guess is not a letter in the chosen_word, then reduce lives by 1
    if lives goes down to 0 then the game should stop and it should print "You lose"
    """

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True

    if "_" not in display:
        game_over = True
        print("You win!")