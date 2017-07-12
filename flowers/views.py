from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status, exceptions
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from flowers.models import Scene, Design
from flowers.serializers import SceneSerializer, DesignSerializer


def home(request):
    return HttpResponse("Hello, You're at ms-miracle.com.")


class SceneViewSet(viewsets.ModelViewSet):
    serializer_class = SceneSerializer
    queryset = Scene.objects.all()


class DesignViewSet(viewsets.ModelViewSet):
    serializer_class = DesignSerializer
    queryset = Design.objects.all()
