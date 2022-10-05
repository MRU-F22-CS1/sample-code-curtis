def roll_dice() -> int:
    """Roll two dice and add the result"""

def print_results(name: str, score: int) -> None:
    """Shows the result of the player's roll"""

def main() -> None:
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")

    score1 = roll_dice()
    score2 = roll_dice()

    print_results(player1, score1)
    print_results(player2, score2)

main()