from rest_framework import status
from rest_framework.response import Response


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
