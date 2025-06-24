from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db import Theme
from app.models.dto.theme.theme_schema import ThemeSchema
from app.models.dto.theme.theme_update_schema import ThemeUpdateSchema
from app.tools.session_scope import SessionScope

# ThemeController handles operations related to themes in the application.

class ThemeController(Resource):
    # get all themes
    def get_all_themes():
        with SessionScope() as session:
            themes = session.query(Theme).all()
            theme_schema = ThemeSchema(many=True)
            theme_serialized = theme_schema.dump(themes)
        return jsonify(theme_serialized), 200
    
    # create a new theme
    def create_theme():
        theme_schema = ThemeSchema()
        errors = theme_schema.validate(request.json)
        if errors:
            return jsonify({"message": str(errors)}), 400
        theme_data = theme_schema.load(request.json)
        with SessionScope() as session:
            new_theme = Theme(**theme_data)
            session.add(new_theme)
            session.commit()
            theme_serialized = theme_schema.dump(new_theme)
        return jsonify(theme_serialized), 201
    
    # update theme information
    def update_theme(id):
        theme_schema = ThemeUpdateSchema()
        try:
            theme_data = theme_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 400
        
        with SessionScope() as session:
            theme = session.query(Theme).get(id)
            if not theme:
                return jsonify({"message": "Theme not found"}), 404
            
            for key, value in theme_data.items():
                setattr(theme, key, value)
            
            session.commit()
            theme_serialized = theme_schema.dump(theme)
        return jsonify(theme_serialized), 200
    
    # delete theme by id
    def delete_theme_by_id(id):
        with SessionScope() as session:
            theme = session.query(Theme).get(id)
            if theme:
                session.delete(theme)
                session.commit()
                return jsonify({"message": "Theme deleted successfully"}), 200
            else:
                return jsonify({"message": "Theme not found"}), 404
