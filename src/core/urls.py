from django.contrib import admin
from django.urls import path

#from .views import upload
from .views import Home, upload

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('upload/',upload, name="upload"),
]
