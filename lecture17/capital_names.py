def cap_case(names: list) -> None:
    """
    Converts each name in names to capital case.
    """
    for i in range(len(names)):
        names[i] = names[i].capitalize()
    
def main() -> None:
    names = ["red", "orange", "green"]
    cap_case(names)
    print(names)

main()