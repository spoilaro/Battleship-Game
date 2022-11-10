import numpy as np
import json
from battleship import Config


from battleship.Game import Game


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
    winner = game.run()

    print(winner)


if __name__ == "__main__":
    main()
