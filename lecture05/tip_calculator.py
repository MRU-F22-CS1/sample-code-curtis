# Illustrating use of triple quotes to display a multi-line string
print("""Welcome!
This is the tip-out calculator 1000
""")

n_employees = 6
sales = 8000
TIP_PERCENT = 0.02
tip_each = sales * TIP_PERCENT / n_employees
print("Everyone gets $", tip_each, sep="")