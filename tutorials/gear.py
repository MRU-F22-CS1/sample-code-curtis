class Gear:
    """
    Represents an item of camping gear.
    """
    def __init__(self, name: str, vol: float) -> None:
        self.name = name
        self.vol = vol
    
    def __str__(self) -> str:
        return f"{self.name} ({self.vol} L)"

if __name__ == "__main__":
    # Anything indented here only runs if gear.py is
    # run directly, not imported
    tent = Gear("a super tiny backpacking tent", 1.5)
    print(tent)
