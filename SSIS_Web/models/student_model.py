from flask_mysql_connector import MySQL

mysql = MySQL()

def get_student_data():
    try:
        if not mysql.connection.is_connected():
            print("Database connection is not established!")
            return "Database connection is not established!"

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM student_info")
        fetchdata = cur.fetchall()
        cur.close()

        return fetchdata
    except Exception as e:
        print("Error executing SQL query:", e)
        return "Error executing SQL query: " + str(e)

