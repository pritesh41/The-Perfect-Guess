import tkinter as tk
from tkinter import messagebox
import random

# Function to check the user's guess
def check_guess():
    try:
        guess = int(entry.get())
        
        if guess < 1 or guess > 100:
            messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100.")
            return
        
        global guess_count
        guess_count += 1
        
        if guess < number:
            result_label.config(text="It's lower than my number, try again! 🥱")
        elif guess > number:
            result_label.config(text="It's higher than my number, try again! 🥱")
        else:
            result_label.config(text=f"Congrats! You guessed the number in {guess_count} attempts! 👏")
            messagebox.showinfo("Congratulations", f"You've won the game in {guess_count} attempts!")
            reset_game()
            
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global number, guess_count
    number = random.randint(1, 100)
    guess_count = 0
    entry.delete(0, tk.END)
    result_label.config(text="")

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Set the window size
root.geometry("300x200")

# Create widgets
instruction_label = tk.Label(root, text="Guess a number between 1 and 100")
instruction_label.pack(pady=10)

entry = tk.Entry(root, width=10)
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start a new game
reset_game()

# Run the application
root.mainloop()
