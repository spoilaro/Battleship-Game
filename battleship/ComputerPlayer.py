
import numpy as np
from battleship.Player import Player
from battleship import PlayerData, Position
from typing import Tuple
import random
from battleship.PrettyPrint import PrettyPrint


pp = PrettyPrint()


class ComputerPlayer(Player):

    def __init__(self, data: PlayerData):
        super()
        self.name = "AI Player"
        self.data = data
        self.grid = data.grid
        self.last_shot: Tuple

        self.ships = self._create_ships(data.available_ships)

        # Grid used to keep up the targeting algorithm
        self.target_grid = np.zeros((10, 10), dtype=int)

        # List of cells adjacent to cell hit
        self.hunt_list: list[Tuple[int, int]] = []

    def fire(self) -> Tuple[int, int]:
        """Fire a shot to a cell in the opponent's grid"""

        pp.pprint("AI is firing", False)

        firing_coordinates = self.hunt_algoritm()

        x = firing_coordinates[0]
        y = firing_coordinates[1]

        self.target_grid[y][x] = -1

        self.last_shot = (x, y)

        return firing_coordinates

    def hunt_algoritm(self):
        """Hunting algorithm"""

        if len(self.hunt_list) == 0:

            x_pos = random.randint(0, 9)
            y_pos = random.randint(0, 9)

            # return random.choice(self.generate_empties())
            return (x_pos, y_pos)

        else:

            return self.hunt_list.pop(0)

    def generate_empties(self):

        empties: list[Tuple[int, int]] = []

        for y, column in enumerate(self.grid):
            for x in column:

                if self.grid[y][x] != -1:
                    empties.append((x, y))

        print(len(empties))
        return empties

    def feed_back(self, hit: bool):

        last_x, last_y = self.last_shot

        if hit:
            self.target_grid[self.last_shot[1]][self.last_shot[0]] = 1

            self.hunt_list = [
                # One UP
                # (last_x, last_y+1) if last_y != 9 else (last_x, last_y),
                # # One DOWN
                # (last_x, last_y-1) if last_y != 0 else (last_x, last_y),
                # # One LEFT
                # (last_x-1, last_y) if last_x != 0 else (last_x, last_y),
                # # One RIGHT
                # (last_x+1, last_y) if last_x != 9 else (last_x, last_y),
            ]

        else:
            self.target_grid[self.last_shot[1]][self.last_shot[0]] = -1
