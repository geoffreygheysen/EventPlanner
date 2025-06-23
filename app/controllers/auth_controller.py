from flask import jsonify, request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.db.user_model import User
from app.models.dto.auth.auth_schema import UserLoginSchema, UserRegisterSchema
from app.tools.jwt_manager import generate_jwt_token
from app.tools.session_scope import SessionScope


class AuthController(Resource):
    # User login
    def login():
        user_schema = UserLoginSchema(only=('email', 'password'))
        errors = user_schema.validate(request.json)

        if errors:
            return {"errors": errors}, 400

        email = request.json.get('email')
        password = request.json.get('password')

        with SessionScope() as session:
            user = session.query(User).filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                return {"message": "Invalid email or password"}, 401
            else:
                roles = {"admin": 'admin', "user": 'user', "participant": 'participant'}
                access_token = generate_jwt_token(user, claims={"roles": roles})
                return jsonify(access_token=access_token), 200

    # User registration
    def register():
        user_schema = UserRegisterSchema()
        errors = user_schema.validate(request.json)

        if errors:
            return jsonify(errors), 400

        email = request.json.get('email')
        password = request.json.get('password')

        password_hash = generate_password_hash(password)

        with SessionScope() as session:
            user = session.query(User).filter_by(email=email).first()
            if user:
                return jsonify({"message": "User already exists"}), 409

            new_user = User(
                email=email,
                password=password_hash
            )
            session.add(new_user)
        return {"message": "User registered successfully"}, 201
