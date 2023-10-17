from flask import Blueprint, render_template, request, redirect, url_for
from SSIS_Web.student.student_model import StudentManager
from flask_mysql_connector import MySQL
from SSIS_Web.student.forms import StudentForm

mysql = MySQL()
student_bp = Blueprint('student', __name__)
StudentManager.init_db(mysql)  # Initialize the database connection

@student_bp.route('/students', methods=['GET'])
def list_students():
    form = StudentForm()
    students = StudentManager.get_student_data()  # Fetch data from the database
    return render_template('student.html', student_data=students, form=form)

@student_bp.route('/students/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Get data from the form submission
        student_id = request.form.get('studentID')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        course = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')

        try:
            # Call the add_student class method from the StudentManager class
            StudentManager.add_student(student_id, first_name, last_name, course, gender, year)
            return redirect(url_for('student.list_students'))
        except Exception as e:
            print(f"Error adding student: {e}")

    # Pass the form instance to the template context
    return render_template('add_student.html', form=form)

@student_bp.route('/students/delete/<string:student_id>', methods=['POST'])
def delete_student(student_id):
    try:
        StudentManager.delete_student(student_id)
        return redirect(url_for('student.list_students'))
    except Exception as e:
        print(f"Error deleting student: {e}")
