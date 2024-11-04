import socket
import threading

HOST = '127.0.0.1'  # Localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []


def broadcast(message, public=True):
    if public:
        print("****\nWRITING TO CLIENTS" + str(clients)+ "\n****")
        for client in clients:
            print(type(client))
            client.send(message)

def handle(client):
    # try to handle incoming messages
    while True:
        try:
            # 1024 bytes maximum for message
            message = client.recv(1024)
            # broadcast the message
            broadcast(message)
        except:
            # if cannot receive message then remove the client from the chat
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("****\nclient and address" + str(client)+", "+ str(address) + "\n****")
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()