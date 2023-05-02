#Kaio Guilherme
# Código do cliente

# Importando as bibliotecas
import socket
import socket
import threading

IP = 'localhost'
PORT = 5000
MENSSAGE = "Hello World"
N_MESSAGES = 1
N_threads = 100

def connect_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    for i in range(N_MESSAGES):
        # envia a mensagem para o servidor
        client.send(MENSSAGE.encode('utf-8'))

        # recebe a mensagem do servidor
        recv_message = client.recv(1024)
        print(recv_message.decode('utf-8'))
   
    client.send("exit".encode('utf-8'))
    client.close()


# cria 10 threads para 10 clientes
threads = []
for i in range(N_threads):
    thread = threading.Thread(target=connect_client)
    threads.append(thread)
    thread.start()

# espera que todas as threads terminem
for thread in threads:
    thread.join()
