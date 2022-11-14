def list_of_squares(n: int) -> list:
    """
    Builds a list containing squares of numbers from 1 to n.
    """
    squares = []
    for num in range(1, n + 1):
        squares.append(num ** 2)
    return squares

def modify_me(a: list) -> None:
    a[0] = 0

def main() -> None:
    maxnum = int(input("Enter the maximum number to square: "))
    squares = list_of_squares(maxnum)
    print(squares)
    modify_me(squares)
    print(squares)
    
main()