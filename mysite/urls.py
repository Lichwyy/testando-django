from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("questoes/", include("polls.urls")),
    path("admin/", admin.site.urls),
]