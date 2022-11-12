from battleship import Printing


class PrettyPrint:
    def __init__(self):
        pass

    def pprint(self, msg: str, human: bool = None):
        """Prints the messages from the game with additional colors"""

        if human is True:
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

    def gprint(self, grid) -> None:
        """
        Prints the grid in pretty colors
        """
        for column in grid:
            for cell in column:
                print(f" {self._icon(cell)}", end="")

            print()
        print()

    def _icon(self, cell: int) -> str:
        """Returns a colored string based on the cell value"""

        if cell == 0:
            # Water
            return Printing.BLUE+f"O"+Printing.END

        elif cell > 0:
            # Player's ship alive OR Player hit AI's ship
            return Printing.GREEN+f"O"+Printing.END
        else:
            # Player's ship got hit OR Player missed a shot
            return f"O"
