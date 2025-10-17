import tkinter as tk

root = tk.Tk()
root.title("Hangman: A word guessing game")
root.geometry("1280x780")

#grid layout
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

#frames
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

#labels in frames
tk.Label(left1, text="Guessed letters:").pack(pady=10)
tk.Label(left2, text="Attempts left:\n Word _ _ _ _").pack(pady=10)
tk.Label(left3, text="Enter a Letter").pack(pady=10)
tk.Label(right1, text="Hangman png").pack(pady=10)
tk.Label(right2, text="Re & Q").pack(pady=10)

root.mainloop()