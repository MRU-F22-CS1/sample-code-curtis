# Illustrating use of triple quotes to display a multi-line string
print("""Welcome!
This is the tip-out calculator 1000
""")

n_employees = int(input("How many employees on shift? "))
sales = float(input("What was the total sales? "))
TIP_PERCENT = 0.02
tip_each = sales * TIP_PERCENT / n_employees
print(f"Everyone gets ${tip_each:>10.2f}")
print(f"Employees:     {n_employees:>10}")