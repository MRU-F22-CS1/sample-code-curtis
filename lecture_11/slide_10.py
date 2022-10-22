def check_caffeine(caffeine: float) -> None:
    if caffeine > 200:
        print("TOO MUCH!")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 50:
        print("Good start")
    else:
        print("You need more!")

def check_caffeine_bad_order(caffeine: float) -> None:
    if caffeine > 50:
        print("Good start")
    elif caffeine > 100:
        print("Perfect amount")
    elif caffeine > 200:
        print("TOO MUCH!")
    else:
        print("You need more!")

def main() -> None:
    level = float(input("How much caffeine have you had? "))
    check_caffeine(level)
    check_caffeine_bad_order(level)

main()