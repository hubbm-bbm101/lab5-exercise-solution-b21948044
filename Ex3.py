import random

N = int(input("Give me a number"))
random_number = random.randint(0,N)
number = int(input("Give me a number"))
while number != random_number:
    if number > random_number:
        print("Decrease your number")
        number = int(input("Give me a number"))
    elif number < random_number:
        print("Increase your number")
        number = int(input("Give me a number"))
if number == random_number:
        print("Well done!")
