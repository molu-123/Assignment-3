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

        import socket
        import threading

        tuple_space = []
        lock = threading.Lock()


        def handle_client(client_socket):
            global tuple_space
            while True:
                try:
                    data = client_socket.recv(1024).decode('utf-8')
                    if not data:
                        break
                    # Parse the requests sent by the client
                    parts = data.split()
                    operation = parts[0]
                    if operation == 'PUT':
                        key = parts[1]
                        value = parts[2]
                        with lock:
                            # Check if the key already exists. If it exists, update it; if not, add it
                            for i, t in enumerate(tuple_space):
                                if t[0] == key:
                                    tuple_space[i] = (key, value)
                                    break
                            else:
                                tuple_space.append((key, value))
                        response = f"OK {key} {value}"
                    elif operation == 'READ':
                        key = parts[1]
                        with lock:
                            # Find the tuple of the specified key
                            for t in tuple_space:
                                if t[0] == key:
                                    response = f"OK {t[0]} {t[1]}"
                                    break
                            else:
                                response = f"NOT_FOUND {key}"
                    elif operation == 'GET':
                        key = parts[1]
                        with lock:
                            # Search for and delete the tuple of the specified key
                            for i, t in enumerate(tuple_space):
                                if t[0] == key:
                                    response = f"OK {t[0]} {t[1]}"
                                    del tuple_space[i]
                                    break
                            else:
                                response = f"NOT_FOUND {key}"
                    else:
                        response = "INVALID_OPERATION"
                    # Send the response to the client
                    client_socket.sendall(response.encode('utf-8'))
                except Exception as e:
                    print(f"Error handling client: {e}")
                    break
            client_socket.close()


        def start_server():
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('localhost', 8888))
            server_socket.listen(5)
            print("Server started, listening on port 8888...")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address}")
                client_thread = threading.Thread(target=handle_client, args=(client_socket,))
                client_thread.start()


        if __name__ == "__main__":
            start_server()