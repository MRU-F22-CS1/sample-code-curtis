def read_number_file(filename: str) -> list:
    """
    Reads the numbers in filename into a list of ints.
    """
    f = open(filename, "r")
    nums = []
    for line in f:
        num = int(line)
        nums.append(num)
    
    f.close()
    return nums

def main() -> None:
    num_list = read_number_file("lecture19/numeric_data.txt")
    print(num_list)

main()