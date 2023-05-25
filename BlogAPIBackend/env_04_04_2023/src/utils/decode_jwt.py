from flask import request, current_app
import jwt


def decode_jwt():
    jwtr = request.headers.get("Authorization")
    auth_token = jwtr.split(" ")[1]
    jwt_payload = jwt.decode(auth_token, current_app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    return jwt_payload
