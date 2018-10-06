from django.urls import path

app_name = 'clients'

urlpatterns = [
    path('toggle/', views.toggle, name='toggle'),
    path('turnon/', views.turnOn, name='turnon'),
    path('turnoff/', views.turnOff, name='turnoff')
    ]