def highest_quiz(quiz1: list, quiz2: list) -> list:
    """
    Creates a list with the highest of each element in
    quiz1 and quiz2.
    """
    highest = []
    for i in range(len(quiz1)):
        if quiz1[i] > quiz2[i]:
            highest.append(quiz1[i])
        else:
            highest.append(quiz2[i])
    
    return highest

def main() -> None:
    quiz1 = [30, 32.5, 5, 10]
    quiz2 = [30, 33, 0, 15]
    print(highest_quiz(quiz1, quiz2))

main()