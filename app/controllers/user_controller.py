from flask import jsonify, request
from flask_restful import Resource
from marshmallow import ValidationError

from app.models.db import User
from app.models.dto.user.user_schema import UserSchema
from app.models.dto.user.user_update_schema import UserUpdateSchema
from app.tools.session_scope import SessionScope


class UserController(Resource):
    # get all users
    def get_all_users():
        with SessionScope() as session:
            users = session.query(User).all()
            user_schema = UserSchema(many=True)
            user_serialized = user_schema.dump(users)
        return jsonify(user_serialized), 200
        
    # get user by id
    def get_user_by_id(id):
        with SessionScope() as session:
            user = session.query(User).filter_by(id=id).first()
            if not user:
                return jsonify({"message": "User not found"}), 404
            
            user_schema = UserSchema(many=False)
            user_serialized = user_schema.dump(user)
        return jsonify(user_serialized), 200
    
    # update user information
    def update_user(id, user_data):
        user_schema = UserUpdateSchema()
        try:
            user_data = user_schema.load(request.json, partial=True)
        except ValidationError as e:
            return jsonify({"message": str(e)}), 400
        
        with SessionScope() as session:
            user = session.query(User).get(id)
            if not user:
                return jsonify({"message": "User not found"}), 404
            
            for key, value in user_data.items():
                setattr(user, key, value)
            
            session.commit()
            user_serialized = user_schema.dump(user)
        return jsonify(user_serialized), 200
    
    # delete user by id
    def delete_user_by_id(id):
        with SessionScope() as session:
            user = session.query(User).get(id)
            if user:
                session.delete(user)
                session.commit()
                return jsonify({"message": "User deleted successfully"}), 200
            else:
                return jsonify({"message": "User not found"}), 404


