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
    """
    pass


class ShipGame:
    """ Represents a game of Battleship.

    Attributes:
    """
    pass
