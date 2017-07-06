from rest_framework import serializers

from flowers.models import Scene


class SceneSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Scene

        fields = ('title', 'detail', 'image')
