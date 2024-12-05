import unittest
from student_management import StudentManagement
import json

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.system = StudentManagement()
        self.system.students = []

    def test_add_student(self):
        result=len(self.system.students)  
        self.system.add_student(101, "Zara Fathima", 20, "VG", ["Math", "Science"]) 
        self.assertEqual(len(self.system.students), result+1) 

    def test_view_students(self):
        self.system.add_student(101, "Zara Fathima", 20, "VG", ["Math", "Science"])
        result = self.system.view_students() 
        self.assertIn("Zara Fathima", result) 

    def test_update_student(self):
        self.system.add_student(101, "Zara Fathima", 20, "VG", ["Math", "Science"])
        self.system.update_student(101,"Updated Name")
        student_names = [student.name for student in self.system.students]
        self.assertIn("Updated Name", student_names)  

    def test_delete_student(self):
        self.system.add_student(202, "Zayd Mohammed", 20, "VG", ["Math", "Science"])
        result=len(self.system.students)
        self.system.delete_student(202) 
        self.assertEqual(len(self.system.students), result-1)  

    def test_save_students_to_file(self):  
        self.system.add_student(101, "Zara Fathima", 20, "VG", ["Math", "Science"])     
        self.system.save_students_to_file()
        with open("student.json", "r") as file:
            data = json.load(file)
        self.assertTrue(any(student["name"] == "Zara Fathima" for student in data))

    def test_load_students_from_file(self):
        self.system.load_students_from_file()
        student_names = [student.name for student in self.system.students]
        self.assertIn("Zara Fathima", student_names)

if __name__ == "__main__":
    unittest.main()
