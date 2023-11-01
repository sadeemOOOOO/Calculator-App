"""
Authors: Sadeem, Lamar, Farah
"""

import tkinter as tk


def on_button_click(character):
    entry_var.set(entry_var.get() + character)


def evaluate_expression():
    try:
        entry_var.set(eval(entry_var.get()))
    except Exception as e:
        entry_var.set("Error")


def clear_entry():
    entry_var.set("")


root = tk.Tk()
root.title("Classic Calculator")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 16), bd=10, insertwidth=2, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('(', 4, 1), (')', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('M+', 5, 1), ('M-', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear_entry)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky='nsew')

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

root.mainloop()
