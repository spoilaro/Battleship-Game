
from battleship import Ship, ShipState, PlayerData, Printing
from typing import Tuple
from battleship.PrettyPrint import PrettyPrint


pp = PrettyPrint()


class Player:
    def __init__(self, data: PlayerData):

        self.data = data
        self.grid = data.grid
        self.ships: list[Ship] = []

    def _check_cell(self, x: int, y: int) -> bool:
        """
        Checks if the cell with provided coordinates is occupied.
        Returns True if occupied
        """
        grid = self.data.grid

        return True if grid[x][y] else False

    def _find_ship(self, id: int) -> int:
        for i, ship in enumerate(self.ships):
            if ship.id == id:
                return i

        # Should not happen => Testing
        return 0

    def check_hit(self, coordinates: Tuple[int, int]) -> bool:
        x_pos = coordinates[0]
        y_pos = coordinates[1]
        cell = self.grid[y_pos][x_pos]

        if cell != 0 and cell > 0:

            pp.pprint(f"HIT!, Ship {cell} was hit")
            self.grid[y_pos][x_pos] = -cell

            ship_index = self._find_ship(cell)

            ship = self.ships[ship_index]

            # Update ship hits
            ship.hits += 1
            if ship.hits == ship.size:
                # If all the cells of the ship are hit => destroyed
                ship.state = ShipState.DESTROYED
            return True

        else:
            pp.pprint("MISS")
            print()
            return False

    def status(self):
        """Checks if there are any ships floating"""

        ships_floating = 0

        for ship in self.ships:
            if ship.state != ShipState.DESTROYED:
                ships_floating += 1

        # If there are no ships alive return False == Player lost
        return False if ships_floating == 0 else True

    def fire(self):
        """Fires a shot to the opponents grid"""
        # This method is a stub which is implemented in child classes

    def feed_back(self, hit: bool):
        """Receives feedback hit/miss"""
        # This method is a stub which is implemented in child classes

    def _create_ships(self, available_ships) -> list[Ship]:
        """Creates the ships for the player"""

        ships = [
            Ship(hits=0, state=ShipState.SAFE, size=ship_type, id=id+1) for id, ship_type in enumerate(available_ships)
        ]
        return ships

    def __repr__(self):
        """Print Player objects better"""
        return f"{self.name}"
