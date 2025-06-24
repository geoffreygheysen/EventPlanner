from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def role_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()  # ✅ On accède aux claims du token
            if claims.get('role') not in allowed_roles:
                return jsonify({"message": "Access forbidden: Insufficient permissions"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator




