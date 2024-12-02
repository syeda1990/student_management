import unittest
from student_management import StudentManagement

class TestStudentManagement(unittest.TestCase):
    def setUp(self):
        self.system = StudentManagement()

    def test_add_student(self):
        self.system.students = []  
        self.system.add_student(1, "Zara Fathima", 20, "VG", ["Math", "Science"]) 
        self.assertEqual(len(self.system.students), 1) 

    def test_view_student(self):
        pass
    def test_update_student(self):
        pass
    '''def test_delete_student(self):
        pass
    def test_save_students_to_file(self):
        pass
    def test_save_students_from_file(self):
        pass'''

if __name__ == "__main__":
    unittest.main()
