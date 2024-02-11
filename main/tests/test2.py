# Import the unittest module

import unittest

from main.tests import session
# Import the Student class and the generate_study_times function from your module
from student import Student
from session import Session


# Define a test case class that inherits from unittest.TestCase
class TestGenerateStudyTimes(unittest.TestCase):

    # Define a test method that starts with test_
    def test_generate_study_times(self, exam_time=None):
        # Create a student object with some courses and exam times
        student = Student(name="Alice", email= "alice.com", courses={
            "Math": "2024-02-10 10:00:00",
            "Physics": "2024-02-11 12:00:00",
            "Chemistry": "2024-02-12 14:00:00"
        })

        # Define the priority, session length, and waking hours for the test
        priority = {
            "Math": "High",
            "Physics": "Medium",
            "Chemistry": "Low"
        }
        session_length = 60 # minutes
        waking_hours = (8, 22) # hours

        # Call the generate_study_times function and store the result
        study_times = session.Session.generate_study_times(self, "8:00:00AM", (8,22), "200",{"Math": "High", "Physics": "Medium", "Chemistry": "Low"},)

        # Print the study times for debugging
        print(study_times)

        # Assert that the result is a list of tuples
        self.assertIsInstance(study_times, list)
        for item in study_times:
            self.assertIsInstance(item, tuple)

        # Assert that the result contains the expected number of sessions for each course
        # Based on the priority multiplier and the session length
        self.assertEqual(study_times.count(("Math",)), 3 * (student.get_course_length("Math") // session_length))
        self.assertEqual(study_times.count(("Physics",)), 2 * (student.get_course_length("Physics") // session_length))
        self.assertEqual(study_times.count(("Chemistry",)), 1 * (student.get_course_length("Chemistry") // session_length))

        # Assert that the result is sorted by priority and time
        # The highest priority course should be scheduled first and closest to the exam time
        self.assertListEqual(study_times, sorted(study_times, key=lambda x: (priority[x[0]], x[1]), reverse=True))

# Run the test case
if __name__ == "__main__":
    unittest.main()
