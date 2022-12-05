from element import Element

def read_table(filename: str) -> list:
    """
    Reads elements into a list.
    """
    f = open(filename, "r")
    elements = []
    # read the header and discard it
    f.readline()
    for line in f:
        # 1,Hydrogen,H,1.007,1
        cols = line.split(",")
        atom = Element(
            int(cols[0]),
            cols[1],
            cols[2],
            float(cols[3]),
            int(cols[4])
            )
        elements.append(atom)
    f.close()
    return elements

def max_neutrons(table: list) -> Element:
    """
    Find the element with the highest number of neutrons
    """
    largest = table[0]
    for elem in table:
        # for first match, elem.neutrons() > largest.neutrons()
        # >= for second match
        if elem.neutrons() >= largest.neutrons():
            largest = elem
    
    return largest

def main() -> None:
    elements = read_table("periodic_table.csv")
    for elem in elements:
        print(elem)

    print(f"Max neutrons is: {max_neutrons(elements)}")
main()