from flask import Blueprint

student_bp = Blueprint('student', __name__)
course_bp = Blueprint('course', __name__)
college_bp = Blueprint('college', __name__)


#from . import controller