def print_clock() -> None:
    for hour in range(24):
        print("Ring! " * hour)
        for min in range(60):
            for sec in range(60):
                print(f"{hour:02}:{min:02}:{sec:02}")

def main() -> None:
    print_clock()

main()