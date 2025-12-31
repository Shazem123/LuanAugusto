
import random
secret_number = random.randint(1, 10)
chances = 0
guess = 0

print("Welcome to the secret number identifier program! The program will run a random number generator between 1 and 10, and you gotta find it out before you ran out of chances. By the way, you have 5 of them!")
while True:
    guess = int(input("Type your guess: "))
    chances += 1

    if guess == secret_number:
        print(f"Congratulations! You found out the number in {chances} chances.") 
        break

    if chances == 5:
        print(f"You ran out of chances and the secret number was {secret_number}. Try running again!")
        break

    if guess < secret_number:
        print("Number too low! Try again.")

    else:
        print("Number too high! Try again.")