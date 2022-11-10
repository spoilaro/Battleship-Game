from datetime import datetime
import numpy as np
from battleship import Printing


class PrettyPrint:
    def __init__(self):
        pass

    def pprint(self, msg: str, human: bool = None):

        if human == True:
            player = "HUMAN"
            accent = Printing.GREEN
        elif human is None:
            player = "GAME"
            accent = Printing.BLUE
        else:
            player = "AI"
            accent = Printing.RED

        output = f"[{accent}{player}{Printing.END}] {msg}"
        print(output)

    def gprint(self, grid):
        """
        Prints the grid
        Modified from: https://stackoverflow.com/questions/60842728/developing-a-function-to-print-a-grid-in-python
        """
        for column in grid:
            for cell in column:
                print(f" {self._icon(cell)}", end="")

            # for _ in range(10):
            #     print("-", end="")
            print()
        print()

    def _icon(self, cell: int):
        if cell == 0:
            return Printing.BLUE+f"O"+Printing.END

        elif cell > 0:
            return Printing.GREEN+f"O"+Printing.END
        else:
            return Printing.RED+f"O"+Printing.END
