import random
import time
import tkinter as tk
from tkinter import messagebox

def run():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    def display_animation(label):
        animation = ["Rock", "Paper", "Scissors", "Shoot!"]
        for frame in animation:
            label.config(text=frame, font=("Helvetica", 16, "bold"), fg="blue")
            root.update()
            time.sleep(0.5)


    def choice(my_choice):
        my_choice = int(my_choice)
        my_choice -= 1
        computer_choice = random.randint(0, 2)

        choices = [rock, paper, scissors]

        result_label.config(text="Let's play...")
        display_animation(result_label)

        user_choice_display = f"Your Choice:\n{choices[my_choice]}"
        computer_choice_display = f"Computer's Choice:\n{choices[computer_choice]}"


        result_label.config(text="")
        choices_label.config(text=f"{user_choice_display}\n\n{computer_choice_display}", font=("Courier", 10))

        if my_choice < 0 or my_choice > 2:
            messagebox.showerror("Invalid Choice", "Please select a number between 1 and 3.")
            return


        if my_choice == computer_choice:
            result_label.config(text="It's a DRAW!", fg="orange", font=("Helvetica", 16, "bold"))
        elif (my_choice == 0 and computer_choice == 2) or (my_choice == 1 and computer_choice == 0) or (
                my_choice == 2 and computer_choice == 1):
            result_label.config(text="YOU WON!", fg="green", font=("Helvetica", 16, "bold"))
        else:
            result_label.config(text="YOU LOSE!", fg="red", font=("Helvetica", 16, "bold"))

    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")
    root.geometry("600x400")
    root.config(bg="#f0f0f0")


    heading_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 20), bg="#f0f0f0")
    heading_label.pack(pady=10)


    left_frame = tk.Frame(root, bg="#f0f0f0")
    left_frame.pack(side=tk.LEFT, padx=20)

    middle_frame = tk.Frame(root, bg="#f0f0f0")
    middle_frame.pack(side=tk.LEFT, padx=40)

    right_frame = tk.Frame(root, bg="#f0f0f0")
    right_frame.pack(side=tk.LEFT, padx=20)

    result_label = tk.Label(middle_frame, text="", font=("Helvetica", 12), bg="#f0f0f0", height=6)
    result_label.pack(pady=20)

    choices_label = tk.Label(right_frame, text="", font=("Courier", 10), bg="#f0f0f0", justify=tk.LEFT)
    choices_label.pack(pady=20)

    def rock_click():
        choice(1)

    def paper_click():
        choice(2)

    def scissors_click():
        choice(3)

    rock_button = tk.Button(left_frame, text="Rock", font=("Helvetica", 12), command=rock_click, bg="#ff6666", fg="white", width=10)
    rock_button.pack(pady=10)

    paper_button = tk.Button(left_frame, text="Paper", font=("Helvetica", 12), command=paper_click, bg="#66b3ff", fg="white", width=10)
    paper_button.pack(pady=10)

    scissors_button = tk.Button(left_frame, text="Scissors", font=("Helvetica", 12), command=scissors_click, bg="#ffcc66", fg="white", width=10)
    scissors_button.pack(pady=10)


    #exit_button = tk.Button(root, text="Exit", font=("Helvetica", 12), command=root.quit, bg="#cc66ff", fg="white", width=10)
    #exit_button.pack(side=tk.BOTTOM, pady=20)

    root.mainloop()

if __name__ == "__main__":
    run()