from django.contrib import admin

# Register your models here.
from flowers.models import Flower, Scene, Design


class SceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Flower)
admin.site.register(Scene,SceneAdmin)
admin.site.register(Design)
