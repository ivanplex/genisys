from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler


class ErrorResponse:
    @staticmethod
    def build_serializer_error(serializer, status):
        return Response({"status": "error", "errors": serializer.errors},
                        status=status)

    @staticmethod
    def build_text_error(text, status):
        return Response({"status": "error", "errors": text}, status=status)


class Utils(object):
    @staticmethod
    def error_response_400(error):
        return Response({"error": str(error)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def message_response_200(error):
        return Response({"message": str(error)}, status=status.HTTP_200_OK)


def exception_handler(exc, context):
    """Handle Django ValidationError as an accepted exception
    Must be set in settings:
    >>> REST_FRAMEWORK = {
    ...     # ...
    ...     'EXCEPTION_HANDLER': 'mtp.apps.common.drf.exception_handler',
    ...     # ...
    ... }
    For the parameters, see ``exception_handler``
    """

    if isinstance(exc, DjangoValidationError):
        if hasattr(exc, 'message_dict'):
            exc = DRFValidationError(detail=exc.message_dict)
        else:
            exc = DRFValidationError(detail=exc.message)

    return drf_exception_handler(exc, context)

