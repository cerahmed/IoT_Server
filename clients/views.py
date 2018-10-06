from django.shortcuts import render
from django.http.response import HttpResponse
from clients.zeroconf.registerZeroconfService import registerService, unregisterService

# Create your views here.
def toggle(request):
    return render(request, 'clients/toggleAvahi.html')
    
def turnOn(request):
    print("turned on")
    registerService()
    return HttpResponse("ok")

def turnOff(request):
    print("turned off")
    unregisterService()
    return HttpResponse("ok")