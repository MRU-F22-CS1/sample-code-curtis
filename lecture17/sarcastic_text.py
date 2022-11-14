def make_sarcastic(phrase: str) -> str:
    """
    Converts a string into alternating upper/lower case
    """

    s_phrase = ""
    for i in range(len(phrase)):
        if phrase[i] == " ":
            s_phrase += " "
        elif i % 2 == 0:
            # s_phrase = s_phrase + phrase[i].upper()
            s_phrase += phrase[i].upper()
        else:
            s_phrase += phrase[i].lower()
    
    return s_phrase

def main() -> None:
    sentence = input("Enter the phrase to make sarcastic: ")
    sarcastic = make_sarcastic(sentence)
    print(sarcastic)

main()