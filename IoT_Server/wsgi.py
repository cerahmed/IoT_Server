"""
WSGI config for IoT_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .zeroconf.registerZeroconfService import registerService


def onStartUp():
    '''
    This function is meant to run on each startup of the server.
    1) register zeroconf-server service for client to reach server.
    '''
    
    registerService() # advertises IoT-server zeroconf service

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IoT_Server.settings')
onStartUp() # This script will run when the server first runs

application = get_wsgi_application()