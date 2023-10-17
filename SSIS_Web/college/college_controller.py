from flask import Blueprint, render_template
from SSIS_Web.college.college_model import get_college_data

college_bp = Blueprint('college', __name__)

@college_bp.route('/colleges')
def list_college():
    colleges = get_college_data()
    return render_template('college.html', data=colleges)
