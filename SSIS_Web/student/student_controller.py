from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from SSIS_Web.student.student_model import StudentManager
from flask_mysql_connector import MySQL
from SSIS_Web.student.forms import StudentForm

mysql = MySQL()
student_bp = Blueprint('student', __name__)
StudentManager.init_db(mysql)  

@student_bp.route('/')
def home():
    return render_template('home.html')


@student_bp.route('/students', methods=['GET', 'POST'])
def list_students():
    form = StudentForm()
    courses = StudentManager.get_courses()
    
    if request.method == 'POST':
        search_field = request.form.get('searchField')  
        search_query = request.form.get('searchInput')  
        # Perform search based on user input
        student_data = StudentManager.search_students(field=search_field, query=search_query)
    else:
        # If no search input, retrieve all students
        student_data = StudentManager.get_student_data()

    return render_template('student.html', student_data=student_data, form=form, courses=courses)

@student_bp.route('/students/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Get data from the form submission
        student_id = request.form.get('studentID')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        course_code = request.form.get('course')
        year = request.form.get('year')
        gender = request.form.get('gender')
        
        if StudentManager.add_student(student_id, first_name, last_name, course_code, gender, year) == Exception:
            flash('Error adding student, duplicate ID. Please try again.', 'error')
        else:
            flash(f'Student {student_id} added successfully!', 'success')
        return redirect(url_for('student.list_students'))
    return render_template('student.html', form=form)


@student_bp.route('/students/delete/<string:student_id>', methods=['POST'])
def delete_student(student_id):
    try:
        StudentManager.delete_student(student_id)
        flash(f'Student {student_id} deleted successfully!', 'success')
        return redirect(url_for('student.list_students'))
    except Exception as e:
        print(f"Error deleting student: {e}")
        flash('Error deleting student. Please try again.', 'error')
        
@student_bp.route('/students/edit/', methods=['POST'])
def edit_student_data():
    form = StudentForm() 
    #form_data = request.form
    #print("Form Data received:", form_data)
    gender = request.form.get('gender')
    print("gender:", gender) 
    updated_data = {
        'new_id': request.form.get('studentID'),
        'firstname': request.form.get('firstName'),
        'lastname': request.form.get('lastName'),
        'course': request.form.get('course'),
        'year': request.form.get('year'),
        'gender': request.form.get('gender'),
        'old_id': request.form.get('old_id')
    }
    if StudentManager.update_student(**updated_data) == Exception:
         flash('Error saving student, duplicate ID. Please try again.', 'error')
    else:
        flash(f'Student {updated_data["new_id"]} updated successfully!', 'success')
    return redirect(url_for('student.list_students'))