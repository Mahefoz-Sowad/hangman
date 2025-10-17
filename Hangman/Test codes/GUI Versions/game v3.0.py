"""
to-do:
1. add message box for invalid input
2. add icon
3. rework the difificulty selection mathod
4. add button to now incude sapcific words
"""


#added image display

import tkinter as tk
from tkinter import messagebox
import random
from english_words import get_english_words_set
from PIL import Image, ImageTk
import os

words = get_english_words_set(['web2'])
filtered_words_easy = [word.upper() for word in words if 4 <= len(word) <= 5]
filtered_words_medium = [word.upper() for word in words if 6 <= len(word) <= 8]
filtered_words_hard = [word.upper() for word in words if 9 <= len(word) <= 10]

guessed_letters = set()
max_attempts = 7
attempts_left = max_attempts
word_display = []
randomly_selected_word = ""

current_index = 0
image_folder = os.path.join(os.getcwd(), "Test codes\GUI Versions\hangmanHP")
images = [
    os.path.join(image_folder, f"hangman{x}.png") for x in range(8)
]

root = tk.Tk()
root.title("Hangman: A Word Guessing Game")
root.geometry("1280x720")

difficulty_frame = tk.Frame(root, bg="white")
difficulty_frame.pack(pady=20)

tk.Label(
    difficulty_frame, 
    text="Select Difficulty").pack(pady=20)
tk.Button(
    difficulty_frame, 
    text="Easy (4-5 letters)", 
    bg="green", 
    fg="white",
    width=20, 
    command=lambda: start_game("easy")).pack(pady=10)
tk.Button(
    difficulty_frame, 
    text="Medium (6-8 letters)", 
    bg="orange", 
    fg="white",
    width=20, 
    command=lambda: start_game("medium")).pack(pady=10)
tk.Button(
    difficulty_frame, 
    text="Hard (9-10 letters)", 
    bg="red", 
    fg="white",
    width=20, 
    command=lambda: start_game("hard")).pack(pady=10)


def start_game(difficulty_level):
    global randomly_selected_word, word_display, guessed_letters, attempts_left, selacted_difficulty, current_index

    selacted_difficulty = difficulty_level
    guessed_letters.clear()
    attempts_left = max_attempts
    current_index = 0

    if selacted_difficulty == 'easy':
        randomly_selected_word = random.choice(filtered_words_easy)
    elif selacted_difficulty == 'medium':
        randomly_selected_word = random.choice(filtered_words_medium)
    else:
        randomly_selected_word = random.choice(filtered_words_hard)

    word_display = ['_' for _ in randomly_selected_word]

    difficulty_frame.destroy()
    build_game_ui()

def build_game_ui():
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    top = tk.Frame(
        root, 
        bg="blue", 
        height=50, 
        relief="raised", 
        bd=3)
    top.grid(
        row=0, 
        column=0, 
        columnspan=2, 
        sticky="nsew", 
        padx=1, 
        pady=1)
    tk.Label(
        top, 
        text="Let's see how good your guesses are!", 
        bg="blue", 
        fg="white").pack(pady=10)

    left1 = tk.Frame(
        root, 
        bg="white", 
        relief="raised", 
        bd=3)
    left1.grid(
        row=1, 
        column=0, 
        sticky="nsew", 
        padx=1, 
        pady=1)

    left2 = tk.Frame(
        root, 
        bg="white", 
        relief="raised", 
        bd=3)
    left2.grid(
        row=2, 
        column=0, 
        sticky="nsew", 
        padx=1, 
        pady=1)

    left3 = tk.Frame(
        root, 
        bg="white", 
        relief="raised", 
        bd=3)
    left3.grid(
        row=3, 
        column=0, 
        sticky="nsew", 
        padx=1, 
        pady=1)

    right1 = tk.Frame(
        root, 
        bg="white", 
        relief="raised", 
        bd=3)
    right1.grid(
        row=1, 
        column=1, 
        rowspan=2, 
        sticky="nsew", 
        padx=1, 
        pady=1)
    tk.Label(
        right1, 
        text="Images").pack(pady=10)

    right2 = tk.Frame(
        root, 
        bg="white", 
        relief="raised", 
        bd=3)
    right2.grid(
        row=3, 
        column=1, 
        sticky="nsew", 
        padx=1, 
        pady=1)

    
    global guessed_label, word_label, word_display, attempts_label, entry, guessed_letters
    global attempts_left, randomly_selected_word, image_label, current_index

    guessed_label = tk.Label(left1, text="Guessed letters: ")
    guessed_label.pack(pady=10)

    word_label = tk.Label(left2, text="Word: " + ' '.join(word_display))
    word_label.pack(pady=10)

    attempts_label = tk.Label(left2, text=f"Attempts left: {attempts_left}")
    attempts_label.pack(pady=10)

    img_display = load_image(current_index)
    image_label = tk.Label(right1, image=img_display)
    image_label.image = img_display  #prevents garbage collection
    image_label.pack(pady=10)

    tk.Label(left3, text="Enter a Letter").pack(pady=10)
    entry = tk.Entry(left3)
    entry.pack(pady=5)

    submit_btn = tk.Button(left3, text="Submit", command=check_letter)
    submit_btn.pack(pady=5)



    word_display = ['_' for _ in randomly_selected_word]
    update_display()


    def restart_game():
        global guessed_letters, attempts_left, word_display, randomly_selected_word, current_index

        guessed_letters.clear()
        attempts_left = max_attempts
        current_index = 0

        if selacted_difficulty == 'easy':
            randomly_selected_word = random.choice(filtered_words_easy)
        elif selacted_difficulty == 'medium':
            randomly_selected_word = random.choice(filtered_words_medium)
        else:
            randomly_selected_word = random.choice(filtered_words_hard)

        word_display.clear()
        word_display = ['_' for _ in randomly_selected_word]
        update_display()
    restart_btn = tk.Button(right2, text="Restart", width=10, command=restart_game)

    def exit_app():
        root.destroy()
    exit_btn = tk.Button(right2, text="exit", command=exit_app, width=10, fg="white", bg="red")

    right2.grid_rowconfigure(1, weight=1)
    right2.grid_columnconfigure(0, weight=1)
    right2.grid_columnconfigure(1, weight=1)

    restart_btn.grid(row=1, column=0, pady=10)
    exit_btn.grid(row=1, column=1, pady=10)

    update_display()

def load_image(index):
    img = Image.open(images[index])
    img = img.resize((300, 300))
    return ImageTk.PhotoImage(img)

def update_display():
    guessed_label.config(text="Guessed letters: " + ' '.join(sorted(guessed_letters)))
    word_label.config(text="Word: " + ' '.join(word_display))
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    img_display = load_image(current_index)
    image_label.config(image=img_display)
    image_label.image = img_display   



def check_letter():
    global attempts_left, current_index

    letter = entry.get().upper()
    entry.delete(0, tk.END)

    if not letter.isalpha() or len(letter) != 1 or letter in guessed_letters:
        return  

    guessed_letters.add(letter)

    if letter in randomly_selected_word:
        for i, char in enumerate(randomly_selected_word):
            if char == letter:
                word_display[i] = letter
    else:
        attempts_left = attempts_left - 1
        current_index = max_attempts - attempts_left

    update_display()

    if "_" not in word_display:
        messagebox.showinfo("Hangman", f"You won! The word was '{randomly_selected_word}'.")
        root.quit()
    elif attempts_left == 0:
        messagebox.showinfo("Hangman", f"You lost! The word was '{randomly_selected_word}'.")
        root.quit()

root.mainloop()