from flask import request
from app import app
from app.controllers.user_controller import UserController

from flask_jwt_extended import jwt_required
from app.tools.role_required import role_required

# Define the routes for user-related operations

# get all users
@app.route('/users', methods=['GET'])
@role_required("admin")
@jwt_required()
def get_all_users():
    return UserController.get_all_users()

# get user by id
@app.route('/user/<int:id>', methods=['GET'])
@jwt_required()
@role_required("admin")
def get_user_by_id(id):
    return UserController.get_user_by_id(id)

# update user information
@app.route('/user/<int:id>', methods=['PUT'])
@jwt_required()
@role_required("user", "admin", "participant")
def update_user(id):
    user_data = request.get_json()
    return UserController.update_user(id, user_data)

# delete user by id
@app.route('/user/<int:id>', methods=['DELETE'])
@jwt_required()
@role_required("admin")
def delete_user_by_id(id):
    return UserController.delete_user_by_id(id)
