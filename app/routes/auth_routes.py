from app import app
from app.controllers.auth_controller import AuthController

@app.route('/auth/login', methods=['POST'])
def login():
    return AuthController.login()

@app.route('/auth/register', methods=['POST'])
def register():
    return AuthController.register()