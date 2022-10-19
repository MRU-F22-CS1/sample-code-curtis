from random import randint

TARGET = randint(1, 10)
# TARGET = 3

def play_game(guess: int) -> None:
    """
    Checks guess to see if it matches.
    """
    if guess == TARGET:
        print("You got it!")
    else:
        print("Sorry, better luck next time.")

def main() -> None:
    guess = int(input("Guess a number between 1 and 10: "))
    play_game(guess)

main()