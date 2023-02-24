import time

import jwt
from flask import request
from flask_restx import Resource, Namespace

from constants import JWT_SECRET_KEY, JWT_TOKEN_ALGORITHM
from container import user_service
from utils import generate_jwt, get_hash

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    # Аутентификация по логину/паролю и выдача токенов
    def post(self):
        """
        Аутентификация по логину и паролю.
        В параметрах запроса ожидаем:
            username: str
            password: str
        """
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)
        if None in [username, password]:
            return {"error": "Неверные учётные данные"}, 400

        user = user_service.get_by_name(username)

        # Проверяем существует ли вообще такой пользователь
        if user is None:
            return {"error": "Неверные учётные данные"}, 401
        # И, верный ли введён пароль
        if user.password != get_hash(password):
            return {"error": "Неверные учётные данные"}, 401

        user_data = {"username": user.username,
                     "role": user.role,
                     }

        tokens = generate_jwt(user_data)
        return tokens, 201

    # Аутентификация по рефреш токену и обновление access токена
    def put(self):
        """
        В функции обновляем токены доступа по рефреш токену.
        В данных запроса ожидаем увидеть:
            username: str
            refresh_token: str
        """

        user_refresh_token_data = request.json()
        refresh_token = user_refresh_token_data.get('refresh_token')

        if refresh_token is None:
            return {"error": "Неверные учётные данные"}, 400

        try:
            decoded_token = jwt.decode(refresh_token, JWT_SECRET_KEY, algorithms=[JWT_TOKEN_ALGORITHM])
        except Exception as e:
            return {"error": "Неверные учётные данные"}, 401

        # Если имя в данных токена не соответствует имени в запросе
        if decoded_token.get('username') != user_refresh_token_data.get('username'):
            return {"error": "Неверные учётные данные"}, 401

        user_data = {'user': decoded_token.get('username'),
                     'role': decoded_token.get('role'),
                     }

        new_tokens = generate_jwt(user_data)
        return new_tokens, 201
