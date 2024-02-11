import database

conn = database.create_connection()
database.create_table(conn)
database.insert_student(conn, 'student2@example.com', 'test student', 'math, english')

student = database.get_student(conn, 'student2@example.com')
print(student)
students = database.get_all_students(conn)
print(students)


'''
    What to design:
    
    Sample calendar GUI:
    
    With the following options:
    
    Flipping from light to dark mode
    
    Allowing for a student to place a timer for some set time.
    
    The student is able to set a timer for X time
        -The task at hand must be specified
        -Once the timer is done, the app will ask if they completed their task
        -Possible option: (could be toggled) in order to keep the student 
        engaged; have a pop up/reminder in order to make sure the student is still
        studying: 
    
        
    Frameworks being utilized:
    
    Flask
    
    
    


'''