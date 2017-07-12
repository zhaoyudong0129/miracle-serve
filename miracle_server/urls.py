"""miracle_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers

from flowers.views import SceneViewSet, DesignViewSet
from miracle_server import settings

router = routers.DefaultRouter()
router.register('scenes', SceneViewSet)
router.register('designs', DesignViewSet)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^weixin/', include('weixin.urls', namespace='weixin')),
                  url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                  url(r'^api/', include(router.urls)),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'miracle_server.views.url_not_found'
handler500 = 'miracle_server.views.server_error'
