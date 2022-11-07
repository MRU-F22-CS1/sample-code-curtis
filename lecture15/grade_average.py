def average_grades() -> float:
    """
    Repeatedly prompts user for grade, shows running average.
    Returns final average value.
    """
    prompt = "Enter the grade (-1 to stop): "
    grade = float(input(prompt))
    sum = 0
    count = 0
    while grade >= 0:
        sum = sum + grade
        count = count + 1
        print(f"Running average: {sum / count:.1f}")
        grade = float(input(prompt))
    
    # Should probably make sure count isn't 0
    return sum / count

def main() -> None:
    average = average_grades()
    print(f"The final average is {average:.1f}")

main()