import die

def main() -> None:
    print("Imported die")
    green = die.Die("green")
    orange = die.Die("orange")
    print(green)
    print(orange)

if __name__ == "__main__":
    main() 