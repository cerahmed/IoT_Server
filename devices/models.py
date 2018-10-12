from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Devices(models.Model):
    '''
    A model table that holds information for connected relays, sensors, etc.
    '''
    class Meta: # a class to fix plural name that shows in the admin site
        verbose_name_plural = 'Devices'
    
    # tuple for type choices
    typeChoices = (
        ('s', 'sensor'),
        ('r', 'relay'),
        )
    
    # -- id field automatically created by django
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=2, unique=True)
    type = models.CharField(max_length=1, choices=typeChoices)
    lastTime = models.TimeField(null=True, default=None)
    pin = models.CharField(max_length=2, unique=True, validators=[RegexValidator(r'^\d{1,10}$')])
    pinTime = models.CharField(max_length = 1, validators=[RegexValidator(r'^\d{1,10}$')])
    
    readonly_fields = ["lastTime"]
    
    def __str__(self):
        return self.name + ' - ' + [element for element in self.typeChoices if element[0] == self.type][0][1]