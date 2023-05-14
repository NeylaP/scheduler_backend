from apps.general.serializers import UsersSerializerList


def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'usuario': UsersSerializerList(user, context={'request': request}).data
    }