from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.conf import settings

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Add default error code to the response.
    if response is not None:
        response.data["code"] = exc.default_code
    else:
        data = {
            "detail": "Ops! Something went wrong",
        }
        if settings.DEBUG:
            data["debug_message"] = str(exc)
        response = Response({
            "detail": "Ops! Something went wrong",
            "debug_message": str(exc)
        }, status=500)

    return response
