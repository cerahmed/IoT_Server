from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from .models import Devices
import time
import datetime

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
    pin = int(pin)
    timeout = int(timeout)
    
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.HIGH)
    
    print("Triggering pin " + str(pin) + " for " + timeout + " seconds...")
    
    time.sleep(timeout)
    gpio.output(pin, gpio.LOW)
    print("done.")
    
def updateLastTime(device):
    device.lastTime = datetime.datetime.now()
    device.save()