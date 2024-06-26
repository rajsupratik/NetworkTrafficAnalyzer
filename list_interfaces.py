from scapy.all import get_if_list

def list_interfaces():
    interfaces = get_if_list()
    for iface in interfaces:
        print(iface)

if __name__ == "__main__":
    list_interfaces()
