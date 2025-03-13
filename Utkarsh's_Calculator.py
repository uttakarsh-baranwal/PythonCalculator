import tkinter as tk

# Entering values either number or operators
def button_click(value):
    entry.insert(tk.END, value)

# Calculating the equation provided
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")
        entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
        root.after(1000, lambda: (entry.delete(0, tk.END), entry.config(highlightthickness=0)))

# Just clearing the whole equation
def clear():
    entry.delete(0, tk.END)

# This will delete the most recent input
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Calculator window
root = tk.Tk()
root.title("Utkarsh's Calculator")
root.geometry("300x400")

# Input Output Widget
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
def create_button(text, row, col, width=1, command=None):
    button = tk.Button(root, text=text, width=5 * width, height=2, font=("Arial", 14), command=command)
    button.grid(row=row, column=col, columnspan=width, padx=5, pady=5)

# All buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 3), ('⌫', 5, 3)  # Backspace button
]

# Adding buttons accordingly
for text, row, col, *width in buttons:
    command = (lambda t=text: button_click(t)) if text not in {'=', 'C', '⌫'} else None
    if text == '=':
        create_button(text, row, col, command=calculate)
    elif text == 'C':
        create_button(text, row, col, width=3, command=clear)
    elif text == '⌫':
        create_button(text, row, col, command=backspace)
    else:
        create_button(text, row, col, command=command)

# Start the loop
root.mainloop()