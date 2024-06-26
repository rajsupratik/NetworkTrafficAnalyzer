from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def capture_packets(interface, packet_count):
    packets = sniff(iface=interface, count=packet_count)
    return packets

def parse_packets(packets):
    packet_list = []
    for packet in packets:
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            proto = packet[IP].proto
            length = packet[IP].len
            
            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                proto_name = 'TCP'
            elif UDP in packet:
                sport = packet[UDP].sport
                dport = packet[UDP].dport
                proto_name = 'UDP'
            else:
                sport = None
                dport = None
                proto_name = 'Other'
            
            packet_list.append([ip_src, ip_dst, proto_name, length, sport, dport])
    
    df = pd.DataFrame(packet_list, columns=['Source IP', 'Destination IP', 'Protocol', 'Length', 'Source Port', 'Destination Port'])
    return df

def visualize_data(df):
    # Plotting packet counts by protocol
    sns.countplot(x='Protocol', data=df)
    plt.title('Packet Counts by Protocol')
    plt.show()
    
    # Plotting packet lengths
    sns.histplot(df['Length'], bins=30)
    plt.title('Packet Length Distribution')
    plt.show()

def main(interface='Ethernet', packet_count=100):
    packets = capture_packets(interface, packet_count)
    df = parse_packets(packets)
    visualize_data(df)

if __name__ == "__main__":
    main()
