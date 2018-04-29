#write a python program to flip a coin 1000 times, and count heads and tails. 
#expected output for heads = 5073, for tails = 4927
'''define a function named coin_flip
import rand
set a variable heads and tails to 0
set counter to 0
create a for loop saying -  if counter <= 1000, if '''


import random
def coin_flip():
    result = random.choice("heads" "tails")
    counter = 0
    while counter <= 1000:
        if result == "heads":
            print(result)
        elif result == "tails":
            print(result)
        counter += 1
print(coin_flip())
