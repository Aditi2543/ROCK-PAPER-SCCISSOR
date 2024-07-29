import tkinter as tk
from tkinter import messagebox
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("350x350")
        self.window.configure(bg="lightcoral")

        self.user_score = 0
        self.computer_score = 0
        self.round_number = 1

        self.user_score_label = tk.Label(self.window, text="User Score: 0", bg="lightcoral", fg="black")
        self.user_score_label.pack()

        self.computer_score_label = tk.Label(self.window, text="Computer Score: 0", bg="lightcoral", fg="black")
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.window, text="", bg="lightcoral", fg="black")
        self.result_label.pack()

        self.round_label = tk.Label(self.window, text="Current Round: 1", bg="lightcoral", fg="black")
        self.round_label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.make_move("rock"), bg="gray", fg="white")
        self.rock_button.pack(pady=5)
        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.make_move("paper"), bg="gray", fg="white")
        self.paper_button.pack(pady=5)
        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.make_move("scissors"), bg="gray", fg="white")
        self.scissors_button.pack(pady=5)

    def make_move(self, user_choice):
        computer_choice = choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "Tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win this round!"
            self.user_score += 1
        else:
            result = "Computer wins this round!"
            self.computer_score += 1

        self.result_label.config(text=f"{result} ({user_choice} vs {computer_choice})")
        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
        self.round_number += 1
        self.round_label.config(text=f"Current Round: {self.round_number}")

        if self.round_number > 10:
            self.show_final_result()
        elif self.user_score >= 10:
            messagebox.showinfo("Game Over", f"The final score is {self.user_score} - {self.computer_score}. You win! Goodbye!")
            self.ask_play_again()
        elif self.computer_score >= 10:
            messagebox.showinfo("Game Over", f"The final score is {self.user_score} - {self.computer_score}. Computer wins! Goodbye!")
            self.ask_play_again()

    def show_final_result(self):
        if self.user_score > self.computer_score:
            final_result = f"The final score is {self.user_score} - {self.computer_score}. You win!"
        elif self.user_score < self.computer_score:
            final_result = f"The final score is {self.user_score} - {self.computer_score}. Computer wins!"
        else:
            final_result = f"The final score is {self.user_score} - {self.computer_score}. It's a tie!"

        messagebox.showinfo("Game Over", final_result)
        self.ask_play_again()

    def ask_play_again(self):
        play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
        if play_again:
            self.reset_game()
        else:
            self.window.quit()

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.round_number = 1
        self.user_score_label.config(text="User Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.round_label.config(text="Current Round: 1")
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
