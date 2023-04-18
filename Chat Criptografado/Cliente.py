#Kaio Guilherme
# Código do cliente

# Importando as bibliotecas
import socket
from cryptography.fernet import Fernet

IP = 'localhost'
PORT = 5000
KEY = b'ZlwQflFSUdYJJKYF5dmh3mqOsAio6aodWYTTdRT6AMw='

# Criando o socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))


while True:
    # envia a mensagem para o servidor
    send_mensagen = input("Digite a mensagem >>> ")
    send_mensagen_encrypted = Fernet(KEY).encrypt(send_mensagen.encode('utf-8'))
    
    print(send_mensagen_encrypted)
    client.send(send_mensagen_encrypted)

    # recebe a mensagem do servidor
    recv_mensagen = client.recv(1024)
    recv_mensagen_decrypted = (Fernet(KEY).decrypt(recv_mensagen)).decode('utf-8')
    print(recv_mensagen_decrypted)

    if (send_mensagen == "exit"):
        break

client.close()
    
