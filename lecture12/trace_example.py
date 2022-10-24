Y_INTERCEPT = 32
SLOPE = 9 / 5

def do_math(a: float) -> float:
    """
    Does some math.
    """
    value = SLOPE * a + Y_INTERCEPT
    return value

def main() -> None:
    value = float(input("Enter a number to do some math: "))
    result = do_math(value)
    print(f"The result is {result:.1f}.")

main()