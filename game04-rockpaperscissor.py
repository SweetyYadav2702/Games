import tkinter as tk
import random as rand


choices = ["rock", "paper", "scissor"]


def play(human):
    computer = rand.choice(choices)

    if human == computer:
        result.config(text="Computer: " + computer + "\nIt's a Tie!")

    elif human == "rock" and computer == "scissor":
        result.config(text="Computer: " + computer + "\nHuman Wins!")

    elif human == "paper" and computer == "rock":
        result.config(text="Computer: " + computer + "\nHuman Wins!")

    elif human == "scissor" and computer == "paper":
        result.config(text="Computer: " + computer + "\nHuman Wins!")

    else:
        result.config(text="Computer: " + computer + "\nComputer Wins!")


def rock():
    play("rock")


def paper():
    play("paper")


def scissor():
    play("scissor")


window = tk.Tk()

window.title("Rock, Paper and Scissor Game")
window.geometry("500x400")

tk.Button(window, text="Rock", command=rock).pack(
    side="left", padx=10
)

tk.Button(window, text="Paper", command=paper).pack(
    side="left", padx=10
)

tk.Button(window, text="Scissor", command=scissor).pack(
    side="left", padx=10
)

result = tk.Label(window, text="Choose your option")
result.pack(pady=100)

window.mainloop()