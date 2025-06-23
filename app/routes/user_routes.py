from app import app
from app.controllers.user_controller import UserController

# Define the user routes

# get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

# get user by id
@app.route('/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    return UserController.get_user_by_id(id)
