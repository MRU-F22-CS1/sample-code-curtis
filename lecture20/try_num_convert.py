def read_num_from_user() -> float:
    """
    Reads a number from the user and returns it.
    """
    num = 0
    while num == 0:
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            print("That's not a number!")
            # recursive version
            # num = read_num_from_user()
    
    return num

def main() -> None:
    num = read_num_from_user()
    print(f"Your number is {num}")

main()