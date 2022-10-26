from random import randint

def draw_card() -> int:
    """
    Draw a random number of gems between 0 and 15.
    25/75 chance of 0 or gems.
    """
    gems_or_zero = randint(0,3)
    n_gems = 0
    if gems_or_zero == 0:
        n_gems = 0
    else:
        n_gems = randint(1, 15)

    return n_gems

def play_game(n_players: int) -> None:
    """
    Draw a card. If not zero, divide gems evenly by players
    and calculate leftover. Otherwise, lose.
    """
    gems = draw_card()
    print(f"You drew {gems} gems")
    if gems == 0:
        print("Sorry, you lose!")
    else:
        n_per_player = gems // n_players
        leftover = gems % n_players
        print(f"Everyone gets {n_per_player} gems with {leftover} leftover.")


def main() -> None:
    print("Welcome to Incan Gold! Let's explore the temple.")
    n_players = int(input("Enter the number of players: "))
    play_game(n_players)

main()