import random

def hangman():
    words = ["python", "programming", "hangman", "challenge", "development"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(chosen_word))

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        current_progress = "".join(letter if letter in guessed_letters else "_" for letter in chosen_word)
        print(current_progress)

        if "_" not in current_progress:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"You've run out of attempts! The word was '{chosen_word}'.")

hangman()