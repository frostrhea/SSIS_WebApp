from flask import Blueprint, render_template
from SSIS_Web.models.student_model import get_student_data

student_bp = Blueprint('student', __name__)

@student_bp.route('/students')
def list_students():
    students = get_student_data()
    return render_template('student.html', data=students)
