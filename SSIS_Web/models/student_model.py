from flask_mysql_connector import MySQL

class StudentManager:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_student_data(self):
        if not self.mysql.connection.is_connected():
            print("Database connection is not established!")
            return "Database connection is not established!"

        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM student_info")
        fetchdata = cur.fetchall()
        cur.close()

        student_data = []
        for row in fetchdata:
            student = {
                'id': row[0],
                'firstname': row[1],
                'lastname': row[2],
                'course': row[3],
                'year': row[4],
                'gender': row[5]
            }
            student_data.append(student)

        return student_data
    
    def addStudent(self, id, name, gender, year, stud_course):
        try:
            # Check if the student with the given ID already exists
            self.cursor.execute("SELECT * FROM student_info WHERE `Student ID` = %s", (id,))
            if self.cursor.fetchone():
                print(f"Student with ID '{id}' already exists.")
            else:
                # Insert a new student into the database
                self.cursor.execute("INSERT INTO student_info (`Student ID`, `Name`, `Gender`, `Year Level`, `Course Code`) VALUES (%s, %s, %s, %s, %s)",
                                    (id, name, gender, year, stud_course))
                self.connection.commit()
                print(f"Student '{name}' with ID '{id}' has been added.")
        except Exception as e:
            print(f"Error adding student: {e}")
