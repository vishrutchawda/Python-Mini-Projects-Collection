import tkinter as tk
import pygame
import snake_game as sg
import banking_system as bs
import dot_matrix_printer as dmp
import game as gm
import train as tr
import rock_paper_scissors as rps


def start_snake_game():
    print("Snake Game selected")
    sg.run()
    return root.mainloop()
def start_train():
    print("Train selected")
    tr.run()
    return root.mainloop()
def start_banking_system():
    print("Banking System selected")
    bs.run()
    return root.mainloop()
def start_dot_matrix_printer():
    print("Dot Matrix Printer selected")
    dmp.run()
    return root.mainloop()

def start_game():
    print("Game selected")
    gm.run()
    return root.mainloop()

def start_rock_paper_scissors():
    print("Rock Paper Scissors selected")
    rps.run()
    return root.mainloop()

root = tk.Tk()
root.title("Select an Option")
root.geometry("300x370")


btn_snake = tk.Button(root, text="Snake Game", command=start_snake_game, width=20, height=2)
btn_train = tk.Button(root, text="Train", command=start_train, width=20, height=2)
btn_banking = tk.Button(root, text="Banking System", command=start_banking_system, width=20, height=2)
btn_printer = tk.Button(root, text="Dot Matrix Printer", command=start_dot_matrix_printer, width=20, height=2)
btn_game = tk.Button(root, text="Game", command=start_game, width=20, height=2)
btn_rock = tk.Button(root, text="Rock Paper Scissors", command=start_rock_paper_scissors, width=20, height=2)

btn_snake.pack(pady=10)
btn_train.pack(pady=10)
btn_banking.pack(pady=10)
btn_printer.pack(pady=10)
btn_game.pack(pady=10)
btn_rock.pack(pady=10)

root.mainloop()


pygame.quit()