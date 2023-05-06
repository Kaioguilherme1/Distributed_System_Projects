# kaio Guilherme
# Código do servidor

import socket
import threading
import os

SERVER_PID = os.getpid()
IP = 'localhost'
PORT = 5000

print(f"PID do servidor: {SERVER_PID}")

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f"Servidor iniciado com sucesso no IP {IP} e na porta {PORT}")
except socket.error as e:
    print("Erro ao criar o socket do servidor")

# Define uma função para lidar com cada cliente
def handle_client(client: socket.socket, address):
    while True:
        # Recebe a mensagem do cliente
        recv_message = client.recv(1024).decode('utf-8')
        if recv_message == "exit":
            break

        # Inverte a mensagem
        recv_message = recv_message[::-1]
        client.send(recv_message.encode('utf-8'))

    # Fecha a conexão com o cliente
    client.close()

# Cria uma lista vazia de clientes
clients = []
clients_lock = threading.Lock()  # adicionando o lock

while True:
    # Aceita a conexão do cliente
    client, address = server.accept()
    print(f"Conexão estabelecida com {address}!")

    # Adiciona o cliente à lista de clientes
    with clients_lock:  # utilizando o lock
        clients.append(client)

    # Cria uma thread para lidar com cada cliente
    client_thread = threading.Thread(target=handle_client, args=(client, address))
    client_thread.start()