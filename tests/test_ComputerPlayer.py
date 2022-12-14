import numpy as np
import unittest
from battleship.ComputerPlayer import ComputerPlayer
from battleship import PlayerData
from battleship.Game import Game
from battleship.PrettyPrint import PrettyPrint
import random
import json
import os

pp = PrettyPrint()


class TestComputerPlayer(unittest.TestCase):

    def setUp(self):

        with open("config.json", "r") as f:
            self.config = json.load(f)

        p1_data = PlayerData(
            grid=np.copy(Game.deserialize_random_grid()),
            pre_filled_grid=True,
            available_ships=self.config["available_ships"],
        )

        p1 = ComputerPlayer(p1_data)

        p2_data = PlayerData(
            grid=np.copy(Game.deserialize_random_grid()),
            available_ships=self.config["available_ships"],
            pre_filled_grid=True
        )

        p2 = ComputerPlayer(p2_data)

        self.players = [p1, p2]

    def run_game(self) -> ComputerPlayer:

        player_list = self.players.copy()

        starting_player = random.choice(player_list)
        player_list.remove(starting_player)
        other_player = player_list[0]

        pp.pprint(f"{starting_player} starts")

        # Main game loop

        rounds = 0
        while (True):

            rounds += 1

            print(f"ROUNDS: {rounds}")

            starting_player.feed_back(
                other_player.check_hit(starting_player.fire()))
            if not other_player.status():
                return starting_player

            other_player.feed_back(
                starting_player.check_hit(other_player.fire()))
            if not starting_player.status():
                return other_player

            os.system('cls' if os.name == 'nt' else 'clear')
            print(starting_player.grid)
            print(starting_player.target_grid)

    def test_run(self):

        winner = self.run_game()
        self.assertTrue(winner, "Winner should exist")


if __name__ == '__main__':
    unittest.main()
