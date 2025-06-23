from flask import request
from app import app
from app.controllers.theme_controller import ThemeController

# Theme routes for managing themes in the application

# get all themes
@app.route('/themes', methods=['GET'])
def get_all_themes():
    return ThemeController.get_all_themes()

# get theme by id
@app.route('/theme/<int:id>', methods=['GET'])
def get_theme_by_id(id):
    return ThemeController.get_theme_by_id(id)

# create a new theme
@app.route('/theme/create', methods=['POST'])
def create_theme():
    return ThemeController.create_theme()

# update theme information
@app.route('/theme/update/<int:id>', methods=['PUT'])
def update_theme(id):
    return ThemeController.update_theme(id)

# delete theme
@app.route('/theme/delete/<int:id>', methods=['DELETE'])
def delete_theme(id):
    return ThemeController.delete_theme_by_id(id)