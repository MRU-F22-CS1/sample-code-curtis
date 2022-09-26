# Unicode characters can be entered as \uxxxx or as glyphs directly
# However, not all systems and terminals will display all characters
print("Ace of \u2661")
print("Don't forget your \u2614")
print("Running out of ⏳")

# Modifying the separator and end-of-line characters
print("Ace of", "\u2660", sep=" ")
print(1, 2, 3, 4, 5, sep=" kittens ")
print(1, 2, 3, 4, 5, sep="\n", end="\n\n\nDone!\n")