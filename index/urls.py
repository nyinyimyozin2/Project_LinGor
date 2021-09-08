from django.urls import path
from . import views
from django.conf.urls import handler404
from django.views import defaults
from django.core.handlers import exception
urlpatterns = [
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
]



