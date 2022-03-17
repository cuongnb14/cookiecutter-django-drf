from rest_framework import status
from rest_framework.exceptions import APIException


class UserAlreadyVerified(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'User already verified'
    default_code = 'params_error'