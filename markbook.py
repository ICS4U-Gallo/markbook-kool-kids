"""
Markbook Application
Group members: Terry, Bryan, Mary, Sydney, Mehana
"""
from typing import Dict, List
import json

student_dictionary = {}
user = 0
average_mark = 0
student_list = []
assignment_list = []
with open("studentlist.json", "r") as f:
    student_list = json.load(f)


def create_assignment() -> List:
    while True:
        name = None
        due = None
        points = None
        name = input("Enter assignment name: ")
        due = input("Enter assignment due date: ")
        points = input("Enter number of points: ")
        new_assignment = {
            "name": name, "due_date": due,
            "points": points
        }
        assignment_list.append(dict(new_assignment))
        if input("""
                Press space then enter to view assignments or
                Press enter to add more assignments:
                    """) == " ":
            print(assignment_list)
            break

    return assignment_list


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    class_dictionary = {"course_code": course_code, "course_name": course_name, "period": period, "teacher": teacher}
    class_dictionary.update({"student list": student_list})
    class_dictionary.update({"assignment list": assignment_list})
    return class_dictionary


def calculate_average_mark() -> float:
    """Calculates the average mark of a student"""
    global average_mark
    total_mark = 0
    target_student_number = int(input("Enter the student number:"))
    for student in range(len(student_list)):
        for key, val in student_list[student]:
            if key == "student_number" and val == target_student_number:
                for i in range(len(student_list[i]["marks"])):
                    marks = ["marks"][i]
                    total_mark += marks
                average_mark = total_mark/(len(student_list[i]["marks"]))
            else:
                continue
    return average_mark


def add_student_to_classroom():
    """Adds student to a classroom
    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    student_number = int(input("What is the student's number? "))
    first_name = input("What is the student's first name? ")
    last_name = input("What is the student's last name? ")
    gender = input("Is the student male or female? ")
    grade = int(input('What grade is the student in? '))
    average_mark_output = calculate_average_mark()
    email = input("What is the student's email? ")
    comments = input("Do you have any comments? Input them separated by a comma and a space ")
    comments_list = comments.split(", ")
    student_dictionary[student_number] = [first_name, last_name, gender, average_mark_output, grade, email, comments_list]
    return "The student has been added!"


def remove_student_from_classroom():
    """Removes student from classroom
    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    remove_student_number = (int(input("What's the student's number? ")))
    for number in student_dictionary.keys():
        if number == remove_student_number:
            student_dictionary.pop(number)
            return "The student has been removed!"
        else:
            return "That is not a valid number."


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs
    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    pass


def main():
    global user
    print("\nWelcome!")
    while True:
        print("\n1 - Create Assignment\n2 - Create Classroom\n3 - Add Student to Classroom")
        print("4 - Remove Student from Classroom\n5 - Edit Student\n6 - Exit Program")
        user = input("\nInput a Number: ")

        # Creates Assignments
        if user == "1":
            create_assignment()

        elif user == "2":
            course_code = input("\nEnter the course code of the class: ")
            course_name = input("Enter the name of the class: ")
            period = input("Enter what period the class is: ")
            teacher = input("Enter the name of the teacher: ")
            print(create_classroom(course_code, course_name, period, teacher))

        elif user == "3":    
            add_student_to_classroom()

        elif user == "4":
            remove_student_from_classroom()

        elif user == "5":
            # edit_student()
            pass

        elif user == "6":
            break

        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
