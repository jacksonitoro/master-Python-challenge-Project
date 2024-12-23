#using random function to create Head or Tail game

import random
random_head_or_tail = random.randint(0,1)

if random_head_or_tail == 0:
    print("Heads")

else:
    print("Tails")