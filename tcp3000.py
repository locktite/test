# Import required libraries
# Simple Server
import socket

# Set listening port
listen_port = 3000

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to port
sock.bind(("", listen_port))

# Listen for incoming connections
sock.listen()

# Loop indefinitely
while True:
    # Accept incoming connection
    conn, addr = sock.accept()

    # Receive data from client
    data = conn.recv(1024)
    data = data.decode().strip()

    # Check for specific strings
    if data == "*":
        response = "Hello\n"
    elif data == "balance":
        response = "My balance is 100\n"
    elif data == "bye":
        response = "Goodbye\n"
        # Close connection and exit loop
        conn.close()
        break
    else:
        # Handle other strings
        response = "Invalid input\n"

    # Send response back to client
    conn.sendall(response.encode())

    # Close connection
    conn.close()

# Close socket
sock.close()
