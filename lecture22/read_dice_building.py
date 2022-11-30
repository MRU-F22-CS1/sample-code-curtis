from die import Die

def read_building(filename: str) -> list:
    """
    Reads the building in filename into a list of dice.
    """
    f = open(filename, "r")
    building = []
    for line in f:
        row = []
        dice = line.split("|")
        for die in dice:
            if die[0] == "-":
                row.append(None)
            else:
                row.append(Die(die[0], int(die[1])))
        building.append(row)
    f.close()
    return building

def do_something_with_dice(d: Die) -> bool:
    """ Do something """
    pass

def main() -> None:
    building = read_building("stone-1-5-0.txt")
    for row in building:
        for die in row:
            print(die, end=" ")
        print()

main()