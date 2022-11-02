from random import randint
def scope_test() -> int:
    """
    Generates an integer based on another random integer.
    """
    choice = randint(1, 10)
    print(f"Choice is {choice}")
    result = -1
    if choice < 3:
        result = 3
    elif choice < 6:
        result = 6
    elif choice < 9:
        result = 9
    
    return result

def main():
    return_value = scope_test()
    print(f"You got a {return_value}")

main()