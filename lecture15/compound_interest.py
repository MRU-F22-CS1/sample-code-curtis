INTEREST = 0.02

def years_to_500(initial: float) -> int:
    """
    Calculate number of years to reach $500, starting with $initial.
    """
    years = 0
    balance = initial
    while balance < 500:
        balance *= (1 + INTEREST)
        balance += 50
        years += 1
    
    return years

def main() -> None:
    deposit = float(input("Enter the initial deposit: "))
    print(f"It takes {years_to_500(deposit)} years to reach $500")

main()