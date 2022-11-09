number = int(input("Enter a number: "))
small = number
large = number

number = int(input("Enter a number: "))

while number >= 0:
    if number > large:
        large = number
    elif number < small:
        small = number
    
    number = int(input("Enter a number: "))

print(large - small)