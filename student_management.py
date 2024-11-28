# class handels student information 
class Student:
    def __init__(self, student_id, name, age, grade, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
        
    def update_student_info(self):
        pass
    def display_all_students(self):
        pass

# class that will do student mangament functions
class StudentManagement:
    def __init__(self):
        self.students=[]

    def add_student(self, student_id, name, age, grade, subjects):
        id_exists = False
        for student in self.students:
            if student.student_id == student_id:
                id_exists = True  
                break
        if id_exists:
            print("ID already exists. Please enter a unique ID.")
            return "ID already exists."
        self.students.append(Student(student_id, name, age, grade, subjects))
        return "Student added successfully."
    
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
if __name__ == "__main__":
    system=StudentManagement()
    try:

        while (True):
            print("\n Student Management System")
            print("1. Add a new student")
            print("2. View all students")
            print("3. Update a student information")
            print("4. Remove a student information")
            print("5. Save to a File and Exit")

            choice=int(input("Select a option from 1-5 "))

            if choice ==1 :
                student_id = int(input("\nEnter Student ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                grade = input("Enter Grade: ")
                subjects = input("Enter Subjects (comma-separated): ").split(',')
                print(system.add_student(student_id, name, age, grade, [s.strip() for s in subjects]))

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

    except ValueError:
        print("Invalid input.Please try again")