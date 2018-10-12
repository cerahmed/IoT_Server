from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from .models import Devices
import time
import datetime
# import RPi.GPIO as gpio 

# Create your views here.
def open(request, deviceID):
    device = Devices.objects.get(id = deviceID)
    try:
        triggerRelay(device.pin, device.pinTime)
        updateLastTime(device)
    except:
        return HttpResponseNotFound()
    
    return HttpResponse()

def triggerRelay(pin, timeout):
    print("Triggering pin " + pin + " for " + timeout + " seconds...")
    time.sleep(int(timeout))
    print("done.")
    
def updateLastTime(device):
    device.lastTime = datetime.datetime.time(datetime.datetime.now())
    device.save()