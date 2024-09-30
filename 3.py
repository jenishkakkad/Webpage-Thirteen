import socket

def reverse_string(string):
    # Reverse the string
    return string[::-1]

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific host and port
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(5)
    print('[*] Listening for connections...')

    while True:
        # Accept connections from clients
        client_socket, client_address = server_socket.accept()
        print(f'[*] Accepted connection from {client_address[0]}:{client_address[1]}')

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            # Reverse the received string
            reversed_string = reverse_string(data)

            # Send the reversed string back to the client
            client_socket.send(reversed_string.encode('utf-8'))
            print(f'[*] Sent reversed string: {reversed_string}')

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    main()
