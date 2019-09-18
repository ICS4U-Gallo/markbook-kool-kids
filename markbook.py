"""
Markbook Application
Group members: 
"""
from typing import Dict


def main():
    while True: 
        while True:
            try:
                menu_choice = int(input("Menu Choice: "))
            except ValueError:
                print("Invalid Option, please choose again")
                input("Back to menu [Enter]...")
            break
        # Adding/editing/removing student profile
        if menu_choice == 1:
            student_profile()

        # Adding/editing/removing course class information
        elif menu_choice == 2:
            class_info()

        # Adding/editing/removing assignment
        elif menu_choice == 3:
            assignments()
"Students"
mark = int(input("Please input mark: "))

def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
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
