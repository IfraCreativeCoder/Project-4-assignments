import random

num_to_guess = random.randint(1, 100)
guess = None
attempts = 0

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 to 100.Can you guess it?")

while guess != num_to_guess:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < num_to_guess:
        print("Too low! Try again.")
    elif guess > num_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulatons! You have guessed the number right. In {attempts} attempts!.")
        
    