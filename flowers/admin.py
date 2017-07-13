from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin

# Register your models here.
from django.db import models

from flowers.models import Flower, Scene, Design, Order


class SceneAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }


admin.site.register(Flower)
admin.site.register(Scene, SceneAdmin)
admin.site.register(Design, DesignAdmin)
admin.site.register(Order)
