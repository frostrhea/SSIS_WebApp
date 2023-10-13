from flask import Blueprint, render_template, jsonify, request
from SSIS_Web.models.student_model import get_student_data

student_bp = Blueprint('student', __name__)

@student_bp.route('/students', methods=['GET'])
def list_students():
    if request.headers.get('accept') == 'application/json':
        students = get_student_data()
        return jsonify(students)
    else:
        return render_template('student.html')
    
