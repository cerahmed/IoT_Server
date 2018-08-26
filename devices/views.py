from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def registerClient(request):
    print("Registering client")
    if request.method == 'GET':
        print("***GET REQUEST***")
    elif request.method == 'POST':
        print("***POST REQUEST***")
    else:
        print("***UNKOWN REQUEST***")
    
    return HttpResponse("OK")