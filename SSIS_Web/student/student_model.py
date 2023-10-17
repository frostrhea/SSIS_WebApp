from flask_mysql_connector import MySQL

class StudentManager:
    def __init__(self, mysql):
        self.mysql = mysql

    @classmethod
    def init_db(cls, mysql):
        cls.mysql = mysql

    @classmethod
    def get_student_data(cls):
        if not cls.mysql.connection.is_connected():
            print("Database connection is not established!")
            return "Database connection is not established!"

        cur = cls.mysql.connection.cursor(dictionary=True)
        cur.execute("SELECT * FROM student_info")
        student_data = cur.fetchall()
        cur.close()

        return student_data

    @classmethod
    def add_student(cls, id, firstname, lastname, course, gender, year):
        try:
            # Check if the student with the given ID already exists
            cur = cls.mysql.connection.cursor()
            cur.execute("SELECT * FROM student_info WHERE `id` = %s", (id,))
            if cur.fetchone():
                print(f"Student with ID '{id}' already exists.")
            else:
                # Insert a new student into the database
                cur.execute("INSERT INTO student_info (`id`, `firstname`, `lastname`, `course`, `gender`, `year`) VALUES (%s, %s, %s, %s, %s, %s)",
                            (id, firstname, lastname, course, gender, year))
                cls.mysql.connection.commit()
                print(f"Student '{firstname} {lastname}' with ID '{id}' has been added.")
        except Exception as e:
            print(f"Error adding student: {e}")

    @classmethod
    def delete_student(cls, student_id):
        try:
            cur = cls.mysql.connection.cursor()
            cur.execute("SELECT * FROM student_info WHERE `id` = %s", (student_id,))
            student = cur.fetchone()

            if student:
                # Delete the student from the database
                print("Deleting student with ID:", student_id)
                cur.execute("DELETE FROM student_info WHERE `id` = %s", (student_id,))
                cls.mysql.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error deleting student: {e}")
            return False
