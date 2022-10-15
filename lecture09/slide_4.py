from math import tan, pi

def area(n_sides: int, apothem: float) -> float:
    """
    Calculate the area of a regular polygon given 
    the number of sides and the apothem length.
    """

    return n_sides * apothem ** 2 * tan(pi / n_sides)

def main():
    n = int(input("Enter the number of sides: "))
    apothem = float(input("Enter the length of the apothem: "))
    A = area(n, apothem)
    print(f"The area is {A:.1f}")

main()