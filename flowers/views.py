from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status, exceptions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from flowers.models import Scene
from flowers.serializers import SceneSerializer


def home(request):
    return HttpResponse("Hello, You're at ms-miracle.com.")


class SceneViewSet(viewsets.ModelViewSet):
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()

    # permission_classes = (permissions.IsAuthenticated,)

    @list_route(methods=['GET'])
    def follow(self, request):
        result = {
            'success': True
        }

        d = Scene.objects.all()[2]

        return Response(result, status.HTTP_200_OK)
