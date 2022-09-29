name = input("Please enter your name: ")
coffees = input("How many coffees have you had today? ")
coffees = int(coffees)
mL_coffee = coffees * 300

print("Hello,", name)
print("You've had", coffees, ". That's", mL_coffee, "mL")