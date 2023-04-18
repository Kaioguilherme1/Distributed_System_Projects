#alarme

import pika
import os
from playsound import playsound
import time
import pygame

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


channel.exchange_declare(exchange='alerts', exchange_type='topic')
channel.queue_declare(queue='alerts')


def callback(ch, method, properties, body):
    pygame.init()
    # tocar um som de alarme
    alarm = pygame.mixer.Sound("alarm.wav")
    alarm.play()
    channel.basic_publish(exchange='alerts', routing_key='prenvencao',body='Contramedida ativada')
    print(f'Fogo detectado: {body.decode()}')
    time.sleep(1)
    alarm.stop()
    pygame.quit()
    os.system('clear')
    

    


# configurar o consumidor para receber as mensagens do exchange alerts com o tópico fire
channel.queue_bind(exchange='alerts', queue='alerts', routing_key='fire')
channel.basic_consume(queue='alerts', on_message_callback=callback, auto_ack=True)


# iniciar o consumo das mensagens
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

