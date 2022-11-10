def get_odd_number_loop(prompt: str) -> int:
    """
    Prompts the user to enter a number, enforcing odd.
    Loops until an odd number is entered.
    """
    user_value = int(input(prompt + " (must be positive and odd): "))
    while user_value % 2 == 0 or user_value < 0:
        print("Not a positive odd number, try again.")
        user_value = int(input(prompt + " (must be positive and odd): "))
    
    return user_value

def get_odd_number_recursive(prompt: str) -> int:
    """
    Prompts the user to enter a number, enforcing odd.
    Recursively calls self until an odd number is entered.
    """
    user_value = int(input(prompt + " (must be positive and odd): "))
    if user_value % 2 == 0 or user_value < 0:
        print("Not a positive odd number, try again.")
        user_value = get_odd_number_recursive(prompt)
    
    return user_value

def print_isoceles_loops() -> None:
    """
    Prints an isoceles triangle, one character at a time, using nested for loops.
    """
    base_length = get_odd_number_loop("Enter the base")
    half = base_length // 2
    for i in range(half + 1):
        for j in range(0, half - i):
            print(" ", end="")
        for j in range(half - i, half + i + 1):
            print("*", end="")
        for j in range(half + j + 1, base_length):
            print(" ", end="")
        print()

def print_isoceles_fstring() -> None:
    """
    Prints an isoceles triangle using fstrings.
    """
    base_length = get_odd_number_recursive("Enter the base")
    for i in range(base_length // 2 + 1):
        stars = "*" * (i * 2 + 1)
        print(f"{stars: ^{base_length}}")

def main() -> None:
    print_isoceles_loops()
    print_isoceles_fstring() 

main()