"""
WSGI config for IoT_Server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
# import time

from django.core.wsgi import get_wsgi_application
# from clients.zeroconf.registerZeroconfService import registerService, unregisterService

def onStartUp():
    '''
    By me.
    This function is meant to run on each startup of the server.
    '''
    
#     registerService() # for debugging purposes
#     time.sleep(6)
#     unregisterService()
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IoT_Server.settings')
onStartUp() # This script will run when the server first runs

application = get_wsgi_application()