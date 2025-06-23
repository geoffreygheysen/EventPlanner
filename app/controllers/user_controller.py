from flask import jsonify
from flask_restful import Resource

from app.models.db import User
from app.models.dto.user.user_schema import UserSchema
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
            
