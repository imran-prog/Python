import random

print("Number Guessing Game")

number = random.randint(1, 100)

chances = 1

print("Guess the number between 1 to 100")

while chances < 10:
    guess = int(input("Guess: "))

    if guess == number:
        print("Congratulation YOU WON!!!")
        print("You done it in", chances, "tries")
        break
    elif guess > number:
        print("Your Guess is too high, Guess the number lower then", guess)
    else:
        print("Your Guess is too low, Guess the number higher then", guess)

    chances += 1

if not chances <= 10:
    print("You lose, Try again next time")
    print("The number is", number)