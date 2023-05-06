# Kaio Guilherme
# Código do cliente
# Importando as bibliotecas
import random
import socket
import string
import sys
import threading

args = sys.argv
print(f"N° de envios simultaneos: {args[1]} \n N° de bytes: {args[2]}")

num_bytes = int(args[3])
IP = 'localhost'
PORT = 5000
MENSSAGE = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num_bytes))
N_MESSAGES = int(args[2])
N_threads = int(args[1])

def connect_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    for _ in range(N_MESSAGES):
        # envia a mensagem para o servidor
        client.send(MENSSAGE.encode('utf-8'))

        # recebe a mensagem do servidor
        recv_message = client.recv(1024)
        #print(recv_message.decode('utf-8')) retire caso vc queira ver as mensagem enviasdas

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
