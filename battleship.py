from ship_game_classes import Ship, Player, ShipGame
from tkinter import *

s = ShipGame()

root = Tk()
root.geometry("750x550")
root.title('Battleship')

# frame for game board grids
frame1 = LabelFrame(root, text="Player1", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=10)
frame2 = LabelFrame(root, text="Player2", padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)

# frame for data input
frame3 = LabelFrame(root, text="Place Ship", padx=15, pady=15)
frame3.grid(row=1, column=0, padx=30, pady=20)

# frame for ships remaining
frame4 = LabelFrame(root, text="Ships Remaining", padx=15, pady=15)
frame4.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
