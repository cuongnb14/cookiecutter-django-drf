import logging

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger('apps')


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    logger.exception(exc)

    # Add default error code to the response.
    if response is not None:
        data = {
            "code": exc.default_code,
            "detail": exc.detail,
        }
        response.data = data
    else:
        data = {
            "code": "unexpected_error",
            "detail": "Oops! Something went wrong",
        }
        if settings.DEBUG:
            data["debug_message"] = str(exc)
        response = Response(data, status=500)

    return response
