x = 5
y = 10

x < y
# 5 < 10 -> True

x < y and x * y <= 50
# 5 < 10 and 5 * 10 <= 50
# True   and True -> True

not (x > 5 or y < 20) and x + y > 10
# not (False or True) and True
# not (True) and True
# False and True -> False

x == 5 or y != 20
# True or True -> True