"""
Markbook Application
Group members:
"""
from typing import Dict
import json

studentlist = []
assignmentlist = []
classdict = {"coursecode" : None, "coursename" : None, "period" : None, "teachername" , None}
classdict.update({"studentlist" : studentlist})
classdict.update({"assignmentlist" : assignmentlist})

student_dictionary = {}
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
    grade = int(input("What grade is the student in? "))
    #average_mark = ???
    email = input("What is the student's email? ")
    comments = input("Do you have any comments? Input them separated by a comma and a space ")
    
    comments_list = comments.split(", ")
    
    student_dictionary[student_number] = [first_name, last_name, gender, grade, email, comments_list]
    return("The student has been added!")

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
            return("The student has been removed!")
            break
        else:
            return("That is not a valid number.")
    


def add_student(first_name: str, last_name: str, gender: str, student_number: int, grade: int, email: str, marks: list, comments: str):
    """Add student's info with the provided key/value pairs

    Args:
        first_name: first name of student
        last_name: last name of student
        gender: gender of student
        student_number: student number of student
        grade: grade of student
        email: email of student
        marks: list of student marks
        comments: comments from teacher
    """

    print(student_list)

    student_list.append({first_name, last_name, gender, student_number, grade, email, marks, comments})
    print(student_list)


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
        print("4 - Add Student to Classroom\n5 - Remove Student from Classroom\n6 - Add Student")
        print("7 - Edd Student\n8 - Exit Program")
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
            marks = []
            answer = None
            first_name = input("What is student's first name?: ")
            last_name = input("What is student's last name?: ")
            gender = input("What is student's gender?: ")
            student_number = input("What is student's student number?: ")
            grade = input("What is student's grade?: ")
            email = input("What is student's email?: ")
            while True:
                marks.append(int(input("Enter student mark")))
                answer = input("Enter another mark? (1 for yes, 2 for no): ")
                if answer == "2":
                    break
                else:
                    pass
            comments = input("Add comment about student: ")

            add_student(first_name, last_name, gender, student_number, grade, email, marks, comments)

        elif user == "7":
            # edit_student()
            pass

        elif user == "8":
            break

        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


main()
