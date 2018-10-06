import socket
from zeroconf import ServiceInfo, Zeroconf

zeroconf = None
info = None

def myLocalIP():
    
    # retrieve hostname from socket
    hostname = socket.gethostname()
    
    # find local ipaddress to for other devices to connect to
    # and to use it in advertising zeroconf service
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IPAddr = s.getsockname()[0]
    
    # for debugging purposes
    print("Hostname: {}".format(hostname))
    print("IP Address: {}".format(IPAddr))
    
    # close socket connection
    s.close()
    
    # return both hostname and local IP Address
    return hostname, IPAddr

def registerService(): #TODO: when turning on twice .. it crashes
    global zeroconf, info
    
    # if zeroconf is not initialized, initialize it.
    if not zeroconf:
        zeroconf = Zeroconf()
    
    serverPrefix = '_IoT-server' # must be '_something'
    serverSuffix = '._tcp.local.' # must be '_valid.local.'
    serverType = serverPrefix + serverSuffix
    
    hostname, ipaddress = myLocalIP()
    
    serverName = hostname + '_.' + serverType
    port = 8000
    desc = {'path': '/~'}
    
    server = hostname + '.local.'
    
    info = ServiceInfo(serverType,
                       serverName,
                       socket.inet_aton(ipaddress), port, 0, 0,
                       desc, server)
    
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)

def unregisterService():
        
    if zeroconf:
        zeroconf.unregister_service(info)

