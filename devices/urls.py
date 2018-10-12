from django.urls import path
from . import views

app_name = 'devices'

urlpatterns = [
    path('open/<int:deviceID>', views.open, name='open'),
    ]