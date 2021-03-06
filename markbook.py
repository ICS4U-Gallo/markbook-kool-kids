"""
Markbook Application
Group members: Terry, Bryan, Mary, Sydney, Mehana
"""
from typing import Dict, List
import json

student_dictionary = {}
user = 0
average_mark = 0
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


def edit_assignment() -> List:
    assignment_name = input("Assignment Name: ")
    for assignment in range(len(assignment_list)):
        if assignment_list[assignment]["name"] == assignment_name:
            edit_item = input("Edit name, due date or points OR enter to exit: ")
            if edit_item == "name":
                new_name = input("Enter new name: ")
                assignment_list[assignment]["name"] = new_name
            elif edit_item == "due date":
                new_date = input("Enter new due date: ")
                assignment_list[assignment]["due"] = new_date
            elif edit_item == "points":
                new_points = input("Enter new points: ")
                assignment_list[assignment]["points"] = new_points
            elif edit_item == "":
                break
            else:
                print("Invalid Input")

    return assignment_list


def remove_assignment() -> List:
    assignment_name = input("Assignment Name: ")
    for assignment in range(len(assignment_list)):
        if assignment_list[assignment]["name"] == assignment_name:
            del assignment_list[assignment]

    return assignment_list


# Collects points(denominator)into one list
def assignment_mark() -> List:
    assignment_mark_list = []
    for assignment in assignment_list:
        for key in assignment:
            if key == "points":
                points = int(assignment.get("points"))
                assignment_mark_list.append(points)

    return assignment_mark_list


# Returns the average mark of each student's assignments
def assignment_avg_marks(assignment_mark_list):
    assignment_avg_list = []
    student_number = int(input("Enter student number: "))
    for key in student_dictionary:
        if key == student_number:
            for mark in assignment_mark_list:
                student_mark = int(input(f"Enter student's mark out of {mark}: "))
                average = (student_mark / mark) * 100
                assignment_avg_list.append(round(average))
    student_dictionary[student_number].append(assignment_avg_list)


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
    assignment_avg_list = []
    average_mark_output = calculate_average_mark()
    email = input("What is the student's email? ")
    comments = input("Do you have any comments? Input them separated by a comma and a space ")
    comments_list = comments.split(", ")
    student_dictionary[student_number] = [first_name, last_name, gender, grade, email, comments_list, assignment_avg_list, average_mark_output]
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

#user can change values in student dictionary
def edit_student():
    print(student_dictionary)
    student_number = (int(input("Enter the number of the student you want to change. ")))
    for student in range(len(student_dictionary)):
        if student == student_number:
            edit_item = input("Edit first name, last name, gender, grade, email, comments, or enter to exit: ")
            if edit_item == "first name":
                new_first_name = input("Enter the new first name ")
                student_dictionary[student_number][0] = new_first_name
            elif edit_item == "last name":
                new_last_name = input("Enter the new last name ")
                student_dictionary[student_number][1] = new_last_name
            elif edit_item == "gender":
                new_gender = input("Enter the new gender ")
                student_dictionary[student_number][2] = new_gender
            elif edit_item == "grade":
                new_grade = input("Enter the new grade ")
                student_dictionary[student_number][3] = new_grade
            elif edit_item == "email":
                new_email = input("Enter the new email ")
                student_dictionary[student_number][4] = new_email
            elif edit_item == "comments":
                student_dictionary[student_number][5].append(input("Enter a comment "))
            else:
                return "Invalid input. "


def main():
    global user
    print("\nWelcome!")
    while True:
        print("\n1 - Assignments\n2 - Create Classroom\n3 - Add Student to Classroom")
        print("4 - Remove Student from Classroom\n5 - Edit Student\n6 - Input Student Marks\n7 - Exit Program")
        user = input("\nInput a Number: ")

        # Creates Assignments
        if user == "1":
            print("\n1 - Create Assignment\n2 - Edit Assignments\n3 - Remove Assignment")
            user = input("\nInput a Number: ")
            if user == "1":
                create_assignment()
            elif user == "2":
                edit_assignment()
            elif user == "3":
                remove_assignment()
            else:
                print("Invalid Input")

        elif user == "2":
            course_code = input("\nEnter the course code of the class: ")
            course_name = input("Enter the name of the class: ")
            period = int(input("Enter what period the class is: "))
            teacher = input("Enter the name of the teacher: ")
            print(create_classroom(course_code, course_name, period, teacher))

        elif user == "3":
            add_student_to_classroom()

        elif user == "4":
            remove_student_from_classroom()

        elif user == "5":
            edit_student()

        elif user == "6":
            assignment_avg_marks(assignment_mark())

        elif user == "7":
            break

        else:
            print("\n<<Invalid Input>>")
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
