from random import randint

def gen_computer_choice() -> str:
    """
    Generates a choice of rock/paper/scissors for the computer
    """
    num = randint(1, 3)
    if num == 1:
        return "r" # rock
    elif num == 2:
        return "p" # paper
    elif num == 3: 
        return "s" # scissors

def get_user_choice() -> str:
    """
    Prompts the user for choice of rock/paper/scissors
    """
    choice = input("Choose rock (r), paper (p) or scissors (s): ")
    return choice

def play_game(user: str, computer: str) -> None:
    """
    Checking to see who wins between user and computer
    """

    if user == computer:
        print(f"You tie! You both chose {user}")

    winner = ""
    if user == "r" and computer == "s":
        winner = "user"
    elif user == "p" and computer == "r":
        winner = "user"
    elif user == "s" and computer == "p":
        winner = "user"
    else:
        winner = "computer"
    
    if winner == "computer":
        print(f"{winner} wins! {computer} beats {user}")
    else:
        print(f"{winner} wins! {user} beats {computer}")

def main() -> None:
    """
    Call the rest of the functions and put them together.
    """
    comp_choice = gen_computer_choice()
    user_choice = get_user_choice()

    play_game(user_choice, comp_choice)

main()