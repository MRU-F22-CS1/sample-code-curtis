def get_courses() -> list:
    """
    Prompts the user to add courses to a list, then returns it.
    """
    course_list = []
    prompt = "Enter the name of a course to add, or press Enter to finish: "
    course = input(prompt) # priming read
    while course != "":
        course_list.append(course)
        course = input(prompt) # internal read
    
    print(len(course_list), "courses added")
    return course_list

def find_highest(courses: list) -> str:
    """
    Looks through the course list and finds the highest code.
    """
    highest_code = 0
    highest_course = ""
    for i in range(0, len(courses), 1):
        components = courses[i].split()
        code = int(components[1])
        if code > highest_code:
            highest_code = code
            highest_course = courses[i]
    
    return highest_course

def main() -> None:
    # courses = get_courses()
    courses = ["COMP 1501", "Math 1505", "GNED 1401", "GNED 1103", "MKTG 2150",
               "COMP 1502", "COMP 2511", "MGMT 3210", "HRES 2170", "GNED 1101"]
    print(courses)
    print(find_highest(courses))

main()