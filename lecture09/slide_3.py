from random import randint

def roll() -> int:
    """Roll two dice together"""
    return randint(1, 6) + randint(1, 6)

def play_game(name: str) -> int:
    """
    Calculates a silly score based on name.
    """
    weight = randint(-1, 1)
    score = weight * len(name) + roll()
    return score

def main():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    print(f"{player1} scores {play_game(player1)}!")
    print(f"{player2} scores {play_game(player2)}!")

main()