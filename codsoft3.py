import tkinter as tk
from random import choice

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("400x300")

       
        self.score_frame = tk.Frame(self.window, bg="gray")
        self.score_frame.pack()

        self.user_score = 0
        self.computer_score = 0

        self.user_score_label = tk.Label(self.score_frame, text="User Score: 0", font=("Arial", 20), bg="gray")
        self.user_score_label.pack(side=tk.LEFT)

        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Arial", 20), bg="gray")
        self.computer_score_label.pack(side=tk.RIGHT)

        
        self.button_frame = tk.Frame(self.window, bg="gray")
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play("rock"), width=10, height=2, font=("Arial", 15))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play("paper"), width=10, height=2, font=("Arial", 15))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play("scissors"), width=10, height=2, font=("Arial", 15))
        self.scissors_button.pack(side=tk.LEFT)

        
        self.result_label = tk.Label(self.window, text="", font=("Arial", 20), wraplength=400)
        self.result_label.pack()

    def play(self, user_choice):
        computer_choice = choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        self.update_scores(result)
        self.display_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "User wins"
        else:
            return "Computer wins"

    def update_scores(self, result):
        if result == "User wins":
            self.user_score += 1
        elif result == "Computer wins":
            self.computer_score += 1
        self.user_score_label['text'] = f"User Score: {self.user_score}"
        self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"

    def display_result(self, user_choice, computer_choice, result):
        if result == "User wins":
            self.window.configure(bg="orange")
            self.score_frame.configure(bg="orange")
            self.button_frame.configure(bg="orange")
            self.result_label.configure(bg="orange", fg="black")
        elif result == "Computer wins":
            self.window.configure(bg="red")
            self.score_frame.configure(bg="red")
            self.button_frame.configure(bg="red")
            self.result_label.configure(bg="red", fg="white")
        else:
            self.window.configure(bg="yellow")
            self.score_frame.configure(bg="yellow")
            self.button_frame.configure(bg="yellow")
            self.result_label.configure(bg="yellow", fg="black")
        self.result_label['text'] = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()
