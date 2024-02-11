import unittest
import json
from main import app
from main.models import Student
from main.tests import database
from main.tests.oldpomodoro_implementation.pomodoro import Pomodoro

#Implement a GUI using Tkinter for the following student object in the following matter:

'''
    Allowing for the student to input the following information:
    
    goals
    study-time
    break time

    

'''

class StudyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_create_study_session(self):
        # Create a new student
        student = Student(email=1, name='Test Student', courses='test1, test2')

        # Define the study session data
        session_data = {
            'student_email': student.email,
            'goals': ['Read Chapter 1', 'Solve Exercise 1'],
            'study_interval': 25,
            'break_interval': 5
        }


        #add student details into database
        conn = database.create_connection()
        database.create_table(conn)
        database.insert_student(conn, student.email, student.name, student.courses)

        student = database.get_student(conn, student.email)
        print(student)

        students = database.get_all_students(conn)
        print(students)

        #begin pomodoro timer
        pomodoro = Pomodoro(session_data['study_interval'], session_data['break_interval'])



        # Send a POST request to the create_study_session route
        response = self.client.post('/create_study_session', data=json.dumps(session_data), content_type='application/json')

        # Check the response status code and data
        # self.assertEqual(response.status_code, 404)
        # self.assertIn('Study session created successfully', response.data.decode())

if __name__ == '__main__':
    unittest.main()
