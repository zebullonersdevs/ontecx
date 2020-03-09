from django.http import JsonResponse

from rest_framework import status

def server_error(request, *args, **kwargs):
    """
    Generic 500 error handler.
    """
    data = {
        'error': 'A server error occured'
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def not_found_request(request, exception, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {
        'error': 'The requested endpoint resource does not exist'
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)
