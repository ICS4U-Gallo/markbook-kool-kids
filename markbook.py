"""
Markbook Application
Group members: 
"""
"hi brobert"

"Menu"
print("Markbook")
print("Press 1 to add student profile")
print("Press 2 for course class information")
print("Press 3 for assignments")

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

def some_func():
    return True
