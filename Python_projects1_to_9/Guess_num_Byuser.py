num_to_guess = int(input("Enter the number I'm thinking of (between 1 and 100): "))
guess = None

print("Guess it!")

while guess != num_to_guess:
    guess = int(input("Enter your guess: "))
    if guess < num_to_guess:
        print("Too low! Try again.")
    elif guess > num_to_guess:
        print("Too high! Try again. ")
        
print("Congratulatons! You have guessed the number right!")
    