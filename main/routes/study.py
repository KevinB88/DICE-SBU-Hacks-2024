from flask import Blueprint, request
from models import Student, Session

study = Blueprint('study', __name__)


@study.route('/create_study_session', methods=['POST'])
def create_study_session():
    data = request.get_json()
    student_email = data.get('student_email')
    goals = data.get('goals')
    study_interval = data.get('study_interval')
    break_interval = data.get('break_interval')

    # Create a new study session
    session = Session(email=None, student_email=student_email, goals=goals, study_interval=study_interval,
                      break_interval=break_interval)

    # Add the session to the student's data
    # You'll need to implement this part based on how you're storing student data
    # For example, if you're using a database, you might add a row to a 'sessions' table

    return {"message": "Study session created successfully"}, 200
