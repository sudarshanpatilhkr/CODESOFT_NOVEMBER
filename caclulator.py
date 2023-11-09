import tkinter as tk
from tkinter import messagebox

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid expression: {e}")

def clear_entry():
    entry.delete(0, tk.END)

def add_to_entry(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))


root = tk.Tk()
root.title("Calculator")

# Create and pack widgets
entry = tk.Entry(root, width=30, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]
#calculator funtions

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: add_to_entry(t))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=5, height=2, command=clear_entry)
clear_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2)

evaluate_button = tk.Button(root, text="=", width=12, height=2, command=evaluate_expression)
evaluate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
