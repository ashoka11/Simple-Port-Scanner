import socket

def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for connection attempt
        sock.settimeout(1)
        # Attempt to connect to the IP address and port
        result = sock.connect_ex((ip, port))
        # Check if the port is open
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        # Close the socket
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_range(ip, start_port, end_port):
    print(f"Scanning ports on {ip}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter starting port number: "))
    end_port = int(input("Enter ending port number: "))

    scan_range(target_ip, start_port, end_port)

