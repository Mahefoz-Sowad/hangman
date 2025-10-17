import random

words = ["TOWER", "SCHOOL", "GENTLEMAN", "HANGMAN", "GOOGLE"]

word = random.choice(words)
guessed_letters = set()
attempts = 7
attempts_left = attempts
display = ["_"] * len(word)

print("\nWelcome to Hangman: A Word Guessing Game!")
print(f"The word has {len(word)} letters.")
print("Type 'EXIT' at any time to quit.\n")

while attempts_left > 0:
    print("\nWord:", ' '.join(display))
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Attempts left: {attempts_left}")

    guess = input("Enter a letter (A-Z): ").upper()
    if guess == "EXIT" or guess == "QUIT":
        print("Exiting the game. Goodbye!")
        break

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
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
        print("\nYou won! The word was:", word)
        break
else:
    print("\nGame Over!\nNo more Attemps left!\nThe word was:", word)