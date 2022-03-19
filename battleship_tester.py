import unittest
from ship_game_classes import ShipGame


class TestShipGame(unittest.TestCase):
    """ Contains unit tests for ship_game_classes module. """

    def test_game_instantiation(self):
        """ Tests instantiation of a ShipGame object. """
        s = ShipGame()
        self.assertIsInstance(s, ShipGame)

    def test_place_ship_1(self):
        """
        Tests if a ship is placed in the right location on the player's board and is also placed in that
        player's collection.
        """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        self.assertEqual('destroyer' in s._player_1.get_ships(), True)
        self.assertEqual(s._player_1.get_ships()['destroyer'].get_location(), [(5, 7), (5, 8)])

    def test_place_ship_2(self):
        """ Test that a ship placed off the board is not counted. """
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        s.place_ship("first", 'carrier', 'J9', 'R')
        self.assertEqual(s.get_num_ships_remaining("first"), 1)

    def test_place_ship_3(self):
        """ Test that a ship placed on positions already occupied is not counted. """
        s = ShipGame()
        s.place_ship("first", 'carrier', 'C1', 'R')
        s.place_ship("first", 'battle-ship', 'B2', 'C')
        self.assertEqual(s.get_num_ships_remaining("first"), 1)
