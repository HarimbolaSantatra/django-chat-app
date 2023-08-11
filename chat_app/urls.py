from django.contrib import admin
from django.urls import path, include
from main_app.views import index

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include('login.urls')),
    path("chat/", include('main_app.urls')),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

