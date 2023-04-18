# sensor

import time
import pika
import os
import psutil

HOST = '192.168.20.4'
PORT = 5672
VirtualHost = '/'
USER = 'Producer'
PASS = '1234'

# criar uma conexão com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=HOST, 
    port=PORT, 
    virtual_host=VirtualHost, 
    credentials=pika.PlainCredentials(USER, PASS)))

channel = connection.channel()

# declarar uma queue chamada 'cpu_temp'
channel.queue_declare(queue='cpu_temp')

while True:
    # obter a temperatura atual do cpu
    cpu_temp =  psutil.sensors_temperatures()['coretemp'][0].current
    # enviar a temperatura para a queue
    channel.basic_publish(exchange='', routing_key='cpu_temp', body=str(cpu_temp))
    print(f"Enviado {cpu_temp} para a queue 'cpu_temp' no RabbitMQ {HOST}:{PORT}")
    time.sleep(0.5)
    os.system('clear')


