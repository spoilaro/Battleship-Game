
import numpy as np
from battleship import Config, PlayerData

from battleship.HumanPlayer import HumanPlayer
from battleship.ComputerPlayer import ComputerPlayer
from battleship.Player import Player
import os
import random
from typing import Tuple


class Game:
    def __init__(self, config: Config):
        self.config = config

        # Empty grid for human player
        self.empty_grid = np.zeros((self.config.grid_size,
                                    self.config.grid_size), dtype=int)

        # A template grid for AI
        self.template_grid = self.deserialize_random_grid()
        self.human_player, self.ai_player = self.init_players()

    def deserialize_random_grid(self):
        """
            Select random grid template from templates directory
            and deserialize it
        """

        template_files = os.listdir("templates/")

        chosen_template = random.choice(template_files)

        # Reads the byte data from a file
        with open(f"templates/{chosen_template}", "rb") as f:
            byte_template = f.read()

        # TODO: Error/Wrong grid shape?
        # Deserializes the data back to numpy 2d array
        template_grid = np.frombuffer(
            byte_template, dtype=int).reshape((10, 10))

        return template_grid

    def init_players(self) -> Tuple[HumanPlayer, ComputerPlayer]:
        """Initialize players"""

        ai_data = PlayerData(
            grid=np.copy(self.template_grid),
            pre_filled_grid=True,
            available_ships=self.config.available_ships,
        )

        ai_player = ComputerPlayer(ai_data)

        human_data = PlayerData(
            # grid=np.copy(self.empty_grid),
            grid=np.copy(self.template_grid),
            available_ships=self.config.available_ships,
            pre_filled_grid=True

        )
        human_player = HumanPlayer(human_data)

        return (human_player, ai_player)

    def run(self) -> Player:
        """Runs the main game loop"""

        players = [self.human_player, self.ai_player]

        # Select random starting player
        starting_player = random.choice(players)
        players.remove(starting_player)
        other_player = players[0]

        print(f"{starting_player} starts!")

        # Main game loop
        while (True):

            starting_player.feed_back(
                other_player.check_hit(starting_player.fire()))
            if not other_player.status():
                return starting_player

            other_player.feed_back(
                starting_player.check_hit(other_player.fire()))

            if not starting_player.status():
                return other_player
