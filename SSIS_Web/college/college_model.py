from flask_mysql_connector import MySQL

mysql = MySQL()

def get_college_data():
    if not mysql.connection.is_connected():
        return "Database connection is not established!"
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM college")
    fetchdata = cur.fetchall()
    cur.close()
    
    return fetchdata

