from rest_framework import serializers

from flowers.models import Scene, Design


class DesignSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Design

        fields = ('title', 'detail', 'image')


class SceneSerializer(serializers.ModelSerializer):
    designs = DesignSerializer(many=True, read_only=True)

    class Meta(object):
        model = Scene

        fields = ('title', 'detail', 'image', 'designs')
