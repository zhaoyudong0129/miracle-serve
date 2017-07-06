import six
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from django.utils.log import CallbackFilter
from rest_framework import status, exceptions
from rest_framework.compat import set_rollback
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _

import logging

logger = logging.getLogger(__name__)


class ExceptionLoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if response.status_code == 404:
            logger.info('Not Found ' + request.path)

        return response

    def process_exception(self, request, exception):
        # log unhandled exception
        logger.exception('Unhandled exception request for ' + request.path)


def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    # logger.exception(exc)

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = {'error': exc.detail}
        else:
            data = {'error': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {'error': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'error': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    return None


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = response.status_code

    return response


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


class InternalError(APIException):
    status_code = 500
    default_detail = 'Server internal error.'
    default_code = 'server_internal_error'


class Duplicate(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _('Already exists.')
    default_code = 'duplicate'