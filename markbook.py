"""
Markbook Application
Group members: 
"""
from typing import Dict

user = 0


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assigment_name = input("Enter assignment name: ")
    due_date = input("Enter assignment due date: ")
    points = input("Enter number of points: ")
    assignment = {
        "name": input("Enter assignment name: "), "due_date": input("Enter due date: "), "points": input("Enter number of points: ")
        }
    return {}


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
            # create_assignment()
            pass
        elif user == "2":
            # create_classroom()
            pass
        elif user == "3": 
            # calculate_average_mark()
            pass
        elif user == "4":
            # add_student_to_classroom()
            pass
        elif user == "5":
            # remove_student_from_classroom()
            pass
        elif user == "6":
            # edit_student()
            pass
        elif user == "7":
            break
        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


main()
