# Battleship (with GUI) in Python

## Description

A Python program that allows two people to play the game Battleship, originally created as a school project, meant to be played in the terminal. During a break between quarters, I implemented a simple GUI for the game using Tkinter. I used Tkinter because it is built into the Python standard library, and because displaying an array of clickable buttons to represent the grid Battleship is played on is fairly trivial with Tkinter.

## Requirements

Python 3

Git

## Installation

1. Clone the repository to your own computer. 
2. ```cd``` into the directory where the code is located locally.
3. Run ```python battleship.py``` from command line.

## Play the game

Players place their ships on their hidden boards* by selecting a ship from the drop menu, entering into the text-box the letter-and-number coordinates of the closest square to 'A1' that the ship will occupy, and choosing the orientation, either "R" if the ship occupies squares in a row or "C" if it occupies squares in a column, by clicking the appropriate radiobutton before clicking the button labelled "Place the ship". 

After players have placed their ships, they take turns (starting with player 1) firing torpedoes by clicking on *their* grid of buttons (player 1 fires torpedoes on the grid in the frame labelled "Player1", and player 2 fires on the grid labelled "Player2"). When a torpedo hits an opponent's ship the square turns red and has an 'X' inside. When a torpedo misses, the square turns blue and has a 'O' inside.

To view the number of ships a player has remaining, choose the radiobutton for the player whose ships you wish to count and click the button labelled "Show ships". The number of ships will be printed inside that frame. 

*(if you must peak at the location of your ships, while the program is running enter ```s.print_board("first")``` if you are player 1 or ```s.print_board("second")``` if you are player 2 and a simple grid where ship positions are represented by X's will be printed in the terminal)

![battleship_example_sm](https://user-images.githubusercontent.com/85808475/159609537-6f5dcb39-4cab-4a69-9141-6e969bbd7a0c.gif)
