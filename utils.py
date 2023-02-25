import hashlib
import re
import time
import jwt
from flask import request, abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET_KEY, JWT_TOKEN_ALGORITHM, PWD_ALGORITHM


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        PWD_ALGORITHM,
        password.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")


def generate_jwt(user_data: dict) -> dict[str:str]:
    time_utc = int(time.time())
    time_30min = time_utc + 1800            # Добавляем 30 минут для текущего времени
    time_100d = time_utc + 3600 * 24 * 100  # Добавляем 100 дней для текущего времени

    user_data['exp'] = time_30min
    access_token = jwt.encode(user_data, JWT_SECRET_KEY, algorithm=JWT_TOKEN_ALGORITHM)
    user_data['exp'] = time_100d
    refresh_token = jwt.encode(user_data, JWT_SECRET_KEY, algorithm=JWT_TOKEN_ALGORITHM)

    return {'access_token': access_token, 'refresh_token': refresh_token}


def check_auth(headers: dict) -> dict:
    if 'Authorization' not in headers:
        abort(401)

    token = headers['Authorization'].split('Bearer ')[-1]
    try:
        user_auth_data = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_TOKEN_ALGORITHM])
        return user_auth_data
    except Exception as e:
        abort(401)


def auth_required(func):
    def wrapper(*args, **kwargs):
        check_auth(request.headers)

        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        user_auth_data = check_auth(request.headers)

        if user_auth_data.get('role') != 'admin':
            abort(403)

        return func(*args, **kwargs)
    return wrapper


def is_email_valid(email: str) -> bool:
    """ проверяет наличие собачки и точки"""
    is_email = re.findall("^([a-z0-9_.]+@[a-z0-9_.]+\.[a-zA-Z]{2,6})$", email)
    return bool(is_email)
