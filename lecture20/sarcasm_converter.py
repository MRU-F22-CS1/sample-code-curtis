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

def read_file(filename: str) -> str:
    """
    Reads the contents of filename into a string.
    """
    try:
        f = open(filename, "r")
        contents = f.read()
        f.close()
    except OSError:
        print(f"Can't open {filename}")
        contents = "Error"

    return contents

def write_file(filename: str, contents: str) -> None:
    """
    Writes contents to filename
    """
    try:
        f = open(filename, "w")
        f.write(contents)
        f.close()
    except OSError:
        print(f"Could not write to {filename}")

def main() -> None:
    file_to_read = input("Enter the file to read: ")
    text = read_file(file_to_read)
    sarcastic = make_sarcastic(text)
    write_file("sarcastic.txt", sarcastic)

main()