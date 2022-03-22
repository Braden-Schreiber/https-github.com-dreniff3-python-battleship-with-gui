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

# game board buttons

# Player1 board
# grid coordinates - alphabet
a_label = Label(frame1, text="A")
a_label.grid(row=1, column=0)
b_label = Label(frame1, text="B")
b_label.grid(row=2, column=0)
c_label = Label(frame1, text="C")
c_label.grid(row=3, column=0)
d_label = Label(frame1, text="D")
d_label.grid(row=4, column=0)
e_label = Label(frame1, text="E")
e_label.grid(row=5, column=0)
f_label = Label(frame1, text="F")
f_label.grid(row=6, column=0)
g_label = Label(frame1, text="G")
g_label.grid(row=7, column=0)
h_label = Label(frame1, text="H")
h_label.grid(row=8, column=0)
i_label = Label(frame1, text="I")
i_label.grid(row=9, column=0)
j_label = Label(frame1, text="J")
j_label.grid(row=10, column=0)

# grid coordinates - digits
blank_label2 = Label(frame1, text=" ")
blank_label2.grid(row=0, column=0)
label_1 = Label(frame1, text="1")
label_1.grid(row=0, column=1)
label_2 = Label(frame1, text="2")
label_2.grid(row=0, column=2)
label_3 = Label(frame1, text="3")
label_3.grid(row=0, column=3)
label_4 = Label(frame1, text="4")
label_4.grid(row=0, column=4)
label_5 = Label(frame1, text="5")
label_5.grid(row=0, column=5)
label_6 = Label(frame1, text="6")
label_6.grid(row=0, column=6)
label_7 = Label(frame1, text="7")
label_7.grid(row=0, column=7)
label_8 = Label(frame1, text="8")
label_8.grid(row=0, column=8)
label_9 = Label(frame1, text="9")
label_9.grid(row=0, column=9)
label_10 = Label(frame1, text="10")
label_10.grid(row=0, column=10)

root.mainloop()
