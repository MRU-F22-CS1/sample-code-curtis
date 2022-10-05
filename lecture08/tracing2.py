def func(b: int, a: int) -> int:
    b = 2 * b
    a = a + b
    d = a + b
    return d

def main() -> None:
    a = 3
    b = 10
    c = func(a, b)
    print(a, b, c)

main()