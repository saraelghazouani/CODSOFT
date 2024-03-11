import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x400")
root.config(background="gray")

label_task = tk.Label(root, text="Enter a task:", font=("Arial", 12), bg="gray")
label_task.pack(pady=3)

entry_task = tk.Entry(root, width=60)
entry_task.pack(pady=5)

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10, padx=2)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=70)
listbox_tasks.pack(side="left")

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_tasks.config(command=listbox_tasks.yview)
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

button_add_task = tk.Button(root, text="Add Task", width=58, command=add_task,background="pink")
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", width=58, command=delete_task,background="pink")
button_delete_task.pack()

root.mainloop()
