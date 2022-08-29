print('\t\t\t INTRODUCTION \n')
print('1) If the guess is less than 1 or greater than 100: "OUT OF BOUNDS"')
print('2) On first turn, if the guess is:')
print('\t within 10 of the number: "WARM!"')
print('\t further than 10 away from the number: "COLD!"')
print('3) On all subsequent turns, if a guess is:')
print('\t closer to the number than the previous guess: "WARMER!"')
print('\t farther from the number than the previous guess: "COLDER!"')
print('4) When the guess equals the number: "CORRECT" and how many guesses taken\n')
print('\t\t\t WELCOME TO GAME \n')
from random import randint

random_value = randint(1, 100)
guess_list = []
while True:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    guess_list.append(guess)
    if guess == random_value:
        print("AMAZING. You found the correct value!")
        print(f"You've guessed {len(guess_list)} times")
        break
    if len(guess_list) == 1:
        if abs(guess - random_value) <= 10:
            print("WARM!")
            continue
        else:
            print("COLD!")
            continue

    if abs(guess - random_value) <= abs(guess_list[-2] - random_value):
        print("WARMER!")
        continue
    else:
        print("COLDER!")
        continue

