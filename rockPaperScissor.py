import tkinter as tk
from tkinter import messagebox
import random

def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    result = determine_winner(user_choice, computer_choice)

    messagebox.showinfo("Result", f"Computer chose {computer_choice}\n{result}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
#game for codsoft
# Create and pack widgets
label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
