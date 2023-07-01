import random

secret_number = random.randint(1, 100)

guesses_taken = 0

max_guesses = 5

print("Welcome to Guessing Number Game!")
print("I'm thinking of number between 1 and 100.")

while guesses_taken < max_guesses:

    guess = int(input("Poskusi: "))
    guesses_taken += 1

    if guess == secret_number:
        print("Congratulations!")
        break
    elif guess < secret_number:
        print("Premalo!")
    else:
        print("Prevec!")

if guesses_taken == max_guesses:
    print("Prevec poskusov. Stevilo je bilo ", secret_number)