from django.shortcuts import render
from django.http.response import HttpResponse
from devices.models import Devices

# Create your views here.
def index(request):
    devices = Devices.objects.all()
    return render(request, 'index.html', {'devices': devices})