from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('student.html')

@views.route('/courses')
def course():
    return render_template('course.html')

@views.route('/colleges')
def college():
    return render_template('college.html')