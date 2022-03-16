# Author: Donald Reniff
# Github username: dreniff3
# Description: This module contains the classes necessary for instantiating a simulated game of Battleship.

class Ship:
    """ Represents a ship.

    Attributes:
        _name (str): The name of the ship.
        _length (int): The length of the ship.
        _location (list): The (x, y) coordinates the ship occupies on the player's game board.
        _status (str): If all of the ship's (x, y) coordinates have been hit by an enemy's torpedoes, the ship status
            is "sunk", otherwise it is "live".
    """

    def __init__(self, name):
        """ The constructor of the Ship class. Sets all data members to their initial values. """
        self._name = name
        if name == 'carrier':
            self._length = 5
        if name == 'battle-ship':
            self._length = 4
        if name == 'cruiser':
            self._length = 3
        if name == 'submarine':
            self._length = 3
        if name == 'destroyer':
            self._length = 2
        self._location = []
        self._status = "live"


class Player:
    """ Represents a player.

    Attributes:
        _turn (str): Either "first" or "second", designating which turn the Player can legally take.
        _ships (dict): The player's collection of Ship objects.
        _hits (list): The (x, y) positions of each hit the Player has made on their opponent's ships.
        _misses (list): The torpedo misses recorded as (x, y) positions.
        _board (list): The player's 10x10 game board represented as a list of ten lists ten strings long.
        _grid (list): The printable board of hits and misses.
    """

    def __init__(self, turn):
        """ The constructor of the Player class. Initializes all data members to their initial values. """
        self._turn = turn
        self._ships = {}
        self._hits = []
        self._misses = []
        self._board = [[' '] * 10 for i in range(10)]
        self._grid = [[' '] * 10 for i in range(10)]

    def get_grid(self):
        """
        Gets the Player's grid, where misses and hits are recorded.
        """
        return self._grid


class ShipGame:
    """ Represents a game of Battleship.

    Attributes:
        _player_turn (str): The player whose turn it is.
        _player_1 (Player): The Player object representing player_1.
        _player_2 (Player): The Player object representing player_2.
        _letters_to_numbers (dict): A collection of key-value pairs for translating ship and torpedo coordinates into
            (x, y) positions on a player's board.
    """

    def __init__(self):
        """
        The constructor of the ShipGame class. Takes no parameters and initializes all data members to their initial
        values.
        """
        self._player_turn = "first"
        self._player_1 = Player("first")
        self._player_2 = Player("second")
        self._letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        self._current_state = 'UNFINISHED'

    def place_ship(self, player, ship, coordinates, orientation):
        """
        Places a ship on a player's grid at a designated starting-coordinate.
        If a ship does not fit entirely on that player's grid, or if it would overlap any previously placed ships
        on that player's grid, the ship is not added and the method returns False.

        :param player: The player placing the ship, either "first" or "second".
        :param ship: The ship being placed.
        :param coordinates: The (x, y) coordinates of the closest square to 'A1' that the ship will occupy.
        :param orientation: The ship's orientation, either "R" if the ship occupies squares in a row, or "C" if it
            occupies squares in a column.
        """
        pass

    def print_board(self, player):
        """
        Prints the 10x10 grid showing the Player's hits and misses on their enemy's board.
        """
        if player == "first":
            player_obj = self._player_1
        else:
            player_obj = self._player_2
        grid = player_obj.get_grid()
        print(" ", " ".join("123456789" + "10"))
        for letter, row in zip("ABCDEFGHIJ", grid):
            print(letter, " ".join(row))


if __name__ == "__main__":
    s = ShipGame()
    s.print_board("first")
