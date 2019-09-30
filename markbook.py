"""
Markbook Application
Group members:
"""
from typing import Dict
import json

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
    student_list = []
    assignment_list = []
    classdict = {"course code" : None, "course name" : None, "period" : None, "teacher" , None}
    classdict.update({"student list" : student_list})
    classdict.update({"assignment list" : assignment_list})
    return {}


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    
    targert_student_number = int(input("Enter the student number:"))
    for i in range(len(student_list)):
        for key, val in student_list[i]:
            if key == "student_number" and val == target_student_number:
                for i in range(len(student_list[i]["marks"])):
                    marks = ["marks"][i]
                    total_mark += marks
                average_mark = total_mark/(len(student_list[i]["marks"])
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


def edit_student():
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    number = int(input("What is the student's student number?"))

    for i in range(len(student_list)):
        if number == student_list[i]["student_number"]:
            print("What would you like to edit?\n1 - First Name\n2 - Last Name")
            key_number = input("3 - Gender\n4 - Grade\n5 - Email")

            if key_number == "1":
                key = "first_name"
            elif key_number == "2":
                key = "last_name"
            elif key_number == "3":
                key = "gender"
            elif key_number == "4":
                key = "grade"
            elif key_number == "5":
                key = "email"

            value = input("Enter new info: ")

            student_list[i][key] = value
            break

        else:
            print("Student number does not exist in system")


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
            edit_student()

        elif user == "7":
            break

        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


main()
