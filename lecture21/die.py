from random import randint

DICE_COLOURS = ["clear", "green", "orange", "black"]

class Die:
    """
    Class to represent a die from the Blueprints game.
    """
    def __init__(self, col: str) -> None:
        """
        Creates a die of the given colour.
        """
        self.roll()
        self.colour = col
    
    def roll(self) -> None:
        """
        Roll the die and update the face variable.
        """
        self.face = randint(1, 6)

def main() -> None:
    building = []
    for i in range(6):
        building.append(Die(DICE_COLOURS[randint(0,len(DICE_COLOURS) - 1)]))
    # print(f"The die is {d1.colour}")
    # print(f"d1 is a {d1.face}")
    # print(f"d2 is a {d2.face}")
    for d in building:
        print(f"Colour is {d.colour}, value is {d.face}")
        d.roll()
        print(f"Now the {d.colour} die is a {d.face}")



main()