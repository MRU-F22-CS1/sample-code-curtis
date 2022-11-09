from random import randint

def gen_computer_choice() -> str:
    """
    Generates a choice of rock/paper/scissors for the computer
    """
    num = randint(1, 3)
    choice = ""
    if num == 1:
        choice = "r" # rock
    elif num == 2:
        choice = "p" # paper
    elif num == 3: 
        choice = "s" # scissors
    
    return choice

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
    winner = ""
    if user == computer:
        print(f"You tie! You both chose {user}")
    elif (user == "r" and computer == "s" 
          or user == "p" and computer == "r" 
          or user == "s" and computer == "p"):
        winner = "user"
    else:
        winner = "computer"
    
    if winner == "computer":
        print(f"{winner} wins! {computer} beats {user}")
    elif winner == "user":
        print(f"{winner} wins! {user} beats {computer}")

def valid_input() -> str:
    """
    Prompt the user to enter y or n. 
    Prompts again if they enter something else.
    """
    user_input = input("Do you want to play again? (y/n) ")
    while user_input != "n" and user_input != "y":
        # alternatively: not (user_input == "" or user_input == "y")
        print("Sorry, choice must be y or n.")
        user_input = input("Do you want to play again? (y/n) ")
    
    return user_input

def main() -> None:
    """
    Call the rest of the functions and put them together.
    """
    play_again = "y"
    while play_again == "y":
        comp_choice = gen_computer_choice()
        user_choice = get_user_choice()
        play_game(user_choice, comp_choice)
        play_again = valid_input()

main()