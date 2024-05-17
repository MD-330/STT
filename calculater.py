import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set the background color to purple
root.configure(background='purple')

# Create a style for the buttons
style = ttk.Style()
style.configure("TButton", background="purple", foreground="white", font=("Helvetica", 12, "bold"))
style.map("TButton",
          background=[('active', 'grey')],
          foreground=[('active', 'white')])

# Create the display widget
display = tk.Entry(root, font=("Helvetica", 20), borderwidth=5, relief="ridge")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the display
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

# Function to clear the display
def button_clear():
    display.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Function to change button color on hover
def on_enter(e):
    e.widget['background'] = 'grey'

def on_leave(e):
    e.widget['background'] = 'purple'

# Create the calculator buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add the buttons to the calculator
for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=button_equal, style="TButton")
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t), style="TButton")
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Add a clear button
clear_button = ttk.Button(root, text="C", command=button_clear, style="TButton")
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

# Make the buttons expand equally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the main loop
root.mainloop()