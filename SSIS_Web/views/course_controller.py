from flask import Blueprint, render_template
from SSIS_Web.models.course_model import get_course_data

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses')
def list_course():
    courses = get_course_data()
    return render_template('course.html', data=courses)
