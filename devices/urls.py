from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('toggle/', views.toggle, name='toggle'),
    path('turnon/', views.turnOn, name='turnon'),
    path('turnoff/', views.turnOff, name='turnoff')
    ]