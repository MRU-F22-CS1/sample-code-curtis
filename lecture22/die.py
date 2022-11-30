from random import randint

class Die:
    """
    Class to represent a die from the Blueprints game.
    """
    def __init__(self, material: str, face: int = 0) -> None:
        """
        Creates a die of the given colour.
        """
        self.material = material
        if face == 0:
            self.roll()
        else:
            self.face = face
    
    def __str__(self) -> str:
        """
        String representation of the die
        """
        return f"{self.material}{self.face}"

    def roll(self) -> None:
        """
        Roll the die and update the face variable.
        """
        self.face = randint(1, 6)