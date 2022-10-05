def average(num1: float, num2: float) -> None:
    avg = (num1 + num2) / 2
    print(f"The average of {num1} and {num2} is {avg}")

def main() -> None:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    average(num2, num1)
    average(2 * num2, 3 * num1)

main()