from django.urls import re_path
from . import views

app_name = 'devices'

urlpatterns = [
    re_path(r'^register/$', views.registerClient, name='registerClient'),
    ]