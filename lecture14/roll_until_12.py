from random import randint

def roll_dice() -> int:
    """
    Rolls a pair of dice
    """
    return randint(1, 6) + randint(1, 6)

def count_until_12() -> int:
    """
    Rolls the dice and counts how many rolls to get a 12.
    """
    roll = 0
    counter = 0
    while roll != 12:
        roll = roll_dice()
        counter = counter + 1
        print(counter)
    
    return counter

def main() -> None:
    print(f"It took {count_until_12()} rolls to get a 12.")

main()