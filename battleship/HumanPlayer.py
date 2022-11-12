

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

        def insert_ship(x_pos: int, y_pos: int, direction: str) -> bool:
            """Helper inner function to place the ship"""

            # Valid cells that are not occupied AND are inside the grid
            valid_cells: list[Tuple[int, int]] = []

            # A loop which does the checks for the cells
            for cell in range(ship.size):

                if direction == "H":
                    # Horizontal adjustment
                    next_x_pos = x_pos + cell
                    next_y_pos = y_pos
                else:
                    # Vertical adjustment
                    next_y_pos = y_pos + cell
                    next_x_pos = x_pos

                # Check that the ship is inside the grid
                if self._check_boundary(next_x_pos, next_y_pos):
                    pp.pprint("Ship does not fit inside the grid!")
                    return False

                # Check the cell is empty
                elif self._check_cell(next_y_pos, next_x_pos):  # Cell was occupied
                    pp.pprint("Ships can't overlap!")
                    return False

                else:
                    valid_cells.append((next_x_pos, next_y_pos))

            for place in valid_cells:
                # Fills the valid cells with actual values
                self.data.grid[place[1]][place[0]] = ship.id

            pp.gprint(self.data.grid)
            return True

        pp.pprint("Ship positions, e.g A1")
        for ship in self.ships:

            while (True):

                # Ask for the position of the ship
                raw_input = input(
                    f"Ship [{''.join(ship.size*'X')}]: ")
                raw_x_pos = raw_input[0]
                raw_y_pos = raw_input[1]

                # Converts the input to index, e.g A => 0
                x_pos = int(ord(raw_x_pos.lower()) - 96) - 1
                y_pos = int(raw_y_pos)

                # Ask for the ship direction
                direction = input("Ship direction (V/H): ")

                if direction != "V" and direction != "H":
                    print("Direction is not valid!")
                    continue

                # Validate the input coordinates
                if self.validate_input(x_pos, y_pos) and len(raw_input) == 2 and insert_ship(x_pos, y_pos, direction) is True:
                    break
                else:
                    pp.pprint("Coordinates not valid, try again")

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
