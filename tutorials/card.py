class Card:
    """
    Represents a standard playing card.
    """
    def __init__(self, value: int, suit: str) -> None:
        self.value = value
        self.suit = suit
    
    def __str__(self) -> str:
        return f"{self.value}{self.suit}"

if __name__ == "__main__":
    ace_of_hearts = Card(1, "♥")
    print(ace_of_hearts)