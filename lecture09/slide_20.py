GST = 0.05

def show_safeway_total(is_first_tuesday: bool, purchase: float) -> None:
    """
    Prints out the total purchase with GST. If it's the first Tuesday
    and the purchase is over $50, subtract 15% pre-tax.
    """
    if is_first_tuesday and purchase > 50:
        purchase = purchase * 0.85
        print("Congratulations! You qualify for the discount!")

    total = purchase * (1 + GST)
    print(f"Total: ${total:.2f}")

def main():
    purchase = float(input("Enter the purchase amount: "))
    show_safeway_total(True, purchase)

main()