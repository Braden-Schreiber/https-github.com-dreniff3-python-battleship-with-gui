import unittest
from ship_game_classes import ShipGame


class TestShipGame(unittest.TestCase):
    """ Contains unit tests for ship_game_classes module. """

    def test_game_instantiation(self):
        s = ShipGame()
        self.assertIsInstance(s, ShipGame)

    def test_place_ship_1(self):
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        self.assertEqual('destroyer' in s._player_1.get_ships(), True)
        self.assertEqual(s._player_1.get_ships()['destroyer'].get_location(), [(5, 7), (5, 8)])

    def test_place_ship_2(self):
        s = ShipGame()
        s.place_ship("first", 'destroyer', 'F8', 'R')
        s.place_ship("first", 'carrier', 'J9', 'R')
        self.assertEqual(s.get_num_ships_remaining("first"), 1)
