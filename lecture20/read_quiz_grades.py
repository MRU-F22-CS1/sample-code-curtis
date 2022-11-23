def read_grades(filename: str) -> list:
    """
    Reads the info in filename into a list.
    """
    grades = []
    f = open(filename, "r")
    header = f.readline()
    for line in f:
        nums = line.split(",")
        entry = []
        for num_s in nums:
            num = float(num_s)
            entry.append(num)
        grades.append(entry)
    
    f.close()
    return grades

def main() -> None:
    quizzes = read_grades("lecture19/quiz_grades.csv")
    print(quizzes)

main()