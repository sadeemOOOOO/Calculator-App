"""
Authors: Sadeem, Lamar, Farah
"""

import tkinter as tk
import math

memory = 0


def memory_add():
    global memory
    try:
        memory += eval(entry_var.get())
    except Exception as e:
        entry_var.set("Error")


def memory_subtract():
    global memory
    try:
        memory -= eval(entry_var.get())
    except Exception as e:
        entry_var.set("Error")


def memory_recall():
    entry_var.set(str(memory))


def memory_clear():
    global memory
    memory = 0


def on_button_click(character):
    entry_var.set(entry_var.get() + character)


def evaluate_expression():
    expression = entry_var.get()
    try:
        result = custom_eval(expression)
        history.insert(tk.END, f"{expression} = {result}")
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")


def custom_eval(expression):
    expression = expression.replace('^', '**')

    expression = expression.replace('π', 'math.pi')
    expression = expression.replace('e', 'math.e')
    expression = expression.replace('log', 'math.log10')
    expression = expression.replace('ln', 'math.log')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')

    return eval(expression)


def clear_entry():
    entry_var.set("")


root = tk.Tk()
root.title("Scientific Calculator")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 16), bd=10, insertwidth=2, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('(', 4, 1), (')', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('M+', 5, 1), ('M-', 5, 2), ('=', 5, 3),
    ('MR', 6, 0), ('MC', 6, 1), ('sin', 6, 2), ('cos', 6, 3),
    ('tan', 7, 0), ('log', 7, 1), ('ln', 7, 2), ('.', 7, 3),
    ('=', 8, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=clear_entry)
    elif text == 'M+':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=memory_add)
    elif text == 'M-':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=memory_subtract)
    elif text == 'MR':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=memory_recall)
    elif text == 'MC':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=memory_clear)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, sticky='nsew')

for i in range(6):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

# History panel
history_label = tk.Label(root, text="History", font=('Arial', 16))
history_label.grid(row=9, column=0, columnspan=4, sticky='nsew')
history = tk.Listbox(root, height=5, font=('Arial', 12))
history.grid(row=10, column=0, columnspan=4, sticky='nsew')

root.mainloop()
