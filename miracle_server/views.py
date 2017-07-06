from django.http import Http404
from rest_framework.decorators import api_view

from miracle_server.exceptions import InternalError


@api_view()
def url_not_found(request, exception):
    raise Http404


@api_view()
def server_error(request):
    raise InternalError
