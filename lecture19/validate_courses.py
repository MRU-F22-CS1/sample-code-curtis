def read_course_codes(filename: str) -> list:
    """
    Reads the contents of filename into a list of strings.
    """
    f_obj = open(filename, "r")
    courses = []
    for line in f_obj:
        courses.append(line.strip())

    f_obj.seek(0)
    # this next loop doesn't do anything without f_obj.seek(0), 
    # file already read
    for line in f_obj:
        print(line)
        # course = line.split()
        # print(int(course[1]))
    
    f_obj.close()
    return courses

def main() -> None:
    course_list = read_course_codes("lecture19/comp_courses.txt")
    print(course_list)
    
main()