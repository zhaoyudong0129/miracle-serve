from django.contrib import admin

# Register your models here.
from flowers.models import Flower, Scene, Design

admin.site.register(Flower)
admin.site.register(Scene)
admin.site.register(Design)
