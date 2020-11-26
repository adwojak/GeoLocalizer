from rest_framework.views import exception_handler as base_exception_handler
from geolocalizer.libs.response import ErrorResponse


class BadAddressError(Exception):
    pass


class IpstackDataNotFoundError(Exception):
    pass


def exception_handler(exception, context):
    response = base_exception_handler(exception, context)
    exception_message = exception.args[0]
    if exception_message:
        return ErrorResponse(exception_message)
    return response
