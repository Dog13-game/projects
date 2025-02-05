

import tkinter as tk

def greet():
    name = entry.get()
    greeting_label.config(text=f"Привіт, {name}!") 


root = tk.Tk()
root.title("Вітальне вікно")


entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)


greet_button = tk.Button(root, text="Привітатись", command=greet, font=("Arial", 14))
greet_button.pack(pady=10)


greeting_label = tk.Label(root, font=("Arial", 14))
greeting_label.pack(pady=10)


root.mainloop() 
