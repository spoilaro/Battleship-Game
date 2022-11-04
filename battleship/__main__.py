import numpy as np
import json
from battleship import Config, Ship, ShipState, PlayerData


class Game:
    def __init__(self, config: Config):
        self.config = config

        self.players: list[Player] = []

        # Grid flattened into one dimension
        self.grid = np.zeros((self.config.grid_size,
                             self.config.grid_size), dtype=int)

        self.init_players()

    def init_players(self) -> None:
        """Initialize players"""

        for player_id in range(self.config.player_count):

            data = PlayerData(
                grid=np.copy(self.grid),
                id=player_id,
                available_ships=self.config.available_ships
            )
            new_player = Player(data)

            # The new player is added to Game's player list
            self.players.append(new_player)

    def run(self) -> None:
        """Runs the main game loop"""

        # TODO: Set up phase

        # TODO: Loop
        pass


class Player:
    def __init__(self, data: PlayerData):

        self.ships: list[Ship] = []
        self.player_id = data.id
        self.data = data

        # TODO: Rename player

        # Create ships for the player
        self._create_ships(data.available_ships)

    def _create_ships(self, available_ships):
        """Creates the ships for the player"""

        self.ships = [
            Ship(cells=None, state=ShipState.SAFE, size=ship_type, id=id+1) for id, ship_type in enumerate(available_ships)
        ]

    def set_up(self):
        """Set ships onto grid"""

        print("Ship positions, e.g A1")
        for ship in self.ships:
            (raw_x_pos, raw_y_pos) = input(
                f"Ship [{''.join(ship.size*'X')}]: ")

            # Converts the letter to number, e.g A => 1
            y_pos = int(ord(raw_y_pos.lower()) - 96)
            x_pos = int(raw_x_pos)

            for cell in range(ship.size):
                self.data.grid[x_pos + cell][y_pos] = ship.id

                # TODO: Rotate ship

            self._show_grid()

    def end_turn(self):
        """Ends the turn"""
        pass

    def fire(self):
        """Fires a shot to the opponents grid"""
        pass

    def _show_grid(self):
        """Prints the grid to stdout"""
        grid = self.data.grid

        # for row in enumerate(grid):
        #     for cell in row:
        #         print(cell)

        # TODO: Prettier grid print
        print(grid)

    def __repr__(self):
        """Print Player objects better"""
        return f"Player ID: {self.player_id}"


def main() -> None:
    """Main function for running the game"""

    # Loading the configuration for the game
    with open("config.json", "r") as f:
        json_config = json.load(f)

        try:
            # Makes sure that provided configuration is correct
            config = Config(**json_config)
        except TypeError as e:
            print(f"Provided undefined configuration, error: {e}")
            exit(1)

    # Game & tool versions
    print(f"Game version: {config.game_version}")
    print(f"Numpy version: {np.__version__}\n")

    game = Game(config)
    game.init_players()
    game.players[0].set_up()


if __name__ == "__main__":
    main()
