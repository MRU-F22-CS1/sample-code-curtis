def count_zeros(some_nums: list) -> int:
    """
    Counts the number of zeros in a list
    """
    zero_counter = 0
    for i in range(len(some_nums)):
        if some_nums[i] == 0:
            zero_counter += 1
    
    return zero_counter

def count_pairs_of_zeros(some_nums: list) -> int:
    """
    Counts the number of pairs of zeros in a list
    """
    zero_counter = 0
    for i in range(1, len(some_nums)):
        if some_nums[i] == 0 and some_nums[i -1] == 0:
            zero_counter += 1
    
    return zero_counter

def main() -> None:
    some_nums = [0, 2, 0, 0, 3, 4, 0, 0, 1, 0, 2, 5, 0, 0]
    print(count_zeros(some_nums))
    print(count_pairs_of_zeros(some_nums))

main()