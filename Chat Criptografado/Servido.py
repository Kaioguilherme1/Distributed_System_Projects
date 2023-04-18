#kaio Guilherme
# Código do servidor

# Importando as bibliotecas
import socket
from cryptography.fernet import Fernet
import threading

IP = 'localhost'
PORT = 5000
KEY = b'ZlwQflFSUdYJJKYF5dmh3mqOsAio6aodWYTTdRT6AMw='


# Criando o socket do servidor
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f"Servidor iniciado com sucesso no IP {IP} e na porta {PORT}")
except:
    print("Erro ao criar o socket do servidor")

# Define uma função para lidar com cada cliente
def handle_client(client, address, KEY):
    while True:
        # Recebe a mensagem do cliente
        recv_mensagen = client.recv(1024)
        recv_mensagen_decrypted = f"{address} > {(Fernet(KEY).decrypt(recv_mensagen)).decode('utf-8')}"
        print(recv_mensagen_decrypted)

        #criptografa a mensagem
        recv_mensagen_encrypted = Fernet(KEY).encrypt(recv_mensagen_decrypted.encode('utf-8'))

        # Reenvia a mensagem para todos os clientes
        for c in clients:
            c.send(recv_mensagen_encrypted)

        if (recv_mensagen_decrypted == f"{address} > exit"):
            break
        
    client.close()

# Cria uma lista vazia de clientes
clients = []

while True:
    # Aceita a conexão do cliente
    client, address = server.accept()
    print(f"Conexão estabelecida com {address}!")

    # Adiciona o cliente à lista de clientes
    clients.append(client)

    # Cria uma thread para lidar com cada cliente
    client_thread = threading.Thread(target=handle_client, args=(client, address, KEY))
    client_thread.start()
