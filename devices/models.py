from django.db import models

# Create your models here.
class RegisteredDevices(models.Model):
    #id field is automatically set by django
    dateAdded = models.DateTimeField(auto_now_add=True)
    hostname = models.CharField(max_length=100, null=False)
    ipaddress = models.CharField(max_length=20, null=False)
    port = models.CharField(max_length=10, null=False, default='80')
    publickey = models.CharField(max_length=1000, null=False)
    # add type field
    # add nickname field
    
    def __str__(self):
        return self.hostname + ' - ' + self.ipaddress + ':' + self.port
    