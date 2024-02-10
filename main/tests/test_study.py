import unittest
import json
import tkinter as tk
from main import app
from main.models import Student

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
        student = Student(id=1, name='Test Student')

        # Define the study session data
        session_data = {
            'student_id': student.id,
            'goals': ['Read Chapter 1', 'Solve Exercise 1'],
            'study_interval': 25,
            'break_interval': 5
        }

        # Send a POST request to the create_study_session route
        response = self.client.post('/create_study_session', data=json.dumps(session_data), content_type='application/json')

        # Check the response status code and data
        # self.assertEqual(response.status_code, 404)
        # self.assertIn('Study session created successfully', response.data.decode())

if __name__ == '__main__':
    unittest.main()
