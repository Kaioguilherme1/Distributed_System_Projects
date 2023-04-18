#alert

import pika

HOST = '192.168.20.4'
PORT = 5672
VirtualHost = '/'
USER = 'Consumer'
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

# declarar um exchange chamado 'alerts' do tipo 'topic' para enviar as mensagens de alerta
channel.exchange_declare(exchange='alerts', exchange_type='topic')
# definir uma função para processar as mensagens recebidas


def callback(ch, method, properties, body):
    # converter o corpo da mensagem para um número
    cpu_temp = float(body)
    # definir o limite de temperatura
    limit = 70
    # verificar se a temperatura está acima do limite
    if cpu_temp > limit:
        # enviar uma mensagem de alerta para o exchange 'alerts' com a chave de roteamento 'fire'
        channel.basic_publish(exchange='alerts', routing_key='fire', body='Fogo na CPU!')
        print(f'Sobreaquecimento detectado: {cpu_temp}')
    else:
        # imprimir a temperatura normal
        print(f'Temperatura da CPU: {cpu_temp} °C')


# configurar o consumidor para receber as mensagens da queue 'cpu_temp'
channel.basic_consume(
    queue='cpu_temp', on_message_callback=callback, auto_ack=True)

# iniciar o consumo das mensagens
print('Iniciando o consumo das mensagens da queue "cpu_temp", para sair pressione CTRL+C')
channel.start_consuming()

