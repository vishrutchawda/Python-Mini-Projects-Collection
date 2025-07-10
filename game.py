import tkinter as tk
from tkinter import messagebox

def run():
    class NumberGame:
        def __init__(self, root):
            self.root = root
            self.root.title("Number Game")
            self.total_score = 0

            self.root.geometry("800x400")
            self.root.configure(bg='#f0f0f0')

            self.main_frame = tk.Frame(root, bg='#f0f0f0')
            self.main_frame.pack(pady=20)

            self.input_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
            self.input_frame.pack(side=tk.LEFT, padx=20)

            tk.Label(self.input_frame, text="Enter a number (1-10):", font=("Helvetica", 16), bg='#f0f0f0').pack(pady=5)

            self.user_input = tk.Entry(self.input_frame, width=10, font=("Helvetica", 18))
            self.user_input.pack(pady=10)
            self.user_input.bind("<Return>", self.process_user_choice)


            self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.process_user_choice, font=("Helvetica", 16), bg='#007ACC', fg='white')
            self.submit_button.pack(pady=10)

            self.score_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
            self.score_frame.pack(side=tk.LEFT, padx=20)


            self.score_label = tk.Label(self.score_frame, text="Total Score: 0", font=("Helvetica", 18), bg='#f0f0f0')
            self.score_label.pack(pady=5)

            self.computer_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
            self.computer_frame.pack(side=tk.LEFT, padx=20)

            self.computer_label = tk.Label(self.computer_frame, text="Computer's Choice: ", font=("Helvetica", 14), bg='#f0f0f0')
            self.computer_label.pack(pady=5)

            self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Helvetica", 16), bg='#FF6F61', fg='white')
            self.reset_button.pack(pady=20)

        def process_user_choice(self, event=None):
            try:
                user_choice = int(self.user_input.get())
                if user_choice < 1 or user_choice > 10:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Invalid Input", "Enter a number between 1 and 10.")
                return

            self.total_score += user_choice
            self.update_score()
            self.user_input.delete(0, tk.END)

            if self.total_score >= 100:
                self.computer_label.config(text="You have won!")
                self.submit_button.config(state=tk.DISABLED)
                return

            computer_choice = self.get_computer_choice()
            self.total_score += computer_choice
            self.computer_label.config(text=f"Computer's Choice: {computer_choice}")

            self.update_score()

            if self.total_score >= 100:
                self.computer_label.config(text="Computer has won!")
                self.submit_button.config(state=tk.DISABLED)

        def get_computer_choice(self):
            if self.total_score == 1:
                return 1
            elif self.total_score == 2:
                return 10
            elif self.total_score == 3:
                return 9
            elif self.total_score == 4:
                return 8
            elif self.total_score == 5:
                return 7
            elif self.total_score == 6:
                return 6
            elif self.total_score == 7:
                return 5
            elif self.total_score == 8:
                return 4
            elif self.total_score == 9:
                return 3
            elif self.total_score == 10:
                return 2
            elif self.total_score == 11:
                return 1
            elif self.total_score == 12:
                return 1
            elif self.total_score == 13:
                return 10
            elif self.total_score == 14:
                return 9
            elif self.total_score == 15:
                return 8
            elif self.total_score == 16:
                return 7
            elif self.total_score == 17:
                return 6
            elif self.total_score == 18:
                return 5
            elif self.total_score == 19:
                return 4
            elif self.total_score == 20:
                return 3
            elif self.total_score == 21:
                return 2
            elif self.total_score == 22:
                return 1
            elif self.total_score == 23:
                return 1
            elif self.total_score == 24:
                return 10
            elif self.total_score == 25:
                return 9
            elif self.total_score == 26:
                return 8
            elif self.total_score == 27:
                return 7
            elif self.total_score == 28:
                return 6
            elif self.total_score == 29:
                return 5
            elif self.total_score == 30:
                return 4
            elif self.total_score == 31:
                return 3
            elif self.total_score == 32:
                return 2
            elif self.total_score == 33:
                return 1
            elif self.total_score == 34:
                return 1
            elif self.total_score == 35:
                return 10
            elif self.total_score == 36:
                return 9
            elif self.total_score == 37:
                return 8
            elif self.total_score == 38:
                return 7
            elif self.total_score == 39:
                return 6
            elif self.total_score == 40:
                return 5
            elif self.total_score == 41:
                return 4
            elif self.total_score == 42:
                return 3
            elif self.total_score == 43:
                return 2
            elif self.total_score == 44:
                return 1
            elif self.total_score == 45:
                return 1
            elif self.total_score == 46:
                return 10
            elif self.total_score == 47:
                return 9
            elif self.total_score == 48:
                return 8
            elif self.total_score == 49:
                return 7
            elif self.total_score == 50:
                return 6
            elif self.total_score == 51:
                return 5
            elif self.total_score == 52:
                return 4
            elif self.total_score == 53:
                return 3
            elif self.total_score == 54:
                return 2
            elif self.total_score == 55:
                return 1
            elif self.total_score == 56:
                return 1
            elif self.total_score == 57:
                return 10
            elif self.total_score == 58:
                return 9
            elif self.total_score == 59:
                return 8
            elif self.total_score == 60:
                return 7
            elif self.total_score == 61:
                return 6
            elif self.total_score == 62:
                return 5
            elif self.total_score == 63:
                return 4
            elif self.total_score == 64:
                return 3
            elif self.total_score == 65:
                return 2
            elif self.total_score == 66:
                return 1
            elif self.total_score == 67:
                return 1
            elif self.total_score == 68:
                return 10
            elif self.total_score == 69:
                return 9
            elif self.total_score == 70:
                return 8
            elif self.total_score == 71:
                return 7
            elif self.total_score == 72:
                return 6
            elif self.total_score == 73:
                return 5
            elif self.total_score == 74:
                return 4
            elif self.total_score == 75:
                return 3
            elif self.total_score == 76:
                return 2
            elif self.total_score == 77:
                return 1
            elif self.total_score == 78:
                return 1
            elif self.total_score == 79:
                return 10
            elif self.total_score == 80:
                return 9
            elif self.total_score == 81:
                return 8
            elif self.total_score == 82:
                return 7
            elif self.total_score == 83:
                return 6
            elif self.total_score == 84:
                return 5
            elif self.total_score == 85:
                return 4
            elif self.total_score == 86:
                return 3
            elif self.total_score == 87:
                return 2
            elif self.total_score == 88:
                return 1
            elif self.total_score == 90:
                return 10
            elif self.total_score == 91:
                return 9
            elif self.total_score == 92:
                return 8
            elif self.total_score == 93:
                return 7
            elif self.total_score == 94:
                return 6
            elif self.total_score == 95:
                return 5
            elif self.total_score == 96:
                return 4
            elif self.total_score == 97:
                return 3
            elif self.total_score == 98:
                return 2
            elif self.total_score == 99:
                return 1

        def update_score(self):
            self.score_label.config(text=f"Total Score: {self.total_score}")

        def reset_game(self):
            self.total_score = 0
            self.update_score()
            self.computer_label.config(text="Computer's Choice: ")
            self.submit_button.config(state=tk.NORMAL)

    root = tk.Tk()
    game = NumberGame(root)
    root.mainloop()

if __name__ == "__main__":
    run()