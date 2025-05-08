import socket

def start_server():
    # Create a TCP socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the server address and port
    server_socket.bind(('localhost', 8888))
    # Start listening for client connections. A maximum of 5 connections are allowed to wait for processing in the queue
    server_socket.listen(5)
    print("Server started, listening on port 8888...")

    while True:
        # Accept the client connection and return a new socket object and the client address
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

if __name__ == "__main__":
    start_server()