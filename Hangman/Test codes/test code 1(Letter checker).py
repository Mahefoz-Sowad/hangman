word = "HELLO"

print("Guess the letters in a word.")
print("Type 'EXIT' to quit.\n")



while True:

    letter = input("Enter a letter: ").upper()

    if letter == "EXIT" or letter == "QUIT":
        print("Exiting the program. Goodbye!")
        break

    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single capital alphabet letter.")
        continue

    if letter in word:
        print(f"Yes, the letter '{letter}' is in the word.\n")

    else:
        print(f"No, the letter '{letter}' is NOT in the word.\n")