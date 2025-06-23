from datetime import timedelta
from flask_jwt_extended import create_access_token

def generate_jwt_token(user, claims=None, expires_in_hours=1):
    token_claims = {
        'email' : user.email,
        'role': user.role
    }

    if claims:
        token_claims.update(claims)

    access_token = create_access_token(
        identity=user.id,
        expires_delta=timedelta(hours=expires_in_hours),
        additional_claims=token_claims
    )

    # Optionally, you can log the token generation for debugging purposes
    print(f"Generated JWT token for user {user.email} with ID {user.id}")

    return access_token
