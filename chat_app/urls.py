from django.contrib import admin
from django.urls import path, include
from main_app.views import index

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", include('login.urls')),
    # path("chat/", include('main_app.urls')),
]
