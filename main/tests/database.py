import sqlite3


def create_connection():
    conn = sqlite3.connect('students.db')
    return conn


def create_table(conn):
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            email TEXT PRIMARY KEY,
            name TEXT,
            courses DICT
            goals TEXT
        )
    ''')
    conn.commit()


def insert_student(conn, email, name, courses):
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (email, name, courses))
    conn.commit()


def get_student(conn, email):
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE email=?", (email,))
    student = c.fetchone()
    return student


def get_all_students(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    return students


def update_student(conn, email, name, courses):
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, courses=? WHERE email=?", (name, courses, email))
    conn.commit()


def delete_student(conn, email):
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE email=?", (email,))
    conn.commit()
