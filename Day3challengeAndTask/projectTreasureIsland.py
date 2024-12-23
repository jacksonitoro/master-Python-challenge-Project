#Project to test the use of logical operators skills
#Treasure Map
#Find your way to the door to win

print(r'''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
 ''')
print("Welcome to Treasure Map.")
print("Your mission is to find the treasure.")

choose_direction = input("You're at a cross road. Where do you want to go? Type Right or Left: ").lower()
if choose_direction == "left":
    print("Please proceed!")
    at_the_lake = input(
        "You have come to the great Lake. Do you want to wait for the boat or swim across? Type Wait or Swim:").lower()
    if at_the_lake == "wait":
        choose_ur_door = input(
            "You're close. Please choose your door to reveal the treasure. Blue for blue, Yellow for yellow door, Red for red door: ").lower()
        if choose_ur_door == "yellow":
            print("Burned by fire. Game Over!")
        elif choose_ur_door == "red":
            print("Eaten by beasts. Game Over!")
        elif choose_ur_door == "blue":
            print("Congratulation! You have found the treasure. You Win!!!")
        else:
            print("Game Over! Try again next time.")
    else:
        print("Attacked by Trout. Game over!")
else:
    print("You fell into the hole. Game Over!")

'''       choose_ur_door = input(
            "You're close. Please choose your door to reveal the treasure. Blue for blue, Yellow for yellow door, Red for red door: ")
        if choose_ur_door == "Yellow":
            print("Burned by fire. Game Over!")
        elif choose_ur_door == "Red":
            print("Eaten by beasts. Game Over!")
        elif choose_ur_door == "Blue":
            print("Congratulation! You Win!!!")
        else:
            print("Game Over! Try again next time.")
'''







