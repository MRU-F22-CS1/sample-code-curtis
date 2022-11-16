def to_pig_latin(word: str) -> str:
    """
    Converts a word to the pig latin version.
    """
    first_letter = word[0]
    rest_of_word = word[1:len(word)]
    return rest_of_word + first_letter + "ay"

def main() -> None:
    # word = input("What would you like to convert to pig latin? ")
    # pig_word = to_pig_latin(word)
    # print("Your word in pig latin is", pig_word)
    sentence = input("What would you like to convert? ")
    words = sentence.split()
    for i in range(0, len(words)):
        words[i] = to_pig_latin(words[i])
    
    # needs index position to change list
    # the following loop does nothing!
    # for word in words:
    #     word = to_pig_latin(word)
    
    print(" ".join(words))

main()