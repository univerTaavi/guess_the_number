import random

random_number = random.randint(0, 20)

while True:
    x = int(input("Guess the number: "))
    if x == random_number:
        print("You win! The number was {}.".format(random_number))
        break
    elif x > random_number:
        print("You guessed too high! The number is smaller.")
    elif x < random_number:
        print("You gussed too low! The number is bigger.")
