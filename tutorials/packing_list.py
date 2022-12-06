from gear import Gear

def read_gear(filename: str) -> list:
    """
    Reads the gear into a list of Gear objects.
    """
    gear_list = []
    f = open(filename, "r")
    for line in f:
        parts = line.split(",")
        item = Gear(parts[0], float(parts[1]))
        gear_list.append(item)
    f.close()
    return gear_list

def find_largest(gear_list: list) -> Gear:
    """
    Looks through the list and finds
    the biggest item by volume.
    """
    largest = gear_list[0]
    for item in gear_list:
        if item.vol > largest.vol:
            largest = item
    
    return largest

def main() -> None:
    gear_list = read_gear("gear.csv")
    for item in gear_list:
        print(item)
    
    print(f"\nYou should pack the {find_largest(gear_list)} first")

main()