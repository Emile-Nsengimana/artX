import jwt
import os

from datetime import datetime, timedelta
from functools import wraps
from graphql import GraphQLError
from flask import request

key = os.getenv('SECRET_KEY')


class Authentication:

    # a method to produce a token from user payload
    # params:
    #    payload: dict
    # returns:
    #    token: string
    def generate_token(payload):
        try:
            payload['exp'] = datetime.utcnow() + timedelta(seconds=900)
            token = jwt.encode(payload, key, 'HS256')

            return token

        except Exception as error:
            return error

    # a decorator function to verify user token
    def verify_token(func):

        @wraps(func)
        def verify(self, info, **kwargs):
            try:
                token = request.headers['Authorization'].split(' ')[1]
                _token = jwt.decode(token, key, 'HS256')
                if _token:
                    return func(self, info, **kwargs)
                raise GraphQLError('invalid token')

            except Exception as ex:
                raise GraphQLError(ex)

        return verify
