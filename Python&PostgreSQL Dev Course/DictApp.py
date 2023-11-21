import statistics

grade_level = [{'name1': 'Alvin', 'name2': 'Draper', 'scores': [88.0, 77.0, 70.0, 89.0]},
               {'name1': 'Xenia', 'name2': 'Quintaro', 'scores': [85.0, 78.0, 69.0, 90.0]}]


def create_student():
    # Ask user for student info
    s_name1 = input("What is the student's given name? ")
    s_name2 = input("What is the student's family name? ")
    scores = input("What are the student's class scores? (Separated by comma)").split(",")
    if len(scores) == 0:
        scores = ['0']
    # Create student profile
    student_profile = {"name1": s_name1, "name2": s_name2, "scores": [float(a) for a in scores]}
    return student_profile


def add_score(student_profile, new_score):
    student_profile["scores"].append(new_score)


def calc_avg_score(student):
    if len(student["scores"]) == 0:
        return 0
    else:
        return round(statistics.mean(student["scores"]), 2)


def student_details(student):
    return "Student: {} {}, Average Grade: {}".format(student["name1"], student["name2"], calc_avg_score(student))


def find_student(student):
    names = student.split(",")
    for s in grade_level:
        if names[0] == s["name2"]:
            return s


def grade_level_details(students):
    for i, p in enumerate(students):
        print("ID: {} ".format(i))
        print(student_details(p))


def menu_prompt():
    return input("p to print all student grades, "
                      "n to add a new student, "
                      "s to add a new score, "
                      "g to see a specific student's scores, "
                      "or q to quit. "
                      "Enter Selection: ")


def menu():
    # add student
    # add score
    # print list of students
    # exit

    selection = menu_prompt()
    while selection != 'q':
        if selection == 'p':
            print(grade_level_details(grade_level))
        elif selection == 'n':
            grade_level.append(create_student())
        elif selection == 's':
            student = input("Which student's scores will be updated and what is the score? (ID, 99)")
            student = student.replace(" ", "")
            items = student.split(",")
            try:
                ID = items[0]
                score = items[1]
                add_score(grade_level[int(ID)], float(score))
                print("Student {} {} updated".format(grade_level[int(ID)]['name1'], grade_level[int(ID)]['name2']))
            except:
                print("Error.")
        else:
            print("Something went wrong. Please try again.")
        selection = menu_prompt()


menu()
