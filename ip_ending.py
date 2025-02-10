import socket
import fcntl
import struct
import sys

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except Exception as e:
        s.close()
        print(f"Could not get IP for interface {ifname}, error: {e}")
        return None

def get_last_number():
    # Get the IP address for eth0
    ip_address_eth0 = get_interface_ip('eth0')

    if ip_address_eth0:
        # Extract the last number of the IP address
        last_number_eth0 = ip_address_eth0.split('.')[-1]
    else:
        sys.exit(1)

    return last_number_eth0
