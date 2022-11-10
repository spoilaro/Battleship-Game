import numpy as np
import unittest
from battleship.ComputerPlayer import ComputerPlayer
from battleship import PlayerData


class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        # Loading the configuration for the game
        # with open("config.json", "r") as f:
        #     json_config = json.load(f)
        #
        #     try:
        #         # Makes sure that provided configuration is correct
        #         config = Config(**json_config)
        #     except TypeError as e:
        #         print(f"Provided undefined configuration, error: {e}")
        #         exit(1)

        test_data = PlayerData(
            grid=np.zeros((10, 10), dtype=int),
            pre_filled_grid=True,
            available_ships=[]
        )

        self.player = ComputerPlayer(test_data)

    def test_fire(self):

        for _ in range(100):
            x_pos, y_pos = self.player.fire()

            self.assertTrue((x_pos < 10 and x_pos > -1),
                            f"X position should be inside the grid, got: {x_pos}")

            self.assertTrue((y_pos < 10 and x_pos > -1),
                            f"Y position should be inside the grid, got: {y_pos}")


if __name__ == '__main__':
    unittest.main()
