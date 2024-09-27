Network Packet Capture and Analysis
This Python project allows you to capture and analyze network packets using the Scapy library. It captures network traffic, extracts useful information (such as IP addresses, protocol type, and packet length), and visualizes the results using Seaborn and Matplotlib.

Features
Packet Capture: Sniffs packets from the specified network interface using Scapy.
Packet Parsing: Extracts source and destination IP addresses, protocol type, packet length, and ports (TCP/UDP).
Data Visualization: Visualizes the packet data, including protocol distribution and packet length distribution, using Seaborn.
Requirements
Ensure you have the following dependencies installed before running the project:

Python 3.x
Scapy
Pandas
Matplotlib
Seaborn
You can install the required packages using pip:

bash
Copy code
pip install scapy pandas matplotlib seaborn
Usage
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/packet-capture-analysis.git
cd packet-capture-analysis
Run the main script:

bash
Copy code
python packet_capture.py
By default, the script captures 100 packets from the 'Ethernet' interface. You can modify the interface and packet_count in the main function:

python
Copy code
def main(interface='Ethernet', packet_count=100):
    ...
Example Usage:
To capture packets from a different interface, change the interface name:

python
Copy code
main(interface='wlan0', packet_count=200)
Functions
capture_packets(interface, packet_count)
Captures network packets from the specified interface.

Parameters:
interface (str): Name of the network interface (e.g., Ethernet, wlan0).
packet_count (int): Number of packets to capture.
Returns:
packets: A list of captured packets.
parse_packets(packets)
Parses captured packets and creates a DataFrame containing key details like IP addresses, protocol type, length, and ports.

Parameters:
packets: The captured packets from the capture_packets function.
Returns:
df: A Pandas DataFrame containing parsed packet information.
visualize_data(df)
Visualizes the packet data using Seaborn plots.

Parameters:
df: A Pandas DataFrame containing packet information.
Data Visualizations
Packet Counts by Protocol: A count plot showing the number of packets for each protocol type (TCP, UDP, Other).
Packet Length Distribution: A histogram displaying the distribution of packet lengths.
