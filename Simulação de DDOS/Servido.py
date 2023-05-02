#kaio Guilherme
# Código do servidor

# Importando as bibliotecas
import socket
import threading
import psutil
import os
from time import sleep
import matplotlib.pyplot as plt

SERVER_PID = os.getpid()
IP = 'localhost'
PORT = 5000

print(SERVER_PID)
cpu_usage = []
num_clients = []
lock = threading.Lock()

# Criando o socket do servidor
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    print(f"Servidor iniciado com sucesso no IP {IP} e na porta {PORT}")
except:
    print("Erro ao criar o socket do servidor")

# Define uma função para lidar com cada cliente
def handle_client(client, address):
    while True:
        # Recebe a mensagem do cliente
        recv_mensagen = client.recv(1024).decode('utf-8')
        if recv_mensagen == "exit":
            break

        # inverte a mensagem
        recv_mensagen = recv_mensagen[::-1]
        client.send(recv_mensagen.encode('utf-8'))
    # Fecha a conexão com o cliente
    clients.remove(client)
    client.close()

        

        
    

# Cria uma lista vazia de clientes
clients = []

# Define uma função para atualizar a lista de uso de CPU
def get_cpu_usage():
    while True:
        with lock:
            cpu_usage.append(psutil.Process(SERVER_PID).cpu_percent(interval=1))
            num_clients.append(len(clients))


def update_plot():
    while True:
        plt.clf()
        plt.plot(num_clients, cpu_usage)
        plt.xlabel('Número de clientes')
        plt.ylabel('Uso de CPU (%)')
        plt.title('Uso de CPU em relação ao número de clientes')
        plt.pause(0.01)
        sleep(1)  # atualiza o gráfico a cada 1 segundo


# Inicia a thread para atualizar a lista de uso de CPU
cpu_thread = threading.Thread(target=get_cpu_usage)
cpu_thread.start()

while True:
    # Aceita a conexão do cliente
    client, address = server.accept()
    print(f"Conexão estabelecida com {address}!")

    # Adiciona o cliente à lista de clientes
    clients.append(client)

    # Cria uma thread para lidar com cada cliente
    client_thread = threading.Thread(target=handle_client, args=(client, address))
    client_thread.start()

    # Plota o gráfico atualizado
    #plt.plot(num_clients, cpu_usage)
    #plt.xlabel('Número de clientes')
    #plt.ylabel('Uso de CPU (%)')
    #plt.title('Uso de CPU em relação ao número de clientes')
    #plt.pause(0.01)
    print(len(clients))
    if len(cpu_usage) == 0:
        break

print(f"Uso de CPU: {cpu_usage}")
print(f"Número de clientes: {num_clients}")
