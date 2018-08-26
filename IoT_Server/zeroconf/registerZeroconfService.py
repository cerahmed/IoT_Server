import socket
from zeroconf import ServiceInfo, Zeroconf

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

def registerService():
    
    desc = {'path': '/~'}
    hostname, ipaddress = myLocalIP()
    
    info = ServiceInfo("_IoT-server._tcp.local.",
                       hostname + "._IoT-server._tcp.local.",
                       socket.inet_aton(ipaddress), 8000, 0, 0,
                       desc, hostname + ".local.")
    
    zeroconf = Zeroconf()
    
    print("Registration of a service, press Ctrl-C to exit...")
    zeroconf.register_service(info)