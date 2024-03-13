import psycopg2
   
def connect_db():
    return psycopg2.connect(
        dbname="A3Q1",
        user="postgres",
        password="postgres",
        host="localhost"
    )

def createTable():
    conn = connect_db()
    cur = conn.cursor()
    deleteTable()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        )
    '''
    cur.execute(create_table_query)
    
    conn.commit()
    
    cur.close()
    conn.close()


def deleteTable():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS students")
    conn.commit()
    cur.close()
    conn.close()

    
def getAllStudents():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    cur.close()
    conn.close()

def deleteStudent(student_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    cur.close()
    conn.close()



if __name__ == "__main__":
    createTable()
    #Insert 3 example students
    addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
    addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
    addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

    #Insert 2 new students
    addStudent ('Anne', 'Dang', 'annedang@gmail.com', '2023-09-02')
    addStudent ('Bill','Cheng', 'billcheng@gmail.com', '2023-09-02')

    #Update email
    updateStudentEmail(1, "john.doe@gmail.com")

    #Delete student with id 4
    deleteStudent(4)

     #Get all students
    getAllStudents()
