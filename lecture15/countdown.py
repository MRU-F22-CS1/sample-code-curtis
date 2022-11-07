def countdown_timer(n: int) -> None:
    """
    Counts down from n, then prints blastoff
    """
    lcv = n
    while lcv > 0:
        print(f"{lcv}...")
        # lcv -= 1
    
    print("Blastoff!")

def countdown_for(n: int) -> None:
    """
    Counts down from n, then prints blastoff
    """
    for lcv in range(n, 0, -1):
        print(f"{lcv}...")
    
    print("Blastoff!")

def main() -> None:
    n_times = int(input("Countdown from? "))
    countdown_timer(n_times)
    countdown_for(n_times)

main()