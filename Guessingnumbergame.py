import random as rd
number = rd.randint(1, 101)

guess = int(input("Enter your guess: "))
counter = 1
while guess <= number:
    if guess < number:
        print("Guess higher")
    else:
        print("Guess lower")

    guess = int(input("Enter your guess: "))
    counter += 1

if guess:
    print(f"Attempts made to guess : {counter}")
    print(f"You have guessed number {guess} which is correct")
else:
    print("Your guess is incorrect")
