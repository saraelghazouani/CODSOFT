import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.config(bg="lightgrey")

entry_input = tk.Entry(root, width=20, font=('Arial', 18))
entry_input.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

def clear():
    entry_input.delete(0, tk.END)

tk.Button(root, text="Clear", width=5, font=('Arial', 12), bg="black", command=clear, fg="white").grid(row=5, column=0, columnspan=2, padx=5, pady=5)
def update_input(value):
    current = entry_input.get()
    entry_input.delete(0, tk.END)
    entry_input.insert(0, current + value)

def calculate():
    expression = entry_input.get()
    try:
        result = eval(expression)
        entry_input.delete(0, tk.END)
        entry_input.insert(0, str(result))
    except Exception as e:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, "Error")


buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', '.', '=', '/'
]

row_num = 1
col_num = 0

for button in buttons:
    butt = tk.Button(root, text=button, width=5, font=('Arial', 14), bg="pink", command=lambda value=button: update_input(value) if value != '=' else calculate())
    butt.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


root.mainloop()
