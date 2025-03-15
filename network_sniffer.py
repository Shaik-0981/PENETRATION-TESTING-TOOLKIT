from scapy.all import sniff

def packet_callback(packet):
    """Callback function to display packet data."""
    print("\nPacket Summary:")
    packet.show()

def start_sniffing():
    """Start capturing network packets."""
    print("Starting network sniffing...")
    sniff(prn=packet_callback, count=10)

if __name__ == "__main__":
    start_sniffing()

