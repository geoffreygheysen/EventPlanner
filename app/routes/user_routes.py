from flask import request
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

# update user information
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    return UserController.update_user(id, user_data)

# delete user by id
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user_by_id(id):
    return UserController.delete_user_by_id(id)
