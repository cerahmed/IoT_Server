from django.contrib import admin
from .models import Devices

# Register your models here.

class DevicesAdmin(admin.ModelAdmin):
#     fields = ('name', 'display_name', 'type', 'pin', 'pinTime')
    exclude = ('lastTime',)

admin.site.register(Devices, DevicesAdmin)