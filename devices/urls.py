from django.urls import re_path
from . import views

app_name = 'devices'

urlpatterns = [
    re_path(r'^toggle/$', views.toggle, name='toggle'),
    re_path(r'^turnon/$', views.turnOn, name='turnon'),
    re_path(r'^turnoff/$', views.turnOff, name='turnoff')
    ]