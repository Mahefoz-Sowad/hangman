import tkinter as tk
#pillow for image handling
from PIL import Image, ImageTk
#handles file paths
import os

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x600")

#img location
"""
os.getcwd() gets the current working directory, 
"Test codes\GUI Versions\hangmanHP" path to the image folder relative to the current directory.
os.path.join(x , y) is used to combine the path of both directories into a single path.
"""
image_folder = os.path.join(os.getcwd(), "Test codes\GUI Versions\hangmanHP")
"""list of image files
hangman0.png to hangman7.png
"""
"""easy way
image_files = [
    os.path.join(image_folder, "hangman0.png"),
    os.path.join(image_folder, "hangman1.png"),
    os.path.join(image_folder, "hangman2.png"),
    os.path.join(image_folder, "hangman3.png"),
    os.path.join(image_folder, "hangman4.png"),
    os.path.join(image_folder, "hangman5.png"),
    os.path.join(image_folder, "hangman6.png"),
    os.path.join(image_folder, "hangman7.png")
]
"""
images = [
    os.path.join(image_folder, f"hangman{x}.png") for x in range(8)
]

#variable to track image on display
image_index = 0

#function to load image
def load_image(index):
    img = Image.open(images[index]).resize((300, 300))
    return ImageTk.PhotoImage(img)

#displays the image
imgOnDisplay = load_image(image_index)
image_label = tk.Label(root, image=imgOnDisplay)
image_label.pack(pady=10)

#next image button's function
def next_image():
    global image_index, imgOnDisplay
    if image_index + 1 >= len(images):
        image_index = 0  
    else:
        image_index = image_index + 1
    imgOnDisplay = load_image(image_index)
    #updates the image in the label
    image_label.config(image=imgOnDisplay)
#next image button
next_button = tk.Button(root, text="Next Image", command=next_image)
next_button.pack(pady=10)

def exit_app():
    root.destroy()  
exit_button = tk.Button(root, text="Exit", command=exit_app, fg="white", bg="red")
exit_button.pack(pady=10)

root.mainloop()