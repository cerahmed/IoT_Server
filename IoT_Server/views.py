from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from devices.models import Devices
import datetime
import pytz

# Create your views here.
@login_required(login_url='accounts:login')
def index(request):
    devices = Devices.objects.all()
    
    # used to make today and yesterday datetime objects offset-aware in order
    # to compare them with lastTime of device inside html template
    
    utc = pytz.UTC
    
    today = datetime.datetime.now().replace(hour=0, minute=0,
                                            second=0, microsecond=0)
    today = utc.localize(today)
    yesterday = today - datetime.timedelta(days=1)
    
    
    return render(request, 'index.html', {'devices': devices, 'today': today, 'yesterday': yesterday})