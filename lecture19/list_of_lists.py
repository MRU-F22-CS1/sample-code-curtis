def to_int_list(num_str: str) -> list:
    """
    Converts a string of comma-separated numbers into a list of ints.
    """
    split_nums = num_str.split(", ")
    int_list = []
    for num in split_nums:
        int_list.append(int(num))
    
    return int_list

def print_matrix(matrix: list) -> None:
    """
    Prints out the items in a 2D list.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
        

def main() -> None:
    list_2D = []
    user_input = input("Enter a list of integers: ")
    while user_input != "":
        nums = to_int_list(user_input)
        list_2D.append(nums)
        user_input = input("Enter a list of integers: ")
    
    print(list_2D)
    print_matrix(list_2D)

main()