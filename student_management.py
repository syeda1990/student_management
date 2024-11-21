# class handels student information 
class Student:
    def __init__(self):
        pass
    def update_student_info(self):
        pass
    def display_all_students(self):
        pass

# class that will do student mangament functions
class StudentManagement:
    def __init__(slef):
        pass
    def add_student(self):
        pass
    def view_student(self):
        pass
    def update_student(self):
        pass
    def delete_student(self):
        pass
    def save_students_to_file(self):
        pass
    def load_students_from_file(self):
        pass





# the main program begins
system=StudentManagement()
while (True):
    print("\n Student Management System")
    print("1. Add a new student")
    print("2. View all students")
    print("3. Update a student information")
    print("4. Remove a student information")
    print("5. Save to a File and Exit")

    choice=int(input("Select a option from 1-5 "))

    if choice ==1 :
        system.add_student()
    elif choice ==2:
        system.view_student()
    elif choice ==3:
        system.update_student()
    elif choice ==4:
        system.delete_student()
    elif choice ==5:
        system.save_students_to_file()
        break
    else:
        print("Please enter a valid choice")

