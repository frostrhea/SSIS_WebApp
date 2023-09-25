from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'frost'
    
    @app.route('/')
    def home():
        return "ssis test!"
    
    return app
