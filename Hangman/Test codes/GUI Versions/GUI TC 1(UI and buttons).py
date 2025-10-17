import tkinter as tk
from tkinter import messagebox

#main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

#ui texts
label = tk.Label(root, text="Welcome to my GUI!")
label.pack(pady=10)

#click me button function
def say_hello():
    messagebox.showinfo("Hello", "You clicked the button!")
#click Me button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)


#exit button function
def exit_app():
    root.destroy()
#exit button
exit_button = tk.Button(root, text="Exit", command=exit_app, fg="white", bg="red")
exit_button.pack(pady=10)

#GUI loop
root.mainloop()
