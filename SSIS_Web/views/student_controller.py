from flask import Blueprint, render_template, jsonify, request, redirect, url_for, abort
from SSIS_Web.models.student_model import StudentManager
from flask_mysql_connector import MySQL

mysql = MySQL()
student_bp = Blueprint('student', __name__)
student = StudentManager(mysql)



@student_bp.route('/students', methods=['GET'])
def list_students():
    students = student.get_student_data()  # Fetch data from the database
    return render_template('student.html', student_data=students)

@student_bp.route('/students/add', methods=['POST'])
def add_student():
    if request.method == 'POST':
        # Get data from the form submission
        student_id = request.POST.get('studentID')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')

        try:
            # Call the addStudent method from the StudentManager class
            student.addStudent(student_id, first_name, last_name, gender, year, course)
            return redirect(url_for('student.list_students'))
        except Exception as e:
            # Handle any exceptions that might occur during the addition of the student
            print(f"Error adding student: {e}")
            return render_template('error.html', error_message='Error adding student')
    
    return redirect('/students')