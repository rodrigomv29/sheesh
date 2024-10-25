import socket

HOST = 'localhost'
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connected by {address}")

    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received data from client: {data.decode('utf-8')}")

    response = "Hello from the server"
    client_socket.sendall(response.encode('utf-8'))

    client_socket.close()


