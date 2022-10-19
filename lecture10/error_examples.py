# Syntax errors
# a variable = 5
#     bad_indent = 8

# Runtime errors
# print(f"Dividing by zero: {5 / 0}")
# number = int("3.14159")

# logic errors
x = 1
if x < 100 and x > 200: # Always false
    print("This will never happen")

y = 10
if x or y > 20: # should be x > 20 or y > 20
    print("One of them is over 20")