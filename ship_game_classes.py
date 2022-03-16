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
        _board (list): The player's 10x10 game board represented as a list of ten lists ten strings long.
    """
    def __init__(self, turn):
        """ The constructor of the Player class. Initializes all data members to their initial values. """
        self._turn = turn
        self._ships = {}
        self._hits = []
        self._board = [[' '] * 10 for i in range(10)]


class ShipGame:
    """ Represents a game of Battleship.

    Attributes:
        _player_turn (str): The player whose turn it is.
    """
    def __init__(self):
        self._player_turn = "first"
