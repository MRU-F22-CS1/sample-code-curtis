from random import randint

TARGET = randint(1, 20)
TARGET = 3

def guessing_game() -> int:
    """
    Prompts a user to guess a number repeatedly.
    Returns the number of guesses, or -1 if incorrect after 3.
    """
    prompt = "Guess a number between 1 and 20: "
    number = int(input(prompt)) # the priming read
    guesses = 1

    while number != TARGET and guesses < 3:
        guesses += 1
        print(f"Sorry, {number} is not the right number")
        number = int(input(prompt)) # internal read

    return_value = -1
    if number == TARGET:
        return_value = guesses
    return return_value


def main() -> None:
    num_guesses = guessing_game()
    if num_guesses == -1:
        print("Sorry, better luck next time.")
    else:
        print(f"You guessed the number in {num_guesses} guesses!")

main()