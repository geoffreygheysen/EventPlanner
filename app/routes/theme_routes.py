from app import app
from app.controllers.theme_controller import ThemeController

from flask_jwt_extended import jwt_required
from app.tools.role_required import role_required

# Define the routes for theme-related operations

# get all themes
@app.route('/themes', methods=['GET'])
def get_all_themes():
    return ThemeController.get_all_themes()

# create a new theme
@jwt_required()
@role_required("admin")
@app.route('/theme/create', methods=['POST'])
def create_theme():
    return ThemeController.create_theme()

# update a theme by id
@jwt_required()
@role_required("admin")
@app.route('/theme/update/<int:id>', methods=['PUT'])
def update_theme(id):
    return ThemeController.update_theme(id)

# delete a theme by id
@jwt_required()
@role_required("admin")
@app.route('/theme/delete/<int:id>', methods=['DELETE'])
def delete_theme(id):
    return ThemeController.delete_theme_by_id(id)