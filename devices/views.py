from django.shortcuts import render
from django.http.response import HttpResponse
from devices.zeroconf.registerZeroconfService import registerService, unregisterService

# Create your views here.
def toggle(request):
    return render(request, 'devices/toggleAvahi.html')
    
def turnOn(request):
    print("turned on")
    registerService()
    return HttpResponse("ok")

def turnOff(request):
    print("turned off")
    unregisterService()
    return HttpResponse("ok")