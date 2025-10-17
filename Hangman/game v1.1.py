import random
import sys
from english_words import get_english_words_set

words = get_english_words_set(['web2'])
filtered_words_easy = [word.upper() for word in words if 4 <= len(word) <= 5]
filtered_words_medium = [word.upper() for word in words if 6 <= len(word) <= 8]
filtered_words_hard = [word.upper() for word in words if 9 <= len(word) <= 10]

def choose_difficulty():
    print("\nWelcome to Hangman: A Word Guessing Game!")
    print("Select difficulty:\n"
            "1. Easy (4-5 letters)\n"
            "2. Medium (6-8 letters)\n"
            "3. Hard (9-10 letters)")
    print("Type 'EXIT' at any time to quit.\n")
    
    while True:
        choice = input("Enter choice (1, 2, 3): ").strip().upper()
        if choice in ["EXIT", "QUIT"]:
            print("Exiting the program. Goodbye!")
            sys.exit()   
        elif choice == "1":
            return random.choice(filtered_words_easy)
        elif choice == "2":
            return random.choice(filtered_words_medium)
        elif choice == "3":
            return random.choice(filtered_words_hard)
        else:
            print("Invalid input. Please choose 1, 2, or 3.")



word = choose_difficulty()
guessed_letters = set()
attempts = 7
attempts_left = attempts
display = ["_"] * len(word)


print("\nLet's start the game!")
    
while attempts_left > 0 and "_" in display:
    print("\nWord:", ' '.join(display))
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}")

    guess = input("Enter a letter (A-Z): ").upper()
    if guess == "EXIT" or guess == "QUIT":
        print("Exiting the game. Goodbye!")
        break

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single english letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts_left = attempts_left - 1

    if "_" not in display:
        print(f"\nYou won! The word was '{word}'.\n")
        break
else:
    print("\nGame Over!\nNo more Attemps left!\nThe word was:", word)