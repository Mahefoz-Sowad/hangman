import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("Hangman: A word guessing game")
root.geometry("1280x780")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

left1 = tk.Frame(
    root, 
    bg="white", 
    relief="groove",
    bd=2
)
left1.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)

left2 = tk.Frame(
    root, 
    bg="white", 
    relief="groove",
    bd=2
)
left2.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)

left3 = tk.Frame(
    root, 
    bg="white", 
    relief="groove",
    bd=2
)
left3.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)

right1 = tk.Frame(
    root, 
    bg="white", 
    relief="groove",
    bd=2
)
right1.grid(row=0, column=1, rowspan= 2, sticky="nsew", padx=1, pady=1)

right2 = tk.Frame(
    root, 
    bg="white", 
    relief="groove",
    bd=2
)
right2.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)

right1.grid_rowconfigure(0, weight=1)
right1.grid_rowconfigure(1, weight=1)
right1.grid_columnconfigure(0, weight=1)
right2.grid_rowconfigure(1, weight=1)
right2.grid_columnconfigure(0, weight=1)
right2.grid_columnconfigure(1, weight=1)

tk.Label(left1, text="Guessed letters:").pack(pady=10)
tk.Label(left2, text="Attempts left:\n Word _ _ _ _").pack(pady=10)
tk.Label(left3, text="Enter a Letter").pack(pady=10)
tk.Label(right1, text="Hangman png").grid(row=0, column=0, pady=10)

#create an entry/input point in left3 frame
entry = tk.Entry(left3)
entry.pack(pady=5)

submit_btn = tk.Button(left3, text="Submit")
submit_btn.pack(pady=5)


image_folder = os.path.join(os.getcwd(), "Test codes\GUI Versions\hangmanHP")
images = [
    os.path.join(image_folder, f"hangman{x}.png") for x in range(8)
]

image_index = 0

def load_image(index):
    img = Image.open(images[index]).resize((300, 300))
    return ImageTk.PhotoImage(img)

imgOnDisplay = load_image(image_index)
image_label = tk.Label(right1, image=imgOnDisplay)
image_label.grid(row=1, column=0, pady=10)

def next_image():
    global image_index, imgOnDisplay
    if image_index + 1 >= len(images):
        image_index = 0  
    else:
        image_index = image_index + 1
    imgOnDisplay = load_image(image_index)
    image_label.config(image=imgOnDisplay)
next_btn = tk.Button(right1, text="Next Image", command=next_image)
next_btn.grid(row=2, column=0, pady=10)


restart_btn = tk.Button(right2, text="Restart", width=10, command=lambda: print("Restart clicked"))
restart_btn.grid(row=1, column=0, pady=10)

def exit_app():
    root.destroy()  
exit_btn = tk.Button(right2, text="Exit", width=10, fg="white", bg="red", command=exit_app)
exit_btn.grid(row=1, column=1, pady=10)

root.mainloop()