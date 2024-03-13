import tkinter as tk
from tkinter import messagebox
import random
import string
from tkinter import PhotoImage
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive integer for password length.")
        else:
            password = generate_password(length)
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

def copy_password():
    password = entry_password.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x500")
root.config(bg="white")

image_color = "#0077b6"

label_text = tk.Label(root, text=" Random Password Generator", font=("Helvetica", 20), foreground=image_color, background="white")
label_text.pack(fill=tk.X,pady=10)

image = PhotoImage(file=r"C:\Users\Hp\PycharmProjects\Password generator\image.png")
image = image.subsample(2)
label_image = tk.Label(root, image=image, bg="white")
label_image.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(root, width=700, height=1000, bg=image_color)
frame.pack(expand=True, padx=1)

label_length = tk.Label(frame, text="Password Length:", bg=image_color)
label_length.grid(row=0, column=0, padx=5, pady=5)

entry_length = tk.Entry(frame, width=40)
entry_length.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

button_generate = tk.Button(frame, text="Generate Password", command=generate_and_display_password, background="black", foreground="white", bd=1, width=15)
button_generate.grid(row=2, column=0, padx=5, pady=5)

button_copy = tk.Button(frame, text="Copy Password", command=copy_password, background="black", foreground="white", bd=1, width=15)
button_copy.grid(row=2, column=1, padx=5, pady=5)

label_password = tk.Label(frame, text="Generated Password:", bg=image_color)
label_password.grid(row=3, column=0, columnspan=2, pady=5)

entry_password = tk.Entry(frame, width=40)
entry_password.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
