import unittest
from battleship.Game import Game
import json
from battleship import Config


class TestGame(unittest.TestCase):

    def setUp(self):
        # Loading the configuration for the game
        with open("config.json", "r") as f:
            json_config = json.load(f)

            try:
                # Makes sure that provided configuration is correct
                config = Config(**json_config)
            except TypeError as e:
                print(f"Provided undefined configuration, error: {e}")
                exit(1)
            self.game = Game(config)

    def testGridInit(self):
        pass
