from flask_mysql_connector import MySQL

mysql = MySQL()

def get_course_data():
    if not mysql.connection.is_connected():
        return "Database connection is not established!"
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM course")
    fetchdata = cur.fetchall()
    cur.close()
    
    return fetchdata

