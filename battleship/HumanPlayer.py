

from battleship.Player import Player
from battleship import PlayerData
from typing import Tuple
import numpy as np
from battleship.PrettyPrint import PrettyPrint
import os


pp = PrettyPrint()


class HumanPlayer(Player):
    def __init__(self, data: PlayerData):
        super()
        self.data = data
        self.name = "Human Player"
        self.grid = data.grid
        self.ships = self._create_ships(self.data.available_ships)
        self.target_grid = np.zeros((10, 10), dtype=int)
        self.last_shot: Tuple[int, int]

        if not data.pre_filled_grid:
            # Prompts the player to insert ship locations
            self.set_up_ships()

    def set_up_ships(self):
        """Set ships onto grid"""

        # Create ships for the player

        def insert_ship(x_pos: int, y_pos: int) -> bool:
            """Helper inner function to place the ship"""
            for cell in range(ship.size):
                if self._check_cell(y_pos, x_pos + cell):  # Cell was occupied
                    pp.pprint("Ships can't overlap, try again!")
                    return False
                else:
                    self.data.grid[y_pos][x_pos +
                                          cell] = ship.id  # Cell filled succesfully
            pp.gprint(self.data.grid)
            return True

        pp.pprint("Ship positions, e.g A1")
        for ship in self.ships:

            while (True):
                # Ask for the position of the ship
                (raw_x_pos, raw_y_pos) = input(
                    f"Ship [{''.join(ship.size*'X')}]: ")
                # Converts the input to index, e.g A => 0
                x_pos = int(ord(raw_x_pos.lower()) - 96) - 1
                y_pos = int(raw_y_pos) - 1

                if insert_ship(x_pos, y_pos):  # If the insertion was succesful, just go on
                    break

    def fire(self) -> Tuple[int, int]:
        """Fire a shot to a cell in the opponent's grid"""

        pp.pprint("Human Player is firing", True)

        while (True):
            raw_input = input("Cordinates for the shot (A0-K9): ")

            raw_x_pos = raw_input[0]
            raw_y_pos = raw_input[1]
            # Converts the input to index, e.g A => 0
            x_pos = int(ord(raw_x_pos.lower()) - 96) - 1
            y_pos = int(raw_y_pos)

            if self.validate_input(x_pos, y_pos) and len(raw_input) == 2:
                break
            else:
                pp.pprint("Coordinates not valid, try again")

        self.last_shot = (x_pos, y_pos)

        return (x_pos, y_pos)

    def validate_input(self, x_pos: int, y_pos: int) -> bool:
        """Checks that the given coordinates are on the grid"""

        if x_pos >= 0 and x_pos < 10 and y_pos >= 0 and y_pos < 10:
            return True
        else:
            return False

    def feed_back(self, hit):
        os.system('cls' if os.name == 'nt' else 'clear')
        if hit:
            self.target_grid[self.last_shot[1]][self.last_shot[0]] = 1
        else:
            self.target_grid[self.last_shot[1]][self.last_shot[0]] = -1
        pp.pprint("PLAYER SHIPS", True)
        pp.gprint(self.grid)

        pp.pprint("PLAYER TARGETS", True)
        pp.gprint(self.target_grid)
