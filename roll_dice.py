
###########################

#python roll_dice.py

import random
def roll_dice():
    return random.randint(1,6)
result = roll_dice()
print(result)

###########################

#python roll_dice.py x

import random
import sys

def roll_dice(x):
    return random.randint(1, x)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = 6  # デフォルト値
    elif len(sys.argv) == 2:
        try:
            x = int(sys.argv[1])
        except ValueError:
            print("Error: Please provide a valid integer for x.")
            sys.exit(1)
    else:
        print("Usage: python roll_dice.py [x]")
        sys.exit(1)

    result = roll_dice(x)
    print(result)

