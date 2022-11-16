def to_int_list(num_str: str) -> list:
    """
    Converts a string of comma-separated numbers into a list of ints.
    """
    split_nums = num_str.split(", ")
    int_list = []
    for num in split_nums:
        int_list.append(int(num))
    
    return int_list

def main() -> None:
    user_input = input("Enter a list of integers: ")
    nums = to_int_list(user_input)
    print(nums)

main()