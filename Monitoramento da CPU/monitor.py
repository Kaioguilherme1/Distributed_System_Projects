#monitor

from tabulate import tabulate
import pika
import os

HOST = '192.168.20.4'
PORT = 5672
VirtualHost = '/'
USER = 'Consumer'
PASS = '1234'
data = {}


# criar uma conexão com o rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=HOST,
    port=PORT,
    virtual_host=VirtualHost,
    credentials=pika.PlainCredentials(USER, PASS)))

channel = connection.channel()

# declarar as queues que queremos monitorar
queues = ['cpu_temp', 'alerts']
# definir uma função para processar as mensagens recebidas



def callback(ch, method, properties, body):
    # obter a queue, a chave de roteamento e o corpo da mensagem
    queue = method.consumer_tag
    routing_key = method.routing_key
    message = body.decode()
    # atualizar o dicionário com os dados da mensagem
    data[queue] = [routing_key, message]
    # criar uma lista com os cabeçalhos da tabela
    headers = ['Queue', 'Routing key', 'Message']
    # criar uma lista com os valores da tabela
    values = [[queue] + value for queue, value in data.items()]
    # limpar a tela
    os.system('clear')
    # imprimir a tabela formatada usando o módulo tabulate
    print(tabulate(values, headers=headers))
    

# configurar os consumidores para receber as mensagens das queues
for queue in queues:
    channel.queue_declare(queue=queue)
    # se a queue for alerts, vincular ela ao exchange alerts com o tópico fire
    if queue == 'alerts':
        channel.queue_bind(exchange='alerts', queue=queue, routing_key='fire')
        channel.queue_bind(exchange='alerts', queue=queue, routing_key='prenvencao')
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True, consumer_tag=queue)
# iniciar o consumo das mensagens
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
