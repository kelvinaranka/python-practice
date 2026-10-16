import sys

from random import randint

random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        number = int(
            input('please choose a number that falls between those two you just choose: '))
        if number >= int(sys.argv[1]) and number <= int(sys.argv[2]):
            if number == random_number:
                print("you are a genuis!")
                break
    except ValueError:
        print("please enter a number")
        continue
