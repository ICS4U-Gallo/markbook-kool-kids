"""
Markbook Application
Group members:
"""
from typing import Dict
import json

user = 0
with open("studentlist.json", "r") as f:
    student_list = json.load(f)


def create_assignment(name: str, due: str, points: int) -> Dict:
    assignment_list = []

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
        break

return assignment_list


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    return 0


def add_student_to_classroom(student, classroom):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    pass


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    pass


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
        print("\n1 - Create Assignment\n2 - Create Classroom\n3 - Calculate Average Mark")
        print("4 - Add Student to Classroom\n5 - Remove Student from Classroom\n6 - Edit Student")
        print("7 - Exit Program")
        user = input("\nInput a Number: ")

        if user == "1":
            name = input("\nEnter the name of the assignment: ")
            due = input("Enter the due date of the assignment: ")
            points = input("Enter what the assignment is out of: ")
            # create_assignment(name, due, points)

        elif user == "2":
            code = input("\nEnter the course code of the class: ")
            name = input("Enter the name of the class: ")
            period = input("Enter what period the class is: ")
            teacher = input("Enter the name of the teacher: ")
            # create_classroom(code, name, period, teacher)

        elif user == "3":
            name = input("\nEnter the name of the student: ")
            # calculate_average_mark(name)

        elif user == "4":
            name = input("\nEnter the name of the student: ")
            classroom = input("Enter the name of the class: ")
            # add_student_to_classroom(name, classroom)

        elif user == "5":
            name = input("\nEnter the name of the student: ")
            classroom = input("Enter the name of the class: ")
            # remove_student_from_classroom(name, classroom)

        elif user == "6":
            # edit_student()
            pass

        elif user == "7":
            break

        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


main()
