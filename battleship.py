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

# which player is making move
player = StringVar()
player.set('first')
Radiobutton(frame3, text="Player1", variable=player, value='first').grid(row=0, column=0)
Radiobutton(frame3, text="Player2", variable=player, value='second').grid(row=0, column=1)

# drop menu for ships
clicked = StringVar()
clicked.set("carrier        ")

options = OptionMenu(frame3, clicked, "carrier        ", "battle-ship", "cruiser       ", "submarine", "destroyer   ")
options.grid(row=1, column=0)

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

# row 1
p1_A1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A1", p1_A1))
p1_A1.grid(row=1, column=1)
p1_A2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A2", p1_A2))
p1_A2.grid(row=1, column=2)
p1_A3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A3", p1_A3))
p1_A3.grid(row=1, column=3)
p1_A4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A4", p1_A4))
p1_A4.grid(row=1, column=4)
p1_A5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A5", p1_A5))
p1_A5.grid(row=1, column=5)
p1_A6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A6", p1_A6))
p1_A6.grid(row=1, column=6)
p1_A7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A7", p1_A7))
p1_A7.grid(row=1, column=7)
p1_A8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A8", p1_A8))
p1_A8.grid(row=1, column=8)
p1_A9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "A9", p1_A9))
p1_A9.grid(row=1, column=9)
p1_A10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "A10", p1_A10))
p1_A10.grid(row=1, column=10)
# row 2
p1_B1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B1", p1_B1))
p1_B1.grid(row=2, column=1)
p1_B2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B2", p1_B2))
p1_B2.grid(row=2, column=2)
p1_B3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B3", p1_B3))
p1_B3.grid(row=2, column=3)
p1_B4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B4", p1_B4))
p1_B4.grid(row=2, column=4)
p1_B5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B5", p1_B5))
p1_B5.grid(row=2, column=5)
p1_B6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B6", p1_B6))
p1_B6.grid(row=2, column=6)
p1_B7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B7", p1_B7))
p1_B7.grid(row=2, column=7)
p1_B8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B8", p1_B8))
p1_B8.grid(row=2, column=8)
p1_B9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "B9", p1_B9))
p1_B9.grid(row=2, column=9)
p1_B10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "B10", p1_B10))
p1_B10.grid(row=2, column=10)

# row 3
p1_C1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C1", p1_C1))
p1_C1.grid(row=3, column=1)
p1_C2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C2", p1_C2))
p1_C2.grid(row=3, column=2)
p1_C3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C3", p1_C3))
p1_C3.grid(row=3, column=3)
p1_C4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C4", p1_C4))
p1_C4.grid(row=3, column=4)
p1_C5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C5", p1_C5))
p1_C5.grid(row=3, column=5)
p1_C6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C6", p1_C6))
p1_C6.grid(row=3, column=6)
p1_C7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C7", p1_C7))
p1_C7.grid(row=3, column=7)
p1_C8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C8", p1_C8))
p1_C8.grid(row=3, column=8)
p1_C9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "C9", p1_C9))
p1_C9.grid(row=3, column=9)
p1_C10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "C10", p1_C10))
p1_C10.grid(row=3, column=10)
# row 4
p1_D1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D1", p1_D1))
p1_D1.grid(row=4, column=1)
p1_D2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D2", p1_D2))
p1_D2.grid(row=4, column=2)
p1_D3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D3", p1_D3))
p1_D3.grid(row=4, column=3)
p1_D4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D4", p1_D4))
p1_D4.grid(row=4, column=4)
p1_D5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D5", p1_D5))
p1_D5.grid(row=4, column=5)
p1_D6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D6", p1_D6))
p1_D6.grid(row=4, column=6)
p1_D7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D7", p1_D7))
p1_D7.grid(row=4, column=7)
p1_D8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D8", p1_D8))
p1_D8.grid(row=4, column=8)
p1_D9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "D9", p1_D9))
p1_D9.grid(row=4, column=9)
p1_D10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "D10", p1_D10))
p1_D10.grid(row=4, column=10)
# row 5
p1_E1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E1", p1_E1))
p1_E1.grid(row=5, column=1)
p1_E2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E2", p1_E2))
p1_E2.grid(row=5, column=2)
p1_E3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E3", p1_E3))
p1_E3.grid(row=5, column=3)
p1_E4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E4", p1_E4))
p1_E4.grid(row=5, column=4)
p1_E5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E5", p1_E5))
p1_E5.grid(row=5, column=5)
p1_E6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E6", p1_E6))
p1_E6.grid(row=5, column=6)
p1_E7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E7", p1_E7))
p1_E7.grid(row=5, column=7)
p1_E8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E8", p1_E8))
p1_E8.grid(row=5, column=8)
p1_E9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "E9", p1_E9))
p1_E9.grid(row=5, column=9)
p1_E10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "E10", p1_E10))
p1_E10.grid(row=5, column=10)
# row 6
p1_F1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F1", p1_F1))
p1_F1.grid(row=6, column=1)
p1_F2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F2", p1_F2))
p1_F2.grid(row=6, column=2)
p1_F3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F3", p1_F3))
p1_F3.grid(row=6, column=3)
p1_F4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F4", p1_F4))
p1_F4.grid(row=6, column=4)
p1_F5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F5", p1_F5))
p1_F5.grid(row=6, column=5)
p1_F6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F6", p1_F6))
p1_F6.grid(row=6, column=6)
p1_F7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F7", p1_F7))
p1_F7.grid(row=6, column=7)
p1_F8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F8", p1_F8))
p1_F8.grid(row=6, column=8)
p1_F9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "F9", p1_F9))
p1_F9.grid(row=6, column=9)
p1_F10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "F10", p1_F10))
p1_F10.grid(row=6, column=10)
# row 7
p1_G1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G1", p1_G1))
p1_G1.grid(row=7, column=1)
p1_G2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G2", p1_G2))
p1_G2.grid(row=7, column=2)
p1_G3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G3", p1_G3))
p1_G3.grid(row=7, column=3)
p1_G4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G4", p1_G4))
p1_G4.grid(row=7, column=4)
p1_G5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G5", p1_G5))
p1_G5.grid(row=7, column=5)
p1_G6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G6", p1_G6))
p1_G6.grid(row=7, column=6)
p1_G7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G7", p1_G7))
p1_G7.grid(row=7, column=7)
p1_G8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G8", p1_G8))
p1_G8.grid(row=7, column=8)
p1_G9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "G9", p1_G9))
p1_G9.grid(row=7, column=9)
p1_G10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "G10", p1_G10))
p1_G10.grid(row=7, column=10)
# row 8
p1_H1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H1", p1_H1))
p1_H1.grid(row=8, column=1)
p1_H2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H2", p1_H2))
p1_H2.grid(row=8, column=2)
p1_H3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H3", p1_H3))
p1_H3.grid(row=8, column=3)
p1_H4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H4", p1_H4))
p1_H4.grid(row=8, column=4)
p1_H5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H5", p1_H5))
p1_H5.grid(row=8, column=5)
p1_H6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H6", p1_H6))
p1_H6.grid(row=8, column=6)
p1_H7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H7", p1_H7))
p1_H7.grid(row=8, column=7)
p1_H8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H8", p1_H8))
p1_H8.grid(row=8, column=8)
p1_H9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H9", p1_H9))
p1_H9.grid(row=8, column=9)
p1_H0 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "H10", p1_H0))
p1_H0.grid(row=8, column=10)
# row 9
p1_I1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I1", p1_I1))
p1_I1.grid(row=9, column=1)
p1_I2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I2", p1_I2))
p1_I2.grid(row=9, column=2)
p1_I3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I3", p1_I3))
p1_I3.grid(row=9, column=3)
p1_I4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I4", p1_I4))
p1_I4.grid(row=9, column=4)
p1_I5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I5", p1_I5))
p1_I5.grid(row=9, column=5)
p1_I6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I6", p1_I6))
p1_I6.grid(row=9, column=6)
p1_I7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I7", p1_I7))
p1_I7.grid(row=9, column=7)
p1_I8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I8", p1_I8))
p1_I8.grid(row=9, column=8)
p1_I9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "I9", p1_I9))
p1_I9.grid(row=9, column=9)
p1_I10 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
                command=lambda: s.fire_torpedo("first", "I10", p1_I10))
