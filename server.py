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
    
    import socket
    import threading

    tuple_space = []
    lock = threading.Lock()


    def handle_client(client_socket):
        global tuple_space
        while True:
            try:
                # Receive the data sent by the client, with a maximum reception of 1024 bytes
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        # Close the client socket connection
        client_socket.close()


    def start_server():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 8888))
        server_socket.listen(5)
        print("Server started, listening on port 8888...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # Create a new thread for each client connection to handle requests
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()


    if __name__ == "__main__":
        start_server()