from random import randint

def roll_dice() -> int:
    """
    Rolls a pair of dice
    """
    return randint(1, 6) + randint(1, 6)

def count_12s(n: int) -> int:
    """
    Rolls the dice n times and counts how many 12s we get.
    """
    counter = 0
    n_12s = 0
    while counter < n:
        roll = roll_dice()
        if roll == 12:
            n_12s = n_12s + 1
        
        counter = counter + 1
    
    return n_12s

def main() -> None:
    num_rolls = int(input("How many times do you want to roll? "))
    num_12s = count_12s(num_rolls)
    print(f"You rolled {num_12s} 12s!")

main()