p1_I10.grid(row=9, column=10)
# row 10
p1_J1 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J1", p1_J1))
p1_J1.grid(row=10, column=1)
p1_J2 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J2", p1_J2))
p1_J2.grid(row=10, column=2)
p1_J3 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J3", p1_J3))
p1_J3.grid(row=10, column=3)
p1_J4 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J4", p1_J4))
p1_J4.grid(row=10, column=4)
p1_J5 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J5", p1_J5))
p1_J5.grid(row=10, column=5)
p1_J6 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J6", p1_J6))
p1_J6.grid(row=10, column=6)
p1_J7 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J7", p1_J7))
p1_J7.grid(row=10, column=7)
p1_J8 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J8", p1_J8))
p1_J8.grid(row=10, column=8)
p1_J9 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J9", p1_J9))
p1_J9.grid(row=10, column=9)
p1_J0 = Button(frame1, text=" ", font=("Helvetica", 10), height=1, width=2, bg="SystemButtonFace",
               command=lambda: s.fire_torpedo("first", "J10", p1_J0))
p1_J0.grid(row=10, column=10)

# Player2 board
# grid coordinates - alphabet
a_label = Label(frame2, text="A")
a_label.grid(row=1, column=0)
b_label = Label(frame2, text="B")
b_label.grid(row=2, column=0)
c_label = Label(frame2, text="C")
c_label.grid(row=3, column=0)
d_label = Label(frame2, text="D")
d_label.grid(row=4, column=0)
e_label = Label(frame2, text="E")
e_label.grid(row=5, column=0)
f_label = Label(frame2, text="F")
f_label.grid(row=6, column=0)
g_label = Label(frame2, text="G")
g_label.grid(row=7, column=0)
h_label = Label(frame2, text="H")
h_label.grid(row=8, column=0)
i_label = Label(frame2, text="I")
i_label.grid(row=9, column=0)
j_label = Label(frame2, text="J")
j_label.grid(row=10, column=0)

# grid coordinates - digits
blank_label3 = Label(frame2, text=" ")
blank_label3.grid(row=0, column=0)
label_1 = Label(frame2, text="1")
label_1.grid(row=0, column=1)
label_2 = Label(frame2, text="2")
label_2.grid(row=0, column=2)
label_3 = Label(frame2, text="3")
label_3.grid(row=0, column=3)
label_4 = Label(frame2, text="4")
label_4.grid(row=0, column=4)
label_5 = Label(frame2, text="5")
label_5.grid(row=0, column=5)
label_6 = Label(frame2, text="6")
label_6.grid(row=0, column=6)
label_7 = Label(frame2, text="7")
label_7.grid(row=0, column=7)
label_8 = Label(frame2, text="8")
label_8.grid(row=0, column=8)
label_9 = Label(frame2, text="9")
label_9.grid(row=0, column=9)
label_10 = Label(frame2, text="10")
label_10.grid(row=0, column=10)

root.mainloop()
