import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
from tkinter import PhotoImage
def play(user_choice):
    if user_choice not in ['rock', 'paper', 'scissors']:
        messagebox.showerror("Error", "Invalid choice. Please enter rock, paper, or scissors.")
        return

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result_label.config(text=f"You chose: {user_choice.capitalize()}\nComputer chose: {computer_choice.capitalize()}", fg='blue')

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
        user_score_var.set(user_score_var.get() + 1)
    else:
        result = "Computer wins!"
        computer_score_var.set(computer_score_var.get() + 1)

    messagebox.showinfo("Result", result)
    update_scores()

def update_scores():
    score_label.config(text=f"Your score: {user_score_var.get()}\nComputer's score: {computer_score_var.get()}", fg='green', font=("Helvetica", 12))
    scores.append((user_score_var.get(), computer_score_var.get()))
    scores_table.delete(*scores_table.get_children())
    for i, (user_score, computer_score) in enumerate(scores, start=1):
        scores_table.insert("", "end", values=(i, user_score, computer_score))

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x600")
root.config(bg="gray")

Image = PhotoImage(file=r"C:\Users\Hp\PycharmProjects\Rock-Paper-Scissors Game\yy.png")
image_label = tk.Label(root, image=Image)
image_label.pack()

user_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
scores = []

label = tk.Label(root, text="Choose:", fg='gray', font=("Helvetica", 14))
label.pack()

button_frame = tk.Frame(root,bg="gray")
button_frame.pack()

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"), bg='black', fg='white', font=("Helvetica", 12))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"), bg='black', fg='white', font=("Helvetica", 12))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"), bg='black', fg='white', font=("Helvetica", 12))
scissors_button.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

score_label = tk.Label(root, text="", font=("Helvetica", 12))
score_label.pack()

# Create a scrollable table for displaying scores
scores_frame = tk.Frame(root)
scores_frame.pack(pady=10)

scores_table = ttk.Treeview(scores_frame, columns=('Round', 'Your Score', 'Computer Score'), show='headings')
scores_table.heading('Round', text='Round')
scores_table.heading('Your Score', text='Your Score')
scores_table.heading('Computer Score', text='Computer Score')
scores_table.pack(side=tk.LEFT, fill=tk.Y)

scores_scroll = tk.Scrollbar(scores_frame, orient=tk.VERTICAL, command=scores_table.yview)
scores_scroll.pack(side=tk.RIGHT, fill=tk.Y)

scores_table.configure(yscrollcommand=scores_scroll.set)

update_scores()

root.mainloop()
