UNCHANGING_NAME = "MRU"

def say_hello(name: str) -> None:
    print(f"Hello, {name}")

def main() -> None:
    name = input("Enter your name: ")
    say_hello(name)

main()