import random
from english_words import get_english_words_set


print("Type 'EXIT' to quit.")
print("Choose difficulty level:\n")


while True:
    words = get_english_words_set(['web2'])

    filtered_words_easy = [word for word in words if 4 <= len(word) <= 5]
    filtered_words_medium = [word for word in words if 6 <= len(word) <= 8]
    filtered_words_hard = [word for word in words if 9 <= len(word) <= 10]


    wordset1 = random.sample(filtered_words_easy, 10)
    wordset2 = random.sample(filtered_words_medium, 10)
    wordset3 = random.sample(filtered_words_hard, 10)

    difficulty = input("1. Easy (4-5 letters)\n" "2. Medium (6-8 letters)\n" "3. Hard (9-10 letters)\n" "\nEnter 1, 2, or 3: ").upper()

    if difficulty == "EXIT" or difficulty == "QUIT":
        print("Exiting the program. Goodbye!")
        break
    if difficulty.isalpha():
        print("\nPlease enter a valid input")
        continue
    if int(difficulty) >=4:
        print("\nPlease enter a valid input")
        continue

    if difficulty == "1":
            randomly_selected_word = wordset1
            print(randomly_selected_word)
    elif difficulty == "2":
            randomly_selected_word = wordset2
            print(randomly_selected_word)
    else: 
        randomly_selected_word = wordset3
        print(randomly_selected_word)
    '''
    break
    '''