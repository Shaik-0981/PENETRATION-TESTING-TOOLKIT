import socket

# Add the starting print statement here
print("Starting Port Scan...")

def scan_port(target, port):
    """Scan a single port to check if it is open."""
    try:
        print(f"Attempting to scan port {port} on {target}...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Increased timeout
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on {target}")
        else:
            print(f"Port {port} is closed on {target}")
        sock.close()
    except socket.error as err:
        print(f"Error scanning port {port} on {target}: {err}")

def scan_ports(target, ports):
    """Scan multiple ports on a target."""
    print(f"Scanning {target} for ports: {ports}")
    for port in ports:
        scan_port(target, port)

if __name__ == "__main__":
    target_ip = "8.8.8.8"  # Replace with a reachable IP
    ports_to_scan = [22, 80, 443, 8080]  # Common ports
    scan_ports(target_ip, ports_to_scan)
