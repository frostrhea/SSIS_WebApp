from flask import Flask
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect
from SSIS_Web.models.student_model import StudentManager


mysql = MySQL()
bootstrap = Bootstrap()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)
    
    student_manager = StudentManager(mysql)
    
    from .views.student_controller import student_bp as student_blueprint
    app.register_blueprint(student_blueprint)

    from .views.course_controller import course_bp as course_blueprint
    app.register_blueprint(course_blueprint)

    from .views.college_controller import college_bp as college_blueprint
    app.register_blueprint(college_blueprint)
    
    return app
