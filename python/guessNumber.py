import random
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()
secret_number = random.randint(1,9)
guess_count= 0
guess_limit = 3
guesses = []

print("Guess number between 1 and 9.")
while guess_count < guess_limit:
    try:
        guess = int(input("Guess: "))
        guess_count += 1
        if guess in guesses:
            print("You already pick this number!")
            continue
        guesses.append(guess)
        if not 1 <= guess <=9:
            print("Number must be between 1 and 9.")
            continue
        elif guess == secret_number:
            print("You are right! Secret number is", secret_number)
            break
        elif guess >= 10:
            print("Number is lower or equal 9.")
        elif guess < secret_number:
            print("Number is bigger.")
        elif guess > secret_number:
            print("Number is smaller.")
    except ValueError:
        print('Must be a number.')
        
else:
    print("Your's numbers: ", guesses)
    print("You'r failed.")
    print("Secret number was", secret_number)